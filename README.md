# Project Arcus

Project Arcus is a repository operating system for human and AI-assisted delivery. The repo root is the project brain: mission, decisions, guardrails, workflows, manifests, context, and agent contracts live here. The archived proof of concept remains preserved under `legacy/poc/` and is not part of the default active workspace.

## Purpose

- Keep the active project state documentation-first and deterministic.
- Give coding agents a clear read order before they change code.
- Separate active governance from archived implementation history.

## Read First

1. [README.md](README.md)
2. [docs/project_context.md](docs/project_context.md)
3. [docs/guardrails.md](docs/guardrails.md)
4. [agents/coding_agent_contract.md](agents/coding_agent_contract.md)
5. [agents/agent_registry.yaml](agents/agent_registry.yaml)
6. [workflows/development_workflow.md](workflows/development_workflow.md)
7. [docs/roadmap/phase_plan.md](docs/roadmap/phase_plan.md)
8. Relevant ADRs under [docs/decisions/](docs/decisions/)
9. Relevant schemas under [schemas/](schemas/)

Do not read or use `legacy/poc/` as context unless a task explicitly directs you there.

## Repo Map

- [docs/](docs/) - architecture notes, ADRs, roadmap, SOPs, guardrails, and project context
- [agents/](agents/) - agent registry and coding contract
- [workflows/](workflows/) - how work moves from plan to verified change
- [schemas/](schemas/) - JSON schemas for repo manifests and structured contracts
- [orchestration/](orchestration/) - planner contracts, policy gate scaffolding, and ScenarioSpec validation
- [providers/](providers/) - provider abstraction for mock, local, and future Bedrock planners
- [observability/](observability/) - audit, trace, and cost-tracking interfaces for orchestration
- [context/](context/) - ingested operational context and domain reference material
- [adapters/](adapters/) - integration-specific implementation slots
- [prompts/](prompts/) - active prompt assets for the repo OS
- [tests/](tests/) - root-level repo OS checks and examples of expected behavior
- [examples/](examples/) - sample manifests, prompts, and workflow artifacts
- `legacy/poc/` - archived Enterprise Synthetic Data Hub POC

## Working Model

- Plan before implementation.
- Make schema and contract changes before downstream implementation changes.
- Record durable decisions in [docs/decisions/](docs/decisions/).
- Update manifests and docs when behavior changes.
- Treat `legacy/poc/` as read-only unless a task explicitly targets it.
- Keep new active work outside `legacy/`.

## Legacy POC

The original proof of concept has been quarantined under `legacy/poc/` so it remains runnable and reviewable without driving current project structure. Start there only when you need the archived demo stack and the task explicitly calls for legacy context.

## Contribution Flow

Use [workflows/development_workflow.md](workflows/development_workflow.md) as the default path for planning, implementation, verification, ADR updates, and manifest maintenance. If a change affects agent behavior, also update the agent contract and registry.
