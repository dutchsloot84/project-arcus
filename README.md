# Project Arcus

Project Arcus is a repository operating system for AI-assisted delivery. The repo root is the project brain: decisions, guardrails, workflows, manifests, context, and agent contracts live here. The archived proof of concept remains preserved under `legacy/poc/`.

## Purpose

- Keep the active project state documentation-first and deterministic
- Give coding agents a clear read order before they change code
- Separate active governance from archived implementation history

## Read First

1. `docs/project_context.md`
2. `docs/guardrails.md`
3. `agents/coding_agent_contract.md`
4. `agents/agent_registry.yaml`
5. `workflows/development_workflow.md`
6. `docs/roadmap/phase_plan.md`
7. `docs/decisions/`

## Repo Map

- `docs/` - architecture notes, ADRs, roadmap, SOPs, guardrails, and project context
- `agents/` - agent registry and coding contract
- `workflows/` - how work moves from plan to verified change
- `schemas/` - JSON schemas for repo manifests and structured contracts
- `context/` - ingested operational context and domain reference material
- `adapters/` - integration-specific implementation slots
- `prompts/` - active prompt assets for the repo OS
- `tests/` - root-level repo OS checks and examples of expected behavior
- `examples/` - sample manifests, prompts, and workflow artifacts
- `legacy/poc/` - archived Enterprise Synthetic Data Hub POC

## Working Model

- Plan before implementation.
- Make schema and contract changes before downstream implementation changes.
- Record durable decisions in `docs/decisions/`.
- Update manifests and docs when behavior changes.
- Treat `legacy/poc/` as read-only unless a task explicitly targets it.

## Legacy POC

The original proof of concept has been quarantined under `legacy/poc/` so it remains runnable and reviewable without driving current project structure. Start there only when you need the archived demo stack.

## Contribution Flow

Use `workflows/development_workflow.md` as the default path for planning, implementation, verification, ADR updates, and manifest maintenance. If a change affects agent behavior, also update the agent contract and registry.
