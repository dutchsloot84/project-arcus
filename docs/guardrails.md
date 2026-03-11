# Guardrails

## Core Rules

- Plan first: do not implement significant work before the plan, scope, and update targets are clear.
- Contract-first: define or update the governing contract before implementation changes land.
- Schema-first: if a change alters a structured artifact, update its schema before or with the producer and consumer changes.
- No drift: root docs, contracts, schemas, workflows, and ADRs are the source of truth for active work and must stay aligned.
- Legacy freeze rule: do not edit anything under `legacy/poc/` unless explicitly requested.
- Legacy context rule: do not use `legacy/poc/` as context unless a task explicitly directs legacy context gathering.
- Active-work boundary: new active work must happen outside `legacy/`.
- ADR rule: an ADR under `docs/decisions/` is required for material decisions that change repo policy, workflow, or operating boundaries.

## Context Hierarchy / Required Reads

Read in this order before making changes:

1. [README.md](../README.md)
2. [docs/project_context.md](project_context.md)
3. [docs/guardrails.md](guardrails.md)
4. [agents/coding_agent_contract.md](../agents/coding_agent_contract.md)
5. [agents/agent_registry.yaml](../agents/agent_registry.yaml)
6. [workflows/development_workflow.md](../workflows/development_workflow.md)
7. [docs/roadmap/phase_plan.md](roadmap/phase_plan.md)
8. relevant ADRs under [docs/decisions/](decisions/)
9. relevant schemas under [schemas/](../schemas/)

`legacy/poc/` is excluded from the default read path and may only be consulted when a task explicitly asks for legacy context.

When files disagree, apply this truth hierarchy until the repo is reconciled:

1. [docs/](./)
2. [schemas/](../schemas/)
3. [agents/](../agents/)
4. [workflows/](../workflows/)

## Documentation Rules

- Keep durable project intent and policy in Markdown under `docs/`.
- Keep machine-consumable contracts in `schemas/` and YAML or JSON manifests.
- Update references when paths change; do not leave stale canonical links behind.
- Do not treat chat transcripts, scratch notes, or legacy POC docs as active authority.

## Change Rules

- Prefer small, reviewable commits that separate policy, workflow, and optional hygiene changes.
- Validate local assumptions before asking other agents or contributors to act.
- Update affected contracts, workflows, manifests, and ADRs in the same workstream when the change is durable.
