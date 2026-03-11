# Phase Plan

## Phase 0: Repo OS Is Real

### Checklist

- [x] Restructure the repository so the active operating system lives at the root.
- [x] Quarantine the legacy proof of concept under `legacy/poc/`.
- [ ] Confirm baseline tag `arcus-foundation-20260311` points at current `main` HEAD.
- [x] Tighten [docs/project_context.md](../project_context.md) for mission, Phase 0 purpose, scope, non-goals, and truth boundaries.
- [x] Tighten [docs/guardrails.md](../guardrails.md) for contract-first, schema-first, no-drift, legacy freeze, and ADR rules.
- [x] Tighten [agents/coding_agent_contract.md](../../agents/coding_agent_contract.md) with exact required reads, allowed actions, forbidden actions, output expectations, and validation steps.
- [x] Tighten [workflows/development_workflow.md](../../workflows/development_workflow.md) so each stage names its purpose, expected outputs, and update locations.
- [x] Publish a manual GitHub settings checklist in [docs/sops/github_branch_protection_checklist.md](../sops/github_branch_protection_checklist.md).
- [x] Keep [agents/agent_registry.yaml](../../agents/agent_registry.yaml) and [schemas/manifest.schema.json](../../schemas/manifest.schema.json) minimal, realistic, and valid.
- [x] Record the Phase 0 operating model in an ADR under [docs/decisions/](../decisions/).
- [x] Confirm no edits land under `legacy/poc/` as part of Phase 0.

### Definition Of Done

Phase 0 is done when:

- The default branch has a correct baseline tag for the new operating model.
- Required reads and truth hierarchy are explicit and consistent across [README.md](../../README.md), [docs/](../), [agents/](../../agents/), [workflows/](../../workflows/), and [schemas/](../../schemas/).
- Guardrails clearly forbid unapproved changes to `legacy/poc/` and exclude it from normal context gathering.
- Workflow guidance names the required outputs for planning, implementation, verification, ADR recording, and companion updates.
- Structured repo contracts still parse cleanly.
- Contributors can determine where project truth lives without consulting external context.

### Dependencies / Blockers

- The tag `arcus-foundation-20260311` already exists but does not resolve to the current `main` HEAD. Do not move it silently; resolve the correction deliberately before checking off the baseline-tag item.
- GitHub branch protection and required status checks live outside the repo and must be applied manually using [docs/sops/github_branch_protection_checklist.md](../sops/github_branch_protection_checklist.md).

## Phase 1 Preview

- Add concrete manifest examples and lightweight validation automation.
- Expand architecture and SOP guidance for active subsystems and context ingestion.
- Add repo-level checks for link integrity, contract drift, and workflow compliance.
- Define the first active implementation contracts for adapters, prompts, or context packages.
