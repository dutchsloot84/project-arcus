# Coding Agent Contract

## Required Reads

Before changing files, read in this order:

1. `docs/project_context.md`
2. `docs/guardrails.md`
3. `agents/coding_agent_contract.md`
4. `agents/agent_registry.yaml`
5. `workflows/development_workflow.md`
6. relevant roadmap items and ADRs

## Change Rules

- Do not touch `legacy/poc/` unless the task explicitly says to work there.
- Prefer root-level contract, schema, workflow, and documentation updates before new implementation work.
- Keep changes deterministic, reviewable, and split into small commits when possible.
- Preserve source-of-truth consistency across docs, schemas, manifests, and workflows.
- If a change affects agent behavior or delivery policy, update this contract or the registry in the same change.

## Output Requirements

- State what changed and why.
- List validation performed and any gaps.
- Call out assumptions if a decision could not be derived from the repo.
- Reference file paths precisely when describing important changes.

## Validation Checklist

- Verify the changed files are the intended source of truth.
- Check for stale references caused by renames or path changes.
- Validate YAML and JSON artifacts after editing them.
- Run the smallest relevant checks that prove the change is coherent.
- Leave the worktree clean, or clearly explain any intentionally preserved local state.
