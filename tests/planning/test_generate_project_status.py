from __future__ import annotations

import importlib.util
import sys
import textwrap
from pathlib import Path

import pytest


def load_module():
    script_path = (
        Path(__file__).resolve().parents[2]
        / "scripts"
        / "planning"
        / "generate_project_status.py"
    )
    spec = importlib.util.spec_from_file_location("generate_project_status", script_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_task(path: Path, content: str) -> None:
    normalized = textwrap.dedent(content).strip() + "\n"
    path.write_text(normalized, encoding="utf-8")


def make_planning_root(tmp_path: Path) -> Path:
    planning_root = tmp_path / "planning"
    for directory in ("backlog", "in_scope", "done"):
        (planning_root / directory).mkdir(parents=True)
    return planning_root


def test_renders_sections_grouped_by_priority(tmp_path: Path) -> None:
    module = load_module()
    planning_root = make_planning_root(tmp_path)

    write_task(
        planning_root / "done" / "ARC-100.yaml",
        """
        id: ARC-100
        title: Shared dependency
        status: done
        definition_status: ready
        priority: P1
        priority_reason: Unblocks current execution
        completed_on: 2026-03-17
        description: Dependency task
        acceptance_criteria:
          - Done
        dependencies: []
        """,
    )
    write_task(
        planning_root / "backlog" / "ARC-010.yaml",
        """
        id: ARC-010
        title: Highest ready task
        status: planned
        definition_status: ready
        priority: P0
        priority_reason: Immediate control-plane priority
        description: Ready now
        acceptance_criteria:
          - Add the thing
        dependencies:
          - ARC-100
        """,
    )
    write_task(
        planning_root / "in_scope" / "ARC-020.yaml",
        """
        id: ARC-020
        title: Active work
        status: in_progress
        definition_status: ready
        priority: P2
        description: In progress
        acceptance_criteria:
          - Keep moving
        dependencies: []
        """,
    )
    write_task(
        planning_root / "in_scope" / "ARC-030.yaml",
        """
        id: ARC-030
        title: Blocked work
        status: blocked
        definition_status: ready
        priority: P1
        priority_reason: Important but waiting
        description: Blocked by external issue
        acceptance_criteria:
          - Resume after unblock
        dependencies: []
        """,
    )
    write_task(
        planning_root / "backlog" / "ARC-040.yaml",
        """
        id: ARC-040
        title: Needs clarification
        status: planned
        definition_status: refinement_needed
        priority: P3
        description: Missing details
        acceptance_criteria: []
        dependencies: []
        """,
    )

    tasks = module.load_tasks(planning_root)
    rendered = module.render_project_status(tasks)

    assert "## Highest-Priority Ready Work" in rendered
    assert rendered.index("`ARC-010`") < rendered.index("`ARC-020`")
    assert "## In-Progress Work" in rendered
    assert "## Blocked Work" in rendered
    assert "## Needs-Refinement Work" in rendered
    assert "## Recently Completed Work" in rendered
    assert "`ARC-100` Shared dependency" in rendered


def test_rejects_done_task_without_completed_on(tmp_path: Path) -> None:
    module = load_module()
    planning_root = make_planning_root(tmp_path)

    write_task(
        planning_root / "done" / "ARC-100.yaml",
        """
        id: ARC-100
        title: Missing completion date
        status: done
        definition_status: ready
        priority: P2
        description: Invalid task
        acceptance_criteria:
          - Done
        dependencies: []
        """,
    )

    with pytest.raises(module.PlanningError, match="completed_on is required"):
        module.load_tasks(planning_root)


def test_rejects_in_progress_task_without_ready_definition(tmp_path: Path) -> None:
    module = load_module()
    planning_root = make_planning_root(tmp_path)

    write_task(
        planning_root / "in_scope" / "ARC-200.yaml",
        """
        id: ARC-200
        title: Premature execution
        status: in_progress
        definition_status: draft
        priority: P2
        description: Invalid task
        acceptance_criteria:
          - Not allowed
        dependencies: []
        """,
    )

    with pytest.raises(
        module.PlanningError,
        match="in_progress only when definition_status is ready",
    ):
        module.load_tasks(planning_root)
