# Development Workflow

## Default Flow

1. Plan the change.
2. Implement the smallest coherent slice.
3. Verify behavior and path correctness.
4. Record or update an ADR when the change introduces a durable decision.
5. Update manifests, schemas, and related docs before closing the work.

## Planning Expectations

- Confirm the relevant contracts, schemas, and guardrails before editing.
- Break structural changes apart from content or behavior changes when possible.
- Prefer explicit move lists and before/after state summaries for large restructures.

## Verification Expectations

- Validate structured files such as YAML and JSON.
- Check links and references after directory or file moves.
- Use repo-level tests or examples when they exist; add them when a new pattern needs proof.

## Decision Recording

- Use `docs/decisions/` for durable project decisions.
- Keep ADRs short, factual, and tied to a concrete repo change.

## Manifest Maintenance

- Add or update manifests when introducing new workflows, adapters, or examples.
- Keep schemas aligned with the manifests they govern.
