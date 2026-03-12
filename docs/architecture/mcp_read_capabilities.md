# MCP Read Capabilities

This document defines the initial portable read-only capability contracts for Arcus MCP adoption. These contracts are intentionally infrastructure-agnostic and should survive moves between local, hosted, or AWS-backed execution environments.

Use this document with [mcp_operating_model.md](mcp_operating_model.md), [mcp_trust_boundaries.md](mcp_trust_boundaries.md), and [mcp_change_control.md](../sops/mcp_change_control.md).

## Shared Read Controls

All read capabilities in this document share these controls:

- least privilege: return the minimum context needed for the current task
- repo-first truth: prefer repo-defined docs, schemas, workflows, and ADRs over secondary sources
- blocked-path support: allow callers or server policy to exclude archived, sensitive, or irrelevant paths
- explicit provenance: every returned item should include its source path or source system
- no mutation side effects: these capabilities do not edit files, change state, or trigger workflows
- no bulk loading by default: broad recursive retrieval should require an explicit request and still be narrowed by policy

## Repo Source-Of-Truth Discovery

### Purpose

Return the smallest set of governing files that should anchor the current task.

### Typical Inputs

- task summary or user intent
- optional path hints
- optional blocked paths
- optional category filters such as `docs`, `schemas`, `workflows`, `adr`, `agent-guidance`, or `readme`

### Expected Response

- selected files with:
  - path
  - category
  - why selected
  - provenance
- skipped or denied paths when policy excludes likely matches
- a short note when no clear source-of-truth artifact can be identified

### Control Notes

- Prefer canonical files over nearby duplicates or convenience summaries.
- Avoid recursive repo sweeps unless the task genuinely needs discovery.
- Exclude archived or frozen paths by default unless the task explicitly authorizes them.

## Repo Context Retrieval

### Purpose

Fetch only the in-scope repository files needed for the current task after discovery or explicit user direction.

### Typical Inputs

- explicit file paths, or approved category filters
- task summary for relevance narrowing
- optional blocked paths
- optional retrieval limit such as a maximum file count

### Expected Response

- retrieved files with:
  - path
  - contents
  - why included
  - provenance
- omitted files with a short reason when the request was narrowed by policy or scope

### Control Notes

- Retrieval should be path-allowlisted or category-scoped rather than open-ended.
- Return only the files required to complete the current task.
- If a request implies broad repo access, narrow it first through source-of-truth discovery.

## GitHub Read

### Purpose

Inspect GitHub metadata for the current repository without granting write capability.

### Typical Inputs

- repository identifier
- resource type such as pull request, issue, checks, branch status, or review state
- optional identifiers or filters such as branch name, PR number, label, or state

### Expected Response

- normalized metadata for the requested resource
- source attribution showing the data came from GitHub
- enough identifiers for a user or later tool to continue the workflow

### Control Notes

- No write operations, merge actions, comment creation, or label changes are in scope.
- Do not assume hidden credentials or undisclosed repo access.
- Keep the response tied to the requested repo and resource only.
