# Coding Agent Contract

## Plan-First Behavior

The coding agent must plan before implementing. Do not start significant implementation until the current task plan, scope, and companion artifact updates are clear.

## Context Hierarchy / Required Reads

Before changing files, read in this order:

1. [README.md](../README.md)
2. [planning/README.md](../planning/README.md) for planning-state work
3. [AI_CONTEXT.md](../AI_CONTEXT.md)
4. [docs/project_context.md](../docs/project_context.md)
5. [docs/guardrails.md](../docs/guardrails.md)
6. [agents/coding_agent_contract.md](coding_agent_contract.md)
7. [agents/agent_registry.yaml](agent_registry.yaml)
8. [workflows/development_workflow.md](../workflows/development_workflow.md)
9. [docs/roadmap/phase_plan.md](../docs/roadmap/phase_plan.md)
10. relevant ADRs under [docs/decisions/](../docs/decisions/)
11. relevant schemas under [schemas/](../schemas/)

`legacy/poc/` is excluded from required reads unless a task explicitly requests legacy context.

Interpret repo truth in this precedence order:

1. [planning/](../planning/)
2. [docs/](../docs/)
3. [schemas/](../schemas/)
4. [agents/](./)
5. [workflows/](../workflows/)

## Allowed Actions

- Read the required project context before editing.
- Treat `planning/` task YAML as canonical when the request changes planning state.
- Update root-level docs, schemas, workflows, `src/` packages, examples, tests, prompts, scenario packs, adapters, and context assets when they are in scope.
- Add active work only outside `legacy/`.
- Make the smallest coherent set of changes needed to satisfy the approved plan.
- Keep commits small, reviewable, and clearly scoped.
- Update related contracts, manifests, workflows, or ADRs when a durable change requires them.
- Run minimal validation needed to prove the change is coherent.
- Prefer MCP-mediated access when an approved MCP path exists for the requested resource.

## Forbidden Actions

- Do not edit anything under `legacy/poc/` unless explicitly requested.
- Do not read or use `legacy/poc/` for context unless explicitly directed.
- Do not create new active implementation under `legacy/`.
- Do not treat archived POC files as active source of truth.
- Do not treat `planning/project_status.md` as canonical.
- Do not bypass permissioned interfaces when approved MCP-mediated access exists.
- Do not treat archived, external, or sensitive resources as available unless they are explicitly granted.
- Do not skip contract or schema updates when behavior, structure, or policy changes require them.
- Do not leave root docs, planning, schemas, agents, and workflows in a conflicting state.
- Do not start significant implementation before the plan is clear.
- Do not make destructive git changes unless the task explicitly authorizes them.

## Output / Update Expectations

- Provide short progress updates while substantial work is underway.
- State what changed and why in the final summary.
- List validation performed and any gaps.
- Call out assumptions if a decision could not be derived from the repo.
- Reference the exact files updated when describing important changes.
- When policy or workflow changes, note which companion artifacts were updated to prevent drift.

## Artifact Update Expectations

When making a durable repo change, update the smallest relevant set of companion artifacts:

- [docs/project_context.md](../docs/project_context.md) when mission, phase, scope, or truth hierarchy changes.
- [planning/README.md](../planning/README.md) and task YAML when planning rules or work state change.
- [docs/guardrails.md](../docs/guardrails.md) when operating rules or boundaries change.
- [workflows/development_workflow.md](../workflows/development_workflow.md) when the expected delivery sequence changes.
- [agents/agent_registry.yaml](agent_registry.yaml) when agent read order, write scope, or blocked paths change.
- [schemas/manifest.schema.json](../schemas/manifest.schema.json) when structured manifest expectations change.
- [docs/decisions/](../docs/decisions/) when the change introduces a material decision.

## Validation Checklist

- Verify the changed files are the intended source of truth.
- Regenerate `planning/project_status.md` after task YAML changes.
- Check for stale references caused by renames or path changes.
- Validate YAML and JSON artifacts after editing them.
- Confirm Markdown links still resolve sensibly after edits.
- Confirm no files under `legacy/poc/` were modified unless explicitly requested.
- Run the smallest relevant checks that prove the change is coherent.
- Leave the worktree clean, or clearly explain any intentionally preserved local state.
