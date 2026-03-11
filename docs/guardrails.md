# Guardrails

## Core Rules

- Contract-first: define or update the governing contract before implementation changes land.
- Schema-first: if a change alters a structured artifact, update its schema before or with the producer and consumer changes.
- No canonical drift: root docs, contracts, schemas, and ADRs are the source of truth for active work.
- Decisions live in `docs/decisions/`; temporary notes do not override ADRs.
- `legacy/poc/` is archived and must not be changed unless a task explicitly calls for it.

## Context Hierarchy

Read in this order before making changes:

1. `docs/project_context.md`
2. `docs/guardrails.md`
3. `agents/coding_agent_contract.md`
4. `agents/agent_registry.yaml`
5. `workflows/development_workflow.md`
6. `docs/roadmap/phase_plan.md`
7. `docs/decisions/`
8. `legacy/poc/` only if explicitly requested

## Documentation Rules

- Keep durable project intent in Markdown under `docs/`.
- Keep machine-consumable contracts in `schemas/` and YAML/JSON manifests.
- Update references when paths change; do not leave stale canonical links behind.

## Change Rules

- Prefer small, reviewable commits that separate structure changes from policy/content changes.
- Validate local assumptions before asking other agents or contributors to act.
- When a change introduces a new decision, add or update an ADR in the same workstream.
