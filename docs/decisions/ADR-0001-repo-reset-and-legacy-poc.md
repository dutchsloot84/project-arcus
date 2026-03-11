# ADR-0001: Repo Reset And Legacy POC Quarantine

- Status: Accepted
- Date: 2026-03-11

## Context

Project Arcus started as a proof-of-concept codebase centered on the Enterprise Synthetic Data Hub demo. That structure mixed implementation, prompts, governance notes, and supporting materials at the repository root. As the project shifts toward a reusable repository operating system, the root needs to represent current intent and working agreements instead of archived implementation.

## Decision

We moved the existing proof-of-concept assets into `legacy/poc/` and repurposed the repository root for active documentation, guardrails, agent contracts, workflows, schemas, adapters, context, examples, and repo-level tests.

## What Moved

The former root-level POC directories and files now live under `legacy/poc/`, including source, tests, scripts, docs, prompts, schemas, governance notes, configuration, and demo support files.

## Rules Going Forward

- Active work starts from the root repo operating system documents.
- `legacy/poc/` is archived and read-only unless a task explicitly targets it.
- New active implementation should be introduced only after its governing contract, schema, and workflow expectations are documented at the root.
- Durable decisions belong in ADRs under `docs/decisions/`.

## Consequences

- The POC remains available for reference and demo playback without shaping the active repo layout.
- Contributors and coding agents now have a single canonical entrypoint for how work should happen.
- Future migrations from the POC into active root-level structures must be intentional and documented.
