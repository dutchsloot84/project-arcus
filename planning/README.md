# Planning Control Plane

The `planning/` directory is the authoritative planning control plane for Project Arcus.

- Task YAML files are the canonical source of truth.
- `planning/project_status.md` is generated from task YAML and is never canonical.
- If a task is not represented in `planning/`, it does not exist.

## Startup Behavior

1. Read `planning/README.md` first.
2. Inspect only the planning files relevant to the request.
3. Apply the smallest correct change consistent with these rules.
4. Preserve field order, schema consistency, and stable IDs.

## Folder Semantics

- `planning/backlog/` holds scoped potential work that is not yet committed.
- `planning/in_scope/` holds committed work allocated to the current execution window.
- `planning/done/` holds verified completed work.

Core invariant:

- Location defines intent.
- Status defines momentum.

## Task File Rules

Task files live directly under `planning/backlog/`, `planning/in_scope/`, or `planning/done/`.
Use the `.yaml` extension and keep fields in this exact order:

1. `id`
2. `title`
3. `status`
4. `definition_status`
5. `priority`
6. `priority_reason` when present
7. `completed_on` when present
8. `description`
9. `acceptance_criteria`
10. `dependencies`

Allowed fields:

- `id`
- `title`
- `status`
- `definition_status`
- `priority`
- `priority_reason`
- `completed_on`
- `description`
- `acceptance_criteria`
- `dependencies`

Required values:

- `status`: `planned` | `in_progress` | `blocked` | `done`
- `definition_status`: `draft` | `refinement_needed` | `ready`
- `priority`: `P0` | `P1` | `P2` | `P3`

Field rules:

- `priority_reason` is required for `P0` and `P1`.
- `completed_on` is required when `status: done` and must be omitted otherwise.
- `acceptance_criteria` is a list of strings.
- `dependencies` is a list of task IDs and may be empty.
- A task may move to `in_progress` only when `definition_status: ready`.
- A blocked task stays in `planning/in_scope/` with `status: blocked`.
- A done task moves to `planning/done/` with `status: done`.

Location rules:

- Files in `planning/backlog/` must use `status: planned`.
- Files in `planning/in_scope/` may use `status: planned`, `status: in_progress`, or `status: blocked`.
- Files in `planning/done/` must use `status: done`.

## ID Rules

- Do not invent or infer new task IDs.
- Only create a new task when the requester explicitly provides the ID.
- Preserve the exact ID format and prefix provided.
- If new task content is requested without an explicit ID, prepare the content but do not create the file.
- Never renumber existing tasks.

## Refinement Rules

If a task is ambiguous, underspecified, missing acceptance criteria, or missing dependency clarity, set `definition_status: refinement_needed`.
Make the minimum precise update needed to expose the gap.
Do not silently invent missing requirements.

## Commitment Gate

A task may move from `planning/backlog/` to `planning/in_scope/` only when:

- the "How" is defined through `description` and `acceptance_criteria`
- the "When" is decided by intentionally moving the file into `planning/in_scope/`

## Dependency Rules

A task is ready to start only when:

- `status: planned`
- `definition_status: ready`
- `dependencies` is empty or every dependency already exists in `planning/done/` with `status: done`

## Generated Status Artifact

`planning/project_status.md` must be generated from task YAML only.
Generate it with:

```powershell
python scripts/planning/generate_project_status.py
```

Generation rules:

- group primarily by priority
- surface highest-priority ready work
- surface in-progress work
- surface blocked work
- surface needs-refinement work
- surface recently completed work
- do not embellish beyond what the YAML supports

## Operating Rules

- Prefer structured planning artifacts over ad hoc notes.
- Never create duplicate truth.
- Never duplicate a task because of wording differences.
- Preserve stable task IDs.
- Treat task YAML as machine-readable contracts, not loose prose.
