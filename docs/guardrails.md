# Guardrails

## Core Rules

- Plan first: write or confirm the implementation plan before changing files.
- Contract-first: define or update the governing contract before implementation changes land.
- Schema-first: if a change alters a structured artifact, update its schema before or with the producer and consumer changes.
- No drift: root docs, contracts, schemas, workflows, and ADRs are the source of truth for active work and must stay aligned.
- Legacy freeze rule: Do not edit anything under `legacy/poc/` unless explicitly requested.
- Decision logging rule: an ADR under `docs/decisions/` is required for material decisions that change repo policy, workflow, or operating boundaries.

## Context Hierarchy / Required Reads

Read in this order before making changes:

1. `docs/project_context.md`
2. `docs/guardrails.md`
3. `agents/coding_agent_contract.md`
4. `agents/agent_registry.yaml`
5. `workflows/development_workflow.md`
6. `docs/roadmap/phase_plan.md`
7. relevant files under `docs/decisions/`
8. `legacy/poc/` only if a task explicitly directs it

When files disagree, apply this truth hierarchy until the repo is reconciled:

1. `docs/`
2. `schemas/`
3. `agents/`
4. `workflows/`

## Documentation Rules

- Keep durable project intent and policy in Markdown under `docs/`.
- Keep machine-consumable contracts in `schemas/` and YAML or JSON manifests.
- Update references when paths change; do not leave stale canonical links behind.
- Do not treat chat transcripts, scratch notes, or legacy POC docs as active authority.

## Change Rules

- Prefer small, reviewable commits that separate policy, workflow, and optional hygiene changes.
- Validate local assumptions before asking other agents or contributors to act.
- Update affected contracts, workflows, manifests, and ADRs in the same workstream when the change is durable.
