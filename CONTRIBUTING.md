# Contributing To Project Arcus

Project Arcus uses the repository root as its operating system. Contributions should strengthen the contracts, workflows, schemas, and documented context that guide future implementation.

## Before You Change Anything

1. Read [README.md](README.md).
2. Read [planning/README.md](planning/README.md) before any planning-state edit.
3. Read [docs/project_context.md](docs/project_context.md).
4. Read [docs/guardrails.md](docs/guardrails.md).
5. Read [agents/coding_agent_contract.md](agents/coding_agent_contract.md).
6. Read [agents/agent_registry.yaml](agents/agent_registry.yaml).
7. Read [workflows/development_workflow.md](workflows/development_workflow.md).
8. Review [docs/roadmap/phase_plan.md](docs/roadmap/phase_plan.md), relevant ADRs in [docs/decisions/](docs/decisions/), and relevant files in [schemas/](schemas/).

## Default Contribution Pattern

1. Plan the change.
2. Update `planning/` task YAML first when the request changes planning state.
3. Update contracts or schemas first when the change affects structure or policy.
4. Implement the smallest coherent slice.
5. Verify the change locally.
6. Record the decision in an ADR when the change is durable.
7. Update manifests, examples, and docs before closing the work.

## Legacy Boundary

- `legacy/poc/` is archived.
- Do not modify `legacy/poc/` unless the task explicitly calls for a legacy change.
- Do not use `legacy/poc/` as default context for active work.
- If you need something from the POC in active work, migrate it intentionally and document the decision.
- Keep new active work outside `legacy/`.

## Commit Expectations

- Keep commits small and reviewable.
- Separate file moves from policy or content changes when possible.
- Prefer explicit commit messages that describe the repo-level effect.

## Validation Expectations

- Validate YAML and JSON after editing them.
- Regenerate `planning/project_status.md` after task YAML changes.
- Check for stale links or outdated path references after moves.
- Run the smallest relevant verification step that proves the change is coherent.

## Ownership

See [`.github/CODEOWNERS`](.github/CODEOWNERS) for the default review owner and [docs/sops/github_branch_protection_checklist.md](docs/sops/github_branch_protection_checklist.md) for the manual GitHub settings that should reinforce the repo operating model.
