# ADR-0004: MCP As Control Plane

- Status: Accepted
- Date: 2026-03-12

## Context

Project Arcus now has a documented Phase 0 architecture baseline, trust boundaries, and repo operating model. That baseline emphasizes deterministic behavior, strong governance, narrow pilot scope, and clear separation between source-of-truth artifacts and consumers.

As agent-assisted work expands, prompt-only guardrails are not enough to preserve those boundaries. The repo needs an explicit decision about how agents should interact with project resources before any MCP server or tool implementation begins.

## Decision

Arcus will treat MCP as a control-plane pattern for agent interaction.

- Policy will be enforced by permissioned interfaces, not by prompts alone.
- MCP adoption starts with architecture and governance definition first.
- Implementation is deferred until contracts, trust boundaries, and change control are defined.
- When an approved MCP path exists, agents should prefer that permissioned interface over broad raw access to files, services, or external systems.

## Consequences

- Arcus gets a durable governance model for future agent access before implementation expands.
- MCP becomes an enforcement layer for least privilege, scoped reads, validated mutations, and approval boundaries.
- Repo artifacts remain the source of truth, while Confluence and other enterprise systems stay ingestion or integration sources rather than policy authorities.
- Future MCP implementation work now requires companion contracts, trust-boundary definitions, and change-control artifacts rather than ad hoc tool growth.

## Alternatives Considered

### Direct File / Tool Access By Agents

This would move faster initially, but it makes least-privilege enforcement, validation, and audit expectations too implicit for Arcus's governance needs.

### Prompt-Only Guardrails Without MCP Mediation

This keeps the system simple on paper, but it relies on contributor discipline rather than permissioned interfaces and leaves too much room for inconsistent behavior.

### Building Custom One-Off Integrations First

This could solve immediate needs for individual systems, but it would create fragmented controls before Arcus has a shared control-plane model.

## What Is Explicitly In Scope Now

- defining MCP as the governed control-plane pattern for agent interaction
- documenting operating-model expectations, trust boundaries, and change-control rules
- aligning repo guardrails and agent expectations with that model
- preparing for future read-only, validated-mutation, and execution capabilities without implementing them yet

## What Is Explicitly Not In Scope Yet

- implementing MCP servers, tools, or external integrations
- granting broad new mutation access to the repo or enterprise systems
- defining a large platform architecture beyond what Phase 0 and early Phase 1 require
- replacing the repo source-of-truth model with an MCP-managed policy source
