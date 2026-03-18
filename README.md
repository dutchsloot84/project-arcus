# Project Arcus

Project Arcus is a repository operating system for human and AI-assisted delivery. The repo root is the project brain: mission, decisions, guardrails, workflows, manifests, context, and agent contracts live here. The archived proof of concept remains preserved under `legacy/poc/` and is not part of the default active workspace.

## Purpose

- Keep the active project state documentation-first and deterministic.
- Give coding agents a clear read order before they change code.
- Separate active governance from archived implementation history.

## Read First

1. [planning/README.md](planning/README.md) for planning-state changes and task execution requests
2. [README.md](README.md)
3. [AI_CONTEXT.md](AI_CONTEXT.md)
4. [docs/project_context.md](docs/project_context.md)
5. [docs/guardrails.md](docs/guardrails.md)
6. [agents/coding_agent_contract.md](agents/coding_agent_contract.md)
7. [agents/agent_registry.yaml](agents/agent_registry.yaml)
8. [workflows/development_workflow.md](workflows/development_workflow.md)
9. [docs/roadmap/phase_plan.md](docs/roadmap/phase_plan.md)
10. Relevant ADRs under [docs/decisions/](docs/decisions/)
11. Relevant schemas under [schemas/](schemas/)

Do not read or use `legacy/poc/` as context unless a task explicitly directs you there.

## Repo Map

- [docs/](docs/) - architecture notes, ADRs, roadmap, SOPs, guardrails, and project context
- [planning/](planning/) - authoritative planning control plane and generated project status
- [agents/](agents/) - agent registry and coding contract
- [workflows/](workflows/) - how work moves from plan to verified change
- [schemas/](schemas/) - JSON schemas for repo manifests and structured contracts
- [src/enterprise_synthetic_data_hub/](src/enterprise_synthetic_data_hub/) - active orchestration, provider, and observability scaffolding
- [context/](context/) - ingested operational context and domain reference material
- [adapters/](adapters/) - integration-specific implementation slots
- [prompts/](prompts/) - Markdown prompt assets for planning and validation workflows
- [scenario_packs/](scenario_packs/) - curated YAML scenario definitions that remain usable without an LLM
- [tests/](tests/) - root-level repo OS checks and examples of expected behavior
- [examples/](examples/) - sample manifests, prompts, and workflow artifacts
- `legacy/poc/` - archived Enterprise Synthetic Data Hub POC

## Working Model

- Plan before implementation.
- Treat `planning/` task YAML as the source of truth for work state.
- Make schema and contract changes before downstream implementation changes.
- Record durable decisions in [docs/decisions/](docs/decisions/).
- Update manifests and docs when behavior changes.
- Treat `legacy/poc/` as read-only unless a task explicitly targets it.
- Keep new active work outside `legacy/`.

## Legacy POC

The original proof of concept has been quarantined under `legacy/poc/` so it remains runnable and reviewable without driving current project structure. Start there only when you need the archived demo stack and the task explicitly calls for legacy context.

## Contribution Flow

Use [workflows/development_workflow.md](workflows/development_workflow.md) as the default path for planning, implementation, verification, ADR updates, and manifest maintenance. Planning-state changes must follow [planning/README.md](planning/README.md). If a change affects agent behavior, also update the agent contract and registry.
