# ADR-0002: Phase 0 Operating Model

- Status: Accepted
- Date: 2026-03-11

## Context

Project Arcus completed the root-level restructure that moved the prior proof of concept into `legacy/poc/` and established repo-operating-system artifacts at the root. The next risk is ambiguity: contributors could still disagree about what Phase 0 requires, which files are authoritative, and whether archived POC material should shape active work. The project needs a durable operating model before it takes on larger implementation work.

## Decision

Phase 0 governs the repository operating system needed to make active work explicit, durable, and enforceable for human and coding-agent contributors. During Phase 0, the active repository truth lives at the root, `legacy/poc/` remains frozen unless explicitly targeted, and the core project documents, workflows, schemas, and agent contracts must agree on the operating model.

## What Phase 0 Governs

- Required reads and context hierarchy for contributors and coding agents
- Truth precedence across [docs/](../), [schemas/](../../schemas/), [agents/](../../agents/), and [workflows/](../../workflows/)
- Plan-first, contract-first, and schema-first behavior for significant work
- The freeze and context-exclusion rules for `legacy/poc/`
- Minimal structured contracts needed to describe manifests and runs
- The Phase 0 roadmap, definition of done, and manual GitHub protection checklist

## What Phase 0 Does Not Govern

- Product feature scope beyond placeholder scaffolding
- Full CI/CD or release automation design
- Automatic migration of archived POC assets into active root-level work
- A large agent ecosystem beyond the minimal operating model the repo currently needs

## Consequences

- Contributors have a concrete definition of what Phase 0 requires and where truth lives.
- The repository root becomes the unambiguous entrypoint for future active work.
- Future implementation phases can build on a stable documented operating model instead of inferred convention.
- Archived POC material remains available for reference without silently shaping active implementation.
