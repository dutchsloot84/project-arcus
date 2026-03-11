# ADR-0002: Phase 0 Means The Repo Operating System Is Real

- Status: Accepted
- Date: 2026-03-11

## Context

Project Arcus has already completed the root-level restructure that moved the prior proof of concept into `legacy/poc/` and established repo-operating-system artifacts at the root. The next risk is ambiguity: contributors could still disagree about what Phase 0 requires, which files are authoritative, and whether archived POC material should shape active work.

## Decision

Phase 0 is defined as the work required to make the repository operating system explicit, durable, and enforceable for human and coding-agent contributors. During Phase 0, the active repository truth lives at the root, `legacy/poc/` remains frozen unless explicitly targeted, and the core project documents, workflows, schemas, and agent contracts must agree on the operating model.

## Constraints

- Plan before implementation.
- Prefer contract-first and schema-first changes.
- Record material operating-model decisions as ADRs.
- Treat `legacy/poc/` as archived and out of scope for normal context gathering or edits.
- Keep Phase 0 focused on repo clarity, not new product feature delivery.

## Consequences

- Contributors have a concrete definition of Phase 0 completion.
- The repository root becomes the unambiguous entrypoint for future active work.
- Future implementation phases can build on a stable documented operating model instead of inferred convention.
