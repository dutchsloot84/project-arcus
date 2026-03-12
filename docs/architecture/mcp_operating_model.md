# MCP Operating Model

This page defines how Project Arcus will use Model Context Protocol (MCP) as a governed interaction layer for agents. It complements the Phase 0 baseline in [architecture_at_a_glance.md](architecture_at_a_glance.md), [trust_boundaries.md](trust_boundaries.md), and [ADR-0004-mcp-as-control-plane.md](../decisions/ADR-0004-mcp-as-control-plane.md).

## Purpose Of MCP In Arcus

Arcus will use MCP as a control plane between agents and project resources. Its purpose is to expose approved, scoped capabilities for reading context, requesting constrained mutations, and eventually triggering validated workflows without giving agents broad raw access by default.

MCP is not the Arcus business architecture itself. The business architecture remains the Synthetic Data Hub, its contracts, adapters, trust boundaries, and delivery workflows. MCP exists to mediate how agents interact with those assets.

## Why MCP Is Being Adopted Now

Phase 0 already establishes strong governance requirements around canonical ownership, deterministic behavior, review, and auditability. Introducing MCP now lets Arcus define the control model before implementation work creates accidental broad access patterns.

Adopting the operating model now helps Arcus:

- turn policy into permissioned interfaces instead of relying on prompts alone
- keep the repo and core docs as the source of truth while agent usage expands
- define mutation boundaries before any MCP server or tool implementation begins
- avoid one-off integrations that bypass review, validation, or audit expectations

## Problems MCP Solves

MCP is intended to solve a narrow set of governance and operating problems:

- uncontrolled context loading that pulls in more repo or external content than a task needs
- broad file or service access that makes least-privilege enforcement hard
- inconsistent mutation behavior across docs, contracts, prompts, and workflow assets
- hidden coupling between agent prompts and sensitive repository or enterprise operations
- missing audit expectations for future integrations with systems such as GitHub, Jira, Confluence, or Postgres

## How MCP Fits Into The Existing Arcus Architecture

Arcus remains a repo-first operating system with root-level docs, ADRs, schemas, and workflows defining active truth. Confluence remains an ingestion source, not an active authority. Within that model, MCP sits above the repo and future enterprise integrations as a permissioned interaction layer for agents.

The expected relationship is:

1. repo artifacts define policy, contracts, and allowed operating boundaries
2. MCP capabilities implement those boundaries as explicit interfaces
3. agents use those interfaces instead of assuming direct access to every underlying file, service, or system

When an approved MCP path exists for a resource, agents should use that path instead of raw repo, filesystem, or service access.

## Access Modes

Arcus distinguishes three MCP access modes:

| Access Mode | What It Covers | Expected Controls |
| --- | --- | --- |
| Read-only context access | Retrieve relevant docs, contracts, run metadata, and other approved context | scoped reads, minimal context loading, provenance, no mutation side effects |
| Validated mutation access | Propose or apply bounded updates to docs, contracts, prompts, or metadata | input validation, path scoping, policy checks, audit trail, rollback-aware review points |
| Execution access | Trigger approved workflows or external actions | identity checks, explicit arguments, environment gating, observable run records, human approval where required |

## Control Principles

- Principle of least privilege: every MCP capability should expose the smallest read, write, or execution surface needed for the job.
- Progressive disclosure: agents should load the minimum context needed to complete the current task instead of bulk-reading the repo or external systems.
- Repo-first truth: MCP capabilities should resolve back to repo-defined sources of truth rather than create a competing policy layer.
- Default bounded writes: mutation paths should be narrow, validated, and easy to audit.
- Interface over prompting: policy should be enforced by the interface contract and permission model, not by prompt wording alone.
- Approved path preference: raw repo files, services, or external systems should not be agent-accessed directly when an approved MCP path exists.

## Initial MCP Capability Map

| Capability Area | Initial Role In Arcus | Near-Term Notes |
| --- | --- | --- |
| Context retrieval | Read repo-approved docs, ADRs, schemas, and operating artifacts with provenance | Start with narrow repo context and source-of-truth discovery before broader search |
| Policy enforcement | Enforce scope rules, blocked paths, write levels, and required approvals | Must reflect [mcp_trust_boundaries.md](mcp_trust_boundaries.md) and [mcp_change_control.md](../sops/mcp_change_control.md) |
| Repo operations | Support constrained reads, diffs, and eventually validated updates to approved paths | No broad unvalidated writes; legacy archives remain frozen |
| Future integrations | Add permissioned interfaces for Confluence, Jira, GitHub, Postgres, and similar systems | External integrations are deferred until scope, validation, and audit expectations are explicit |

## Phase 0 Position

In Phase 0 and early Phase 1, MCP is a governance and operating-model decision, not an implementation rollout. Arcus is defining the control plane first so later MCP tools can be introduced with clear trust boundaries, change control, and approval expectations.
