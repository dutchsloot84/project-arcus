# MCP Trust Boundaries

This page defines the trust boundaries for MCP-mediated agent interactions in Project Arcus. It extends the baseline trust model in [trust_boundaries.md](trust_boundaries.md) and should be applied alongside [mcp_operating_model.md](mcp_operating_model.md) and [mcp_change_control.md](../sops/mcp_change_control.md).

## MCP Interaction Boundary

MCP is the permissioned layer between agents and governed project resources. The boundary clarifies what agents can observe, what they may ask for, what the MCP server may allow or deny, and where human review stays mandatory.

### What The Agent Can See

- repo-approved source-of-truth artifacts exposed for the current task
- explicitly granted schemas, contracts, prompts, workflow definitions, and supporting metadata
- limited external context only when an approved MCP capability exposes it

Agents do not automatically see all repository content, archived material, secrets, runtime environments, or external enterprise systems.

### What The Agent Can Request

- read-only context retrieval for relevant in-scope artifacts
- bounded mutations to approved files or resources when a permissioned mutation capability exists
- execution of approved workflows when an execution capability exists and the requested action is in scope

Requests do not imply entitlement. Every request remains subject to interface policy, validation, and approval rules.

### What The MCP Server Can Allow Or Deny

The MCP server is allowed to:

- allow requests that match the approved capability contract, trust boundary, and write-severity rules
- deny requests that exceed scope, target frozen or sensitive areas, fail validation, or lack required approval
- reduce returned context to the minimum necessary for the task
- require structured inputs instead of free-form broad actions

### What Requires Explicit Human Approval

Explicit human approval is required for:

- sensitive mutations with material policy, contract, schema, workflow, or implementation impact
- new MCP capabilities or scope expansion into new resource classes or enterprise systems
- execution actions with operational side effects beyond approved low-risk automation
- any request that crosses from documentation-only changes into broader workflow or implementation change

## Default Deny Posture

- Sensitive mutations are deny-by-default until their scope, validation path, and audit expectations are defined.
- `legacy/poc/` is explicitly frozen and denied for mutation by default.
- Archived, external, or sensitive resources are unavailable unless an approved interface grants access.
- If policy is unclear, the safe outcome is deny or escalate for review rather than infer permission.

## Trust Domains

| Trust Domain | What It Contains | MCP Default Posture |
| --- | --- | --- |
| Repo source-of-truth docs | `docs/`, approved root guidance, durable repo policy | readable when relevant; writes limited by severity and scope |
| Schemas / contracts | `schemas/`, versioned contracts, structured validation rules | readable when relevant; mutations require stronger validation and review |
| Executable workflows | workflow definitions, automation entrypoints, implementation-affecting control artifacts | restricted; higher write severity and likely approval requirements |
| Archived legacy content | `legacy/poc/` and similar archived material | frozen and excluded by default |
| External enterprise systems | Confluence, Jira, GitHub, Postgres, and future integrations | unavailable unless a specific approved MCP capability exposes them |

## Write-Severity Ladder

| Level | Change Type | Agent-Only Allowed | Validation Required | Human Approval Required |
| --- | --- | --- | --- | --- |
| Level 0 | Read-only context access | Yes | provenance and scope checks | No |
| Level 1 | Documentation updates | Yes, within approved paths | link/path checks and repo policy alignment | Not by default, but required if the change alters project policy materially |
| Level 2 | Schema / prompt / contract changes | No | structured validation and companion artifact review | Yes |
| Level 3 | Workflow / execution / implementation changes | No | structured validation plus execution or behavior review | Yes |

## Practical Enforcement Notes

- Agents may operate directly only at Level 0 and limited Level 1 documentation paths that are already in scope for the task.
- Level 2 and Level 3 changes require a validation path that proves the interface, contract, and companion artifacts stay aligned.
- When an approved MCP interface exists, it should encode path scoping, write level, and approval expectations rather than leaving those decisions to prompt text.
- External-system mutations should be treated at least as Level 2, and often Level 3, until a narrower policy is documented.
