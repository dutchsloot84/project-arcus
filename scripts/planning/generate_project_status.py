#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ALLOWED_DIRECTORIES = ("backlog", "in_scope", "done")
ALLOWED_FIELDS = {
    "id",
    "title",
    "status",
    "definition_status",
    "priority",
    "priority_reason",
    "completed_on",
    "description",
    "acceptance_criteria",
    "dependencies",
}
ALLOWED_STATUSES = {"planned", "in_progress", "blocked", "done"}
ALLOWED_DEFINITION_STATUSES = {"draft", "refinement_needed", "ready"}
ALLOWED_PRIORITIES = ("P0", "P1", "P2", "P3")
PRIORITY_ORDER = {priority: index for index, priority in enumerate(ALLOWED_PRIORITIES)}
LIST_FIELDS = {"acceptance_criteria", "dependencies"}
BASE_FIELD_ORDER = ["id", "title", "status", "definition_status", "priority"]
TRAILING_FIELD_ORDER = ["description", "acceptance_criteria", "dependencies"]


class PlanningError(ValueError):
    """Raised when planning data violates the repo control-plane rules."""


@dataclass(frozen=True)
class Task:
    path: Path
    location: str
    id: str
    title: str
    status: str
    definition_status: str
    priority: str
    priority_reason: str | None
    completed_on: date | None
    description: str
    acceptance_criteria: tuple[str, ...]
    dependencies: tuple[str, ...]


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_inline_list(value: str, path: Path, key: str) -> list[str]:
    value = value.strip()
    if value == "[]":
        return []
    if not (value.startswith("[") and value.endswith("]")):
        raise PlanningError(f"{path}: {key} must use a YAML list or []")
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [strip_quotes(part) for part in inner.split(",")]


def fold_block(block_lines: list[str]) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in block_lines:
        if line == "":
            if current:
                paragraphs.append(" ".join(current))
                current = []
            else:
                paragraphs.append("")
            continue
        current.append(line)
    if current:
        paragraphs.append(" ".join(current))
    return "\n\n".join(
        paragraph for paragraph in paragraphs if paragraph or len(paragraphs) == 1
    )


def parse_yaml_subset(path: Path) -> tuple[list[tuple[str, object]], dict[str, object]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    pairs: list[tuple[str, object]] = []
    payload: dict[str, object] = {}
    index = 0

    while index < len(lines):
        raw_line = lines[index]
        stripped = raw_line.strip()

        if not stripped or stripped.startswith("#"):
            index += 1
            continue

        if raw_line[:1].isspace():
            raise PlanningError(f"{path}: unexpected indentation on line {index + 1}")

        if ":" not in raw_line:
            raise PlanningError(f"{path}: expected key/value pair on line {index + 1}")

        key, remainder = raw_line.split(":", 1)
        key = key.strip()
        value = remainder.strip()

        if key not in ALLOWED_FIELDS:
            raise PlanningError(f"{path}: unknown field '{key}'")
        if key in payload:
            raise PlanningError(f"{path}: duplicate field '{key}'")

        if key in LIST_FIELDS:
            if value:
                parsed_value = parse_inline_list(value, path, key)
                pairs.append((key, parsed_value))
                payload[key] = parsed_value
                index += 1
                continue

            items: list[str] = []
            index += 1
            while index < len(lines):
                item_line = lines[index]
                item_stripped = item_line.strip()

                if not item_stripped or item_stripped.startswith("#"):
                    index += 1
                    continue

                if not item_line.startswith("  - "):
                    break

                item_value = strip_quotes(item_line[4:].strip())
                if not item_value:
                    raise PlanningError(
                        f"{path}: empty list item for '{key}' on line {index + 1}"
                    )
                items.append(item_value)
                index += 1

            pairs.append((key, items))
            payload[key] = items
            continue

        if value in {"|", ">"}:
            block_lines: list[str] = []
            index += 1
            while index < len(lines):
                block_line = lines[index]
                if block_line.startswith("  "):
                    block_lines.append(block_line[2:])
                    index += 1
                    continue
                if block_line == "":
                    block_lines.append("")
                    index += 1
                    continue
                break

            parsed_value = (
                "\n".join(block_lines).rstrip()
                if value == "|"
                else fold_block(block_lines).rstrip()
            )
            pairs.append((key, parsed_value))
            payload[key] = parsed_value
            continue

        parsed_value = strip_quotes(value)
        pairs.append((key, parsed_value))
        payload[key] = parsed_value
        index += 1

    return pairs, payload


def expected_field_order(payload: dict[str, object]) -> list[str]:
    ordered = list(BASE_FIELD_ORDER)
    if "priority_reason" in payload:
        ordered.append("priority_reason")
    if "completed_on" in payload:
        ordered.append("completed_on")
    ordered.extend(TRAILING_FIELD_ORDER)
    return ordered


def parse_completed_on(raw_value: str, path: Path) -> date:
    try:
        return date.fromisoformat(raw_value)
    except ValueError as exc:
        raise PlanningError(f"{path}: completed_on must use YYYY-MM-DD") from exc


def validate_task(
    path: Path, pairs: list[tuple[str, object]], payload: dict[str, object]
) -> Task:
    field_order = [key for key, _ in pairs]
    expected = expected_field_order(payload)
    if field_order != expected:
        raise PlanningError(
            f"{path}: fields must appear in this order: {', '.join(expected)}"
        )

    required_fields = {
        "id",
        "title",
        "status",
        "definition_status",
        "priority",
        "description",
        "acceptance_criteria",
        "dependencies",
    }
    missing = required_fields.difference(payload)
    if missing:
        missing_fields = ", ".join(sorted(missing))
        raise PlanningError(f"{path}: missing required field(s): {missing_fields}")

    status = str(payload["status"])
    definition_status = str(payload["definition_status"])
    priority = str(payload["priority"])
    location = path.parent.name

    if status not in ALLOWED_STATUSES:
        raise PlanningError(f"{path}: invalid status '{status}'")
    if definition_status not in ALLOWED_DEFINITION_STATUSES:
        raise PlanningError(
            f"{path}: invalid definition_status '{definition_status}'"
        )
    if priority not in ALLOWED_PRIORITIES:
        raise PlanningError(f"{path}: invalid priority '{priority}'")
    if location not in ALLOWED_DIRECTORIES:
        raise PlanningError(f"{path}: unexpected planning directory '{location}'")

    priority_reason = payload.get("priority_reason")
    if priority in {"P0", "P1"} and not priority_reason:
        raise PlanningError(f"{path}: priority_reason is required for {priority}")

    if status == "done":
        if location != "done":
            raise PlanningError(f"{path}: done tasks must live in planning/done/")
        if "completed_on" not in payload:
            raise PlanningError(f"{path}: completed_on is required when status is done")
    elif "completed_on" in payload:
        raise PlanningError(f"{path}: completed_on is only allowed when status is done")

    if location == "backlog" and status != "planned":
        raise PlanningError(f"{path}: backlog tasks must use status planned")
    if location == "in_scope" and status not in {"planned", "in_progress", "blocked"}:
        raise PlanningError(
            f"{path}: in_scope tasks must use planned, in_progress, or blocked"
        )
    if status == "blocked" and location != "in_scope":
        raise PlanningError(f"{path}: blocked tasks must stay in planning/in_scope/")
    if status == "in_progress" and definition_status != "ready":
        raise PlanningError(
            f"{path}: tasks may enter in_progress only when definition_status is ready"
        )

    acceptance_criteria = payload["acceptance_criteria"]
    dependencies = payload["dependencies"]
    if not isinstance(acceptance_criteria, list):
        raise PlanningError(f"{path}: acceptance_criteria must be a list")
    if not isinstance(dependencies, list):
        raise PlanningError(f"{path}: dependencies must be a list")
    if any(not isinstance(item, str) or not item for item in acceptance_criteria):
        raise PlanningError(
            f"{path}: acceptance_criteria entries must be non-empty strings"
        )
    if any(not isinstance(item, str) or not item for item in dependencies):
        raise PlanningError(f"{path}: dependencies entries must be non-empty strings")

    completed_on = None
    if "completed_on" in payload:
        completed_on = parse_completed_on(str(payload["completed_on"]), path)

    return Task(
        path=path,
        location=location,
        id=str(payload["id"]),
        title=str(payload["title"]),
        status=status,
        definition_status=definition_status,
        priority=priority,
        priority_reason=str(priority_reason) if priority_reason is not None else None,
        completed_on=completed_on,
        description=str(payload["description"]),
        acceptance_criteria=tuple(str(item) for item in acceptance_criteria),
        dependencies=tuple(str(item) for item in dependencies),
    )


def load_tasks(planning_root: Path) -> list[Task]:
    tasks: list[Task] = []
    seen_ids: dict[str, Path] = {}

    for directory in ALLOWED_DIRECTORIES:
        task_paths = sorted((planning_root / directory).glob("*.y*ml"))
        for task_path in task_paths:
            pairs, payload = parse_yaml_subset(task_path)
            task = validate_task(task_path, pairs, payload)
            if task.id in seen_ids:
                raise PlanningError(
                    f"{task_path}: duplicate task id '{task.id}' also exists at "
                    f"{seen_ids[task.id]}"
                )
            seen_ids[task.id] = task_path
            tasks.append(task)

    return tasks


def dependencies_satisfied(task: Task, tasks_by_id: dict[str, Task]) -> bool:
    for dependency_id in task.dependencies:
        dependency = tasks_by_id.get(dependency_id)
        if dependency is None:
            return False
        if dependency.location != "done" or dependency.status != "done":
            return False
    return True


def sort_key(task: Task) -> tuple[int, str]:
    return PRIORITY_ORDER[task.priority], task.id


def render_task_line(task: Task) -> str:
    relative_path = task.path.relative_to(task.path.parents[2]).as_posix()
    return f"- `{task.id}` {task.title} (`{task.priority}` | `{relative_path}`)"


def render_section(title: str, tasks: list[Task]) -> list[str]:
    lines = [f"## {title}", ""]
    if not tasks:
        lines.append("None.")
        lines.append("")
        return lines

    for priority in ALLOWED_PRIORITIES:
        priority_tasks = [task for task in tasks if task.priority == priority]
        if not priority_tasks:
            continue
        lines.append(f"### {priority}")
        lines.extend(render_task_line(task) for task in priority_tasks)
        lines.append("")
    return lines


def render_project_status(tasks: list[Task]) -> str:
    tasks_by_id = {task.id: task for task in tasks}

    ready = sorted(
        [
            task
            for task in tasks
            if task.status == "planned"
            and task.definition_status == "ready"
            and dependencies_satisfied(task, tasks_by_id)
        ],
        key=sort_key,
    )
    in_progress = sorted(
        [task for task in tasks if task.status == "in_progress"], key=sort_key
    )
    blocked = sorted([task for task in tasks if task.status == "blocked"], key=sort_key)
    needs_refinement = sorted(
        [
            task
            for task in tasks
            if task.status != "done" and task.definition_status == "refinement_needed"
        ],
        key=sort_key,
    )
    recently_completed = sorted(
        [task for task in tasks if task.status == "done"],
        key=lambda task: (
            task.completed_on is None,
            date.min if task.completed_on is None else -task.completed_on.toordinal(),
            PRIORITY_ORDER[task.priority],
            task.id,
        ),
    )[:5]

    lines = [
        "# Project Status",
        "",
        "This file is generated from task YAML under `planning/`. Do not edit it manually.",
        "",
    ]
    lines.extend(render_section("Highest-Priority Ready Work", ready))
    lines.extend(render_section("In-Progress Work", in_progress))
    lines.extend(render_section("Blocked Work", blocked))
    lines.extend(render_section("Needs-Refinement Work", needs_refinement))
    lines.extend(render_section("Recently Completed Work", recently_completed))
    return "\n".join(lines).rstrip() + "\n"


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate planning/project_status.md from task YAML."
    )
    parser.add_argument(
        "--planning-root",
        default=str(repo_root_from_script() / "planning"),
        help="Path to the planning directory.",
    )
    parser.add_argument(
        "--output",
        default=str(repo_root_from_script() / "planning" / "project_status.md"),
        help="Path to the generated markdown output.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero when the output file is missing or out of date.",
    )
    args = parser.parse_args()

    planning_root = Path(args.planning_root).resolve()
    output_path = Path(args.output).resolve()

    tasks = load_tasks(planning_root)
    rendered = render_project_status(tasks)

    if args.check:
        current = output_path.read_text(encoding="utf-8") if output_path.exists() else None
        if current != rendered:
            raise SystemExit(1)
        return 0

    output_path.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
