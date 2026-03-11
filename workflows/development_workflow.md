# Development Workflow

## Default Flow

1. Plan
2. Implement
3. Verify
4. Record ADR
5. Update manifests and companion docs

## 1. Plan

- Read `docs/project_context.md`, `docs/guardrails.md`, `agents/coding_agent_contract.md`, `agents/agent_registry.yaml`, and `docs/roadmap/phase_plan.md`.
- Confirm which root-level artifacts are in scope before editing.
- Identify whether the change affects policy, workflow, schema, manifests, or agent behavior.
- Split the work into small, reviewable commits when possible.

## 2. Implement

- Update the governing contract or policy file first when behavior or boundaries are changing.
- Touch the smallest coherent slice of files needed for the planned outcome.
- Keep active work at the repository root unless the task explicitly targets `legacy/poc/`.
- Typical implementation files:
  - `docs/project_context.md`
  - `docs/guardrails.md`
  - `agents/coding_agent_contract.md`
  - `agents/agent_registry.yaml`
  - `workflows/development_workflow.md`
  - `schemas/manifest.schema.json`

## 3. Verify

- Check link and relative path correctness for edited docs and README references.
- Validate structured artifacts such as `agents/agent_registry.yaml` and `schemas/manifest.schema.json`.
- Confirm no unintended files changed, especially under `legacy/poc/`.
- Run the smallest relevant verification step that proves the repo remains coherent.

## 4. Record ADR

- When the change introduces a durable operating-model decision, add or update an ADR under `docs/decisions/`.
- ADRs should explain what changed, why it changed, and the constraints that now apply.

## 5. Update Manifests And Companion Docs

- Update manifests or schemas when new workflows, adapters, examples, or structured contracts are introduced or changed.
- Update companion docs when workflow or policy changes would otherwise create drift.
- Before closing the work, make sure docs, schemas, agents, and workflows still agree on the operating model.
