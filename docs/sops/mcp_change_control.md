# MCP Change Control

Use this SOP when introducing or modifying MCP-related architecture, contracts, tools, or permissions in Project Arcus.

## Purpose

Arcus adopts MCP as a governed control-plane pattern, not as an unbounded integration surface. No MCP mutation capability should be introduced without clear scope, validation expectations, and audit expectations.

## When An ADR Is Required

Create or update an ADR under [docs/decisions/](../decisions/) when a change:

- adds a new MCP capability class such as read, mutation, execution, or external-system integration
- changes trust boundaries, approval expectations, or write-severity interpretation
- expands MCP into a new trust domain or enterprise system
- changes repo policy for how agents are expected to access governed resources

Minor wording improvements inside an already accepted MCP document do not need a new ADR if they do not change policy.

## When Schema Changes Are Required

Add or update schemas or other structured contracts when a change:

- introduces a structured MCP request or response shape
- adds validation rules for mutations, approvals, or audit metadata
- changes machine-consumable prompt, contract, or workflow inputs that an MCP tool will depend on

If the change alters structured behavior, schema-first still applies.

## When New MCP Tools Or Capabilities Require Approval

Explicit approval is required before merge when the proposed change:

- introduces a new MCP tool, endpoint, or resource type
- adds mutation capability for repo files, metadata, or external systems
- introduces execution capability with operational side effects
- widens access to archived, sensitive, or external resources
- changes a capability from read-only to mutation or execution

## How To Classify The Change

Use the write-severity ladder in [docs/architecture/mcp_trust_boundaries.md](../architecture/mcp_trust_boundaries.md):

- Level 0: read-only context access
- Level 1: documentation updates
- Level 2: schema / prompt / contract changes
- Level 3: workflow / execution / implementation changes

Classify the change by the highest-severity artifact or side effect it introduces, not by the author's intent.

## Required Documentation Updates

Update the smallest coherent set of artifacts needed to keep policy aligned:

- [docs/architecture/mcp_operating_model.md](../architecture/mcp_operating_model.md) for operating-model changes
- [docs/architecture/mcp_trust_boundaries.md](../architecture/mcp_trust_boundaries.md) for trust, scope, or write-level changes
- [docs/project_context.md](../project_context.md) when the repo-wide control model changes
- [docs/guardrails.md](../guardrails.md) when contributor rules or blocked paths change
- [agents/coding_agent_contract.md](../../agents/coding_agent_contract.md) when agent behavior expectations change
- relevant ADRs, schemas, prompts, or workflow docs when the change affects them

## Required Validation Before Merge

Before merge:

1. confirm the change is classified against the write-severity ladder
2. confirm blocked paths such as `legacy/poc/` remain untouched unless explicitly authorized
3. confirm all affected docs, ADRs, contracts, and schemas remain aligned
4. confirm Markdown links and file references resolve sensibly
5. confirm new mutation or execution capabilities have explicit validation and audit expectations
6. confirm human-approval requirements are documented where the boundary demands them

## Merge Gate For Mutation Capability

Do not merge a new MCP mutation capability unless it has:

- a clearly defined scope and allowed resource boundary
- validation rules for the requested mutation
- documented approval expectations
- an audit expectation for what should be recorded
- a companion documentation update that explains why the capability is allowed

## Current Phase Constraint

In Phase 0 and early Phase 1, Arcus should prefer governance-first MCP changes: control model, trust boundaries, contracts, and SOPs before tool implementation. If a proposed change starts to imply server behavior, execution design, or enterprise rollout, stop and document the boundary first.
