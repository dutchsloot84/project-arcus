# Development Workflow

## Default Flow

1. Plan
2. Implement
3. Verify
4. Record ADR
5. Update manifests and companion docs

## 1. Plan

Purpose:
Align on scope, truth sources, and companion artifacts before any significant implementation starts.

Expected outputs:
- A short plan or scoped task breakdown
- Identified source-of-truth files to update
- Identified validation steps

Where updates go:
- [docs/project_context.md](../docs/project_context.md) if phase, mission, or scope changes
- [docs/guardrails.md](../docs/guardrails.md) if operating boundaries change
- [docs/roadmap/phase_plan.md](../docs/roadmap/phase_plan.md) if roadmap status or blockers change

Execution notes:
- Read [README.md](../README.md), [docs/project_context.md](../docs/project_context.md), [docs/guardrails.md](../docs/guardrails.md), [agents/coding_agent_contract.md](../agents/coding_agent_contract.md), [agents/agent_registry.yaml](../agents/agent_registry.yaml), [workflows/development_workflow.md](development_workflow.md), [docs/roadmap/phase_plan.md](../docs/roadmap/phase_plan.md), relevant ADRs, and relevant schemas.
- Exclude `legacy/poc/` from planning context unless the task explicitly targets legacy work.
- Split the work into small, reviewable commits when possible.

## 2. Implement

Purpose:
Apply the planned change in the smallest coherent slice while honoring contract-first and schema-first rules.

Expected outputs:
- Updated source-of-truth artifacts
- Small, reviewable commits
- No uncontrolled drift across docs, schemas, agents, and workflows

Where updates go:
- [docs/](../docs/) for policy, roadmap, SOPs, and ADRs
- [agents/](../agents/) for agent contracts and registry metadata
- [workflows/](./) for delivery process guidance
- [schemas/](../schemas/) for machine-readable contracts
- Active implementation folders outside `legacy/` when the task includes real implementation

Execution notes:
- Update the governing contract or policy file first when behavior or boundaries are changing.
- Touch the smallest coherent slice of files needed for the planned outcome.
- Keep active work outside `legacy/` unless the task explicitly targets archived POC material.

## 3. Verify

Purpose:
Prove the change is coherent and that repo contracts still agree.

Expected outputs:
- Validation notes or command results
- Confirmed YAML and JSON validity where applicable
- Confirmed absence of unintended legacy edits

Where updates go:
- Final execution summary
- Companion docs if verification uncovers stale references or contract drift

Execution notes:
- Check link and relative path correctness for edited docs and README references.
- Validate structured artifacts such as [agents/agent_registry.yaml](../agents/agent_registry.yaml) and [schemas/manifest.schema.json](../schemas/manifest.schema.json).
- Confirm no unintended files changed, especially under `legacy/poc/`.
- Run the smallest relevant verification step that proves the repo remains coherent.

## 4. Record ADR

Purpose:
Capture durable operating-model decisions so future contributors do not rely on implicit history.

Expected outputs:
- A new or updated ADR
- Clear context, decision, and consequences

Where updates go:
- [docs/decisions/](../docs/decisions/)

Execution notes:
- When the change introduces a durable operating-model decision, add or update an ADR under [docs/decisions/](../docs/decisions/).
- ADRs should explain what changed, why it changed, and the constraints that now apply.

## 5. Update Manifests And Companion Docs

Purpose:
Prevent drift between repo policy, machine-readable contracts, and contributor guidance.

Expected outputs:
- Updated manifests or schemas when structure changes
- Updated companion docs when operating guidance changes
- Roadmap or README updates when the repo operating model materially shifts

Where updates go:
- [schemas/](../schemas/)
- [docs/roadmap/](../docs/roadmap/)
- [README.md](../README.md)
- [agents/](../agents/) and [workflows/](./) when expectations change

Execution notes:
- Update manifests or schemas when new workflows, adapters, examples, or structured contracts are introduced or changed.
- Update companion docs when workflow or policy changes would otherwise create drift.
- Before closing the work, make sure docs, schemas, agents, and workflows still agree on the operating model.
