# Guardrails

## Core Rules

- Planning control-plane rule: `planning/` task YAML is authoritative for work state, and `planning/project_status.md` is generated only.
- Plan first: do not implement significant work before the plan, scope, and update targets are clear.
- Contract-first: define or update the governing contract before implementation changes land.
- Schema-first: if a change alters a structured artifact, update its schema before or with the producer and consumer changes.
- No drift: root docs, planning files, contracts, schemas, workflows, and ADRs are the source of truth for active work and must stay aligned.
- Policy-in-interface rule: enforce policy through permissioned interfaces and tools, not prompts alone.
- Legacy freeze rule: do not edit anything under `legacy/poc/` unless explicitly requested.
- Legacy context rule: do not use `legacy/poc/` as context unless a task explicitly directs legacy context gathering.
- Active-work boundary: new active work must happen outside `legacy/`.
- Permissioned mutation rule: mutation paths should be scoped, permissioned, and validated.
- No broad-write rule: do not give agents broad unvalidated write access.
- ScenarioSpec-only planner rule: planner providers and LLM-backed steps may only propose structured `ScenarioSpec` objects.
- Generator ownership rule: the deterministic generator remains the only component allowed to create final synthetic records or assign `synthetic_source`.
- Policy gate rule: planner output must clear a policy gate before generator execution can proceed.
- ADR rule: an ADR under `docs/decisions/` is required for material decisions that change repo policy, workflow, or operating boundaries.

## Context Hierarchy / Required Reads

Read in this order before making changes:

1. [README.md](../README.md)
2. [planning/README.md](../planning/README.md) for planning-state changes
3. [AI_CONTEXT.md](../AI_CONTEXT.md)
4. [docs/project_context.md](project_context.md)
5. [docs/guardrails.md](guardrails.md)
6. [agents/coding_agent_contract.md](../agents/coding_agent_contract.md)
7. [agents/agent_registry.yaml](../agents/agent_registry.yaml)
8. [workflows/development_workflow.md](../workflows/development_workflow.md)
9. [docs/roadmap/phase_plan.md](roadmap/phase_plan.md)
10. relevant ADRs under [docs/decisions/](decisions/)
11. relevant schemas under [schemas/](../schemas/)

`legacy/poc/` is excluded from the default read path and may only be consulted when a task explicitly asks for legacy context.

When files disagree, apply this truth hierarchy until the repo is reconciled:

1. [planning/](../planning/)
2. [docs/](./)
3. [schemas/](../schemas/)
4. [agents/](../agents/)
5. [workflows/](../workflows/)

## Documentation Rules

- Keep durable project intent and policy in Markdown under `docs/`.
- Keep canonical planning state in task YAML under `planning/`.
- Keep machine-consumable contracts in `schemas/` and YAML or JSON manifests.
- Update references when paths change; do not leave stale canonical links behind.
- Do not treat chat transcripts, scratch notes, or legacy POC docs as active authority.

## Change Rules

- Prefer small, reviewable commits that separate policy, workflow, and optional hygiene changes.
- Validate local assumptions before asking other agents or contributors to act.
- Update affected planning files, contracts, workflows, manifests, and ADRs in the same workstream when the change is durable.
- When an approved MCP path exists, prefer it over broad raw access.

## Canonical Data Mutation Policy

- Canonical model changes must go through formal review.
- QA or RapidBotz convenience tweaks may not bypass deterministic seed behavior.
- Environment-specific overrides are not permitted in the canonical model.
- Dataset variations must be derived from seed and contract inputs, not manual post-generation edits.
- Requests to expand entities, consumers, environments, or scenario breadth trigger scope review.

## Deterministic Seed Guarantees

- Reproducibility depends on a fixed deterministic seed, fixed logic state, fixed schema or canonical version, and a controlled execution boundary.
- The same seed and the same canonical version must produce identical outputs for the same scenario inputs.
- Generation manifests must log the seed, canonical version, and logic version needed for replay.
- Golden snapshot reproducibility is part of the pilot baseline, not an optional quality check.
- If replay cannot reproduce the same dataset artifacts, the pilot baseline is considered unstable.

## Canonical Drift Prevention Rules

- Scenario contracts must stay versioned and validated before generation.
- Provider-backed planning must stay behind shared provider abstractions and observable policy enforcement.
- Validation failure moves a scenario out of active use until drift is resolved.
- Deprecated or retired scenarios must not silently return to active use.
- Canonical growth is intentionally constrained during Phase 0 to prevent uncontrolled expansion.
- Material changes to the baseline should be documented in an ADR under [docs/decisions/](decisions/).

## Governance Guarantees

- Phase 0 has zero intended production write impact.
- The dataset registry is metadata-only and should point to manifests or artifacts rather than act as a second raw-data store.
- Canonical ownership, adapter ownership, application ownership, QA ownership, and DevOps ownership remain distinct.
- No autonomous or runtime schema mutation is allowed in the pilot baseline.
- Governance exists to preserve auditability, bounded scope, and exact replay rather than maximize scenario volume.
- `legacy/poc/` remains denied by default for agent mutation paths.
