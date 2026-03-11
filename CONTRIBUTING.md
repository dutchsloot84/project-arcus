# Contributing To Project Arcus

Project Arcus uses the repository root as its operating system. Contributions should strengthen the contracts, workflows, schemas, and documented context that guide future implementation.

## Before You Change Anything

1. Read `docs/project_context.md`.
2. Read `docs/guardrails.md`.
3. Read `agents/coding_agent_contract.md`.
4. Read `workflows/development_workflow.md`.
5. Review relevant ADRs in `docs/decisions/`.

## Default Contribution Pattern

1. Plan the change.
2. Update contracts or schemas first when the change affects structure or policy.
3. Implement the smallest coherent slice.
4. Verify the change locally.
5. Record the decision in an ADR when the change is durable.
6. Update manifests, examples, and docs before closing the work.

## Legacy Boundary

- `legacy/poc/` is archived.
- Do not modify `legacy/poc/` unless the task explicitly calls for a legacy change.
- If you need something from the POC in active work, migrate it intentionally and document the decision.

## Commit Expectations

- Keep commits small and reviewable.
- Separate file moves from policy or content changes when possible.
- Prefer explicit commit messages that describe the repo-level effect.

## Validation Expectations

- Validate YAML and JSON after editing them.
- Check for stale links or outdated path references after moves.
- Run the smallest relevant verification step that proves the change is coherent.

## Ownership

See `.github/CODEOWNERS` for the default review owner.
