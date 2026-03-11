# Phase Plan

## Phase 0: Repo OS Is Real

### Checklist

- [x] Restructure the repository so the active operating system lives at the root.
- [x] Quarantine the legacy proof of concept under `legacy/poc/`.
- [x] Lock the new foundation with a same-day baseline tag on the default branch.
- [x] Tighten `docs/project_context.md` for Phase 0 scope, non-goals, and truth hierarchy.
- [x] Tighten `docs/guardrails.md` for contract-first, schema-first, no-drift, and legacy-freeze rules.
- [ ] Tighten `agents/coding_agent_contract.md` with required reads, allowed actions, forbidden actions, and validation expectations.
- [ ] Tighten `workflows/development_workflow.md` so each step names the artifacts it must update.
- [ ] Confirm `agents/agent_registry.yaml` and `schemas/manifest.schema.json` remain valid after Phase 0 tightening.
- [ ] Record any material operating-model clarification in an ADR.
- [ ] Confirm no edits land under `legacy/poc/` as part of Phase 0.

### Definition Of Done

Phase 0 is done when:

- The default branch has a baseline tag for the new operating model.
- Required reads and truth hierarchy are explicit and consistent across docs and agent contracts.
- Guardrails clearly forbid unapproved changes to `legacy/poc/`.
- Workflow guidance names the required updates for planning, implementation, verification, ADR recording, and manifest maintenance.
- Structured repo contracts still parse cleanly.
- Contributors can determine where project truth lives without consulting external context.

## Phase 1 Preview

- Add concrete manifest examples and lightweight validation automation.
- Expand architecture and SOP guidance for active subsystems and context ingestion.
- Add repo-level checks for link integrity, contract drift, and workflow compliance.
- Define the first active implementation contracts for adapters, prompts, or context packages.
