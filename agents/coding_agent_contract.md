# Coding Agent Contract

## Plan-First Rule

The coding agent must plan before implementing. Do not change files, create commits, or run risky commands until the current task plan is clear and any required approval has been received.

## Context Hierarchy / Required Reads

Before changing files, read in this order:

1. `docs/project_context.md`
2. `docs/guardrails.md`
3. `agents/coding_agent_contract.md`
4. `agents/agent_registry.yaml`
5. `workflows/development_workflow.md`
6. `docs/roadmap/phase_plan.md`
7. relevant ADRs under `docs/decisions/`

Interpret repo truth in this precedence order:

1. `docs/`
2. `schemas/`
3. `agents/`
4. `workflows/`

## Allowed Actions

- Read the required project context before editing.
- Update root-level docs, schemas, workflows, examples, tests, prompts, adapters, and context assets when they are in scope.
- Make the smallest coherent set of changes needed to satisfy the approved plan.
- Keep commits small, reviewable, and clearly scoped.
- Update related contracts, manifests, workflows, or ADRs when a durable change requires them.
- Run minimal validation needed to prove the change is coherent.

## Forbidden Actions

- Do not edit anything under `legacy/poc/` unless explicitly requested.
- The coding agent must not read `legacy/poc/` for context unless explicitly directed.
- Do not treat archived POC files as active source of truth.
- Do not skip contract or schema updates when behavior, structure, or policy changes require them.
- Do not leave root docs, schemas, agents, and workflows in a conflicting state.
- Do not make destructive git changes unless the task explicitly authorizes them.

## Output Expectations

- State what changed and why.
- List validation performed and any gaps.
- Call out assumptions if a decision could not be derived from the repo.
- Reference the exact files updated when describing important changes.
- When policy or workflow changes, note which companion artifacts were updated to prevent drift.

## Artifact Update Expectations

When making a durable repo change, update the smallest relevant set of companion artifacts:

- `docs/project_context.md` when mission, phase, scope, or truth hierarchy changes.
- `docs/guardrails.md` when operating rules or boundaries change.
- `workflows/development_workflow.md` when the expected delivery sequence changes.
- `agents/agent_registry.yaml` when agent read order, write scope, or blocked paths change.
- `docs/decisions/` when the change introduces a material decision.

## Validation Checklist

- Verify the changed files are the intended source of truth.
- Check for stale references caused by renames or path changes.
- Validate YAML and JSON artifacts after editing them.
- Confirm no files under `legacy/poc/` were modified unless explicitly requested.
- Run the smallest relevant checks that prove the change is coherent.
- Leave the worktree clean, or clearly explain any intentionally preserved local state.
