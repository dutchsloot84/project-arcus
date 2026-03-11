# Project Context

## Mission

Project Arcus turns this repository into a dependable operating system for human and AI-assisted delivery. The repo root is the active control plane for mission, policy, workflow, schemas, and decisions so contributors can make changes with a shared contract, predictable review boundaries, and a clean separation from archived proof-of-concept history.

## Current Phase

Phase 0: Repo OS Is Real

## Scope For Phase 0

- Lock the new repository baseline on the default branch.
- Treat the root repository layout as the canonical active workspace.
- Preserve `legacy/poc/` as archived, frozen reference material.
- Tighten project context, guardrails, workflow, and agent contract documents.
- Make required reads and truth hierarchy explicit for coding agents.
- Ensure structured repo artifacts have a clear schema and ownership story.
- Define a minimal definition of done for repo-operating-system readiness.
- Record durable operating-model decisions in ADRs.

## Non-Goals

- Building new product features or adapters beyond placeholder scaffolding.
- Migrating archived POC code into active root-level implementation.
- Expanding `legacy/poc/` behavior, tests, or documentation.
- Designing full CI/CD or release automation beyond baseline guidance.
- Replacing governance docs with informal notes or chat-only decisions.

## Trust Boundaries And Invariants

- The active source of truth lives at the repository root, not in `legacy/poc/`.
- `legacy/poc/` is archived and frozen unless a task explicitly says otherwise.
- Durable operating decisions require an ADR under `docs/decisions/`.
- Contracts and schemas must lead implementation when behavior or structure changes.
- If documents disagree, follow the truth hierarchy until the conflict is resolved in-repo.

## Where The Truth Lives

Read and interpret active guidance in this precedence order:

1. `docs/`
2. `schemas/`
3. `agents/`
4. `workflows/`

Supporting materials such as `examples/`, `context/`, `adapters/`, `prompts/`, and `tests/` must align to that hierarchy and not silently redefine it.
