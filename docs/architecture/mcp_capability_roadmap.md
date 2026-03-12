# MCP Capability Roadmap

This roadmap gives a phased view of MCP adoption in Arcus. It is intentionally narrow and should be read with [mcp_operating_model.md](mcp_operating_model.md), [mcp_trust_boundaries.md](mcp_trust_boundaries.md), and [ADR-0004-mcp-as-control-plane.md](../decisions/ADR-0004-mcp-as-control-plane.md).

## Phase 0: Governance + Control Model

- define MCP as the Arcus control-plane pattern for agent interaction
- document trust boundaries, write levels, and change-control rules
- keep repo artifacts as the source of truth and Confluence as an ingestion source
- defer MCP server and tool implementation

## Phase 1: Read-Only Context Tools

- expose narrow MCP capabilities for source-of-truth discovery and scoped context retrieval
- enforce least-privilege reads and minimal context loading
- keep archived, sensitive, and external resources unavailable unless explicitly approved

## Phase 2: Validated Mutation Tools

- add bounded mutation capabilities for approved documentation, metadata, contract, or prompt updates
- require path scoping, structured validation, and audit expectations
- keep broad write access out of scope

## Phase 3: Execution And External Integrations

- introduce tightly scoped execution capabilities for approved workflows
- add enterprise integrations such as Confluence, Jira, GitHub, or Postgres only behind explicit contracts and approvals
- preserve human approval for higher-severity or operationally sensitive actions
