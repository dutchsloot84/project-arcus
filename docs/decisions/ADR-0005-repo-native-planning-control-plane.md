# ADR-0005: Repo-Native Planning Control Plane

- Status: Accepted
- Date: 2026-03-18

## Context

Project Arcus already treats repo artifacts as the active source of truth for policy, workflow, and implementation guidance. Planning state, however, was still implicit across chat context, roadmap notes, and contributor interpretation rather than expressed through one canonical, machine-readable control plane.

Arcus needs planning changes to be deterministic, minimal, and auditable inside the repo itself. That requires a single place where task intent, execution momentum, readiness, dependency state, and completion can be inspected without treating generated summaries as authority.

## Decision

Arcus will use `planning/` as its repo-native planning control plane.

- Task YAML files under `planning/backlog/`, `planning/in_scope/`, and `planning/done/` are the canonical source of truth for task state.
- Folder location encodes intent, while task `status` encodes current momentum.
- `planning/project_status.md` is a generated artifact derived from task YAML only and is never canonical.
- Contributors must not invent task IDs. New task files require an explicit user- or project-provided ID.
- Planning changes must preserve stable IDs, exact field order, and the smallest compliant mutation needed to reflect reality.

## Consequences

- Arcus gets an auditable planning layer that can be reviewed, diffed, and regenerated directly from repo state.
- Generated status views become safe to consume because they are explicitly derived and non-authoritative.
- Contributors have a clear rule for planning moves: backlog for potential work, in-scope for committed execution, and done for verified completion.
- Requests that describe new work without an explicit task ID now stop short of file creation and must return prepared content instead.

## Alternatives Considered

### Roadmap-Only Tracking

Roadmap notes help with phase visibility, but they are too coarse to act as canonical task contracts or support deterministic status generation.

### Chat-Or Comment-Driven Planning State

This is easy to start with, but it creates duplicate truth, weak auditability, and inconsistent task identity.

### Generated Status As Source Of Truth

This would make summaries easy to read, but it would collapse the distinction between canonical planning contracts and derived reporting.

## What Is Explicitly In Scope Now

- the `planning/` directory structure
- task YAML rules and movement semantics
- deterministic generation of `planning/project_status.md`
- companion workflow and contributor guidance updates needed to keep repo truth aligned

## What Is Explicitly Not In Scope Yet

- auto-creating task IDs
- external planning tools as canonical authorities
- broad roadmap rewrites beyond the planning control-plane decision
- additional task metadata beyond what the planning rules require for deterministic status generation
