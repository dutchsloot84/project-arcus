# Project Context

## Mission

Project Arcus turns this repository into a dependable operating system for human and AI-assisted delivery. The repo root is the active control plane for mission, policy, workflow, schemas, and decisions so contributors can make changes with a shared contract, predictable review boundaries, and a clean separation from archived proof-of-concept history.

## Current Phase

Phase 0: Repo OS Is Real

## Why Phase 0 Exists

Phase 0 exists to remove ambiguity after the repo reset. The project needs a stable operating model before it grows new implementation: contributors should know what to read first, where project truth lives, which files are authoritative, and which areas are intentionally frozen. Phase 0 makes that operating model explicit inside the repo so active work does not depend on memory, chat context, or legacy implementation shortcuts.

## Scope For Phase 0

- Confirm the repo root is the canonical active workspace for all new work.
- Keep the new baseline legible and traceable on `main`.
- Preserve `legacy/poc/` as archived, frozen material outside the default context window.
- Make the required read order explicit for coding agents and human contributors.
- Keep [docs/guardrails.md](guardrails.md), [agents/coding_agent_contract.md](../agents/coding_agent_contract.md), and [workflows/development_workflow.md](../workflows/development_workflow.md) aligned.
- Make the truth hierarchy between [docs/](./), [schemas/](../schemas/), [agents/](../agents/), and [workflows/](../workflows/) explicit.
- Maintain a minimal, practical schema for project manifests and run artifacts.
- Capture material operating-model decisions in ADRs under [docs/decisions/](decisions/).
- Maintain a visible Phase 0 checklist and definition of done in [docs/roadmap/phase_plan.md](roadmap/phase_plan.md).
- Provide manual repo-setting guidance when enforcement depends on GitHub UI or repository settings.

## Non-Goals

- Building new product features or adapters beyond placeholder scaffolding.
- Migrating archived POC code into active root-level implementation.
- Expanding `legacy/poc/` behavior, tests, or documentation.
- Designing full CI/CD or release automation beyond baseline guidance.
- Replacing governance docs with informal notes or chat-only decisions.
- Inventing a large multi-agent ecosystem before the repo operating model requires it.

## Trust Boundaries And Invariants

- The active source of truth lives at the repository root, not in `legacy/poc/`.
- `legacy/poc/` is archived and frozen unless a task explicitly says otherwise.
- Durable operating decisions require an ADR under `docs/decisions/`.
- Contracts and schemas must lead implementation when behavior or structure changes.
- New active work must happen outside `legacy/`.
- External sources may inform the repo, but they do not override in-repo contracts once recorded.
- If documents disagree, follow the truth hierarchy until the conflict is resolved in-repo.

## Where The Truth Lives

Read and interpret active guidance in this precedence order:

1. [docs/](./) for mission, policy, roadmap, SOPs, and ADRs
2. [schemas/](../schemas/) for structured contract definitions
3. [agents/](../agents/) for agent operating expectations and registry metadata
4. [workflows/](../workflows/) for the default delivery sequence and update locations

Supporting materials such as `examples/`, `context/`, `adapters/`, `prompts/`, and `tests/` must align to that hierarchy and not silently redefine it.

## Operational Source Of Truth Note

Confluence and other external systems may seed context, but repository artifacts are the operational source of truth once the information is captured here. If an external source conflicts with the repo, reconcile the repo through a documented change rather than treating the external source as an override.
