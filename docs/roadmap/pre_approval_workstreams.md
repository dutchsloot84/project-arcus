# Pre-Approval Workstreams

This document groups the highest-leverage planning work that can be prepared before Project Arcus receives official execution approval. These workstreams are not commitments, dates, or in-scope tasks. They are preparation lanes only.

Related packet:

- [Pre-Kickoff Readiness Matrix](../governance/pre_kickoff_readiness_matrix.md)
- [Open Decision Register](../governance/open_decision_register.md)
- [Approval Gate Template](../governance/approval_gate_template.md)
- [ADR Backlog](../decisions/adr_backlog.md)

## Workstream Rules

- Keep outputs outside canonical execution scope until official approval exists.
- Favor durable scaffolding over speculative design detail.
- Record assumptions explicitly rather than filling gaps with invented approvals.
- Treat any future repo-native planning control plane as a deliberate follow-on decision, not a current branch fact.

## Workstream 1: Readiness Packet

**Goal:** Prepare the governance and planning packet needed to start quickly once approval is granted.

**Safe outputs now:**

- readiness matrix
- open decision register
- approval gate template
- task-preparation template

**Depends on:** current repo truth only

**Waits for:** none

## Workstream 2: Canonical Planning Readiness

**Goal:** Ensure the team can convert approved work into a canonical planning method with minimal delay.

**Safe outputs now:**

- non-canonical task briefs prepared outside execution-tracking surfaces
- readiness criteria for backlog versus in-scope moves
- dependency language and evidence expectations

**Depends on:** current workflow and repo operating model

**Waits for:** official task ID policy, approved scope, and any explicit repo-native planning decision

## Workstream 3: Governance And Signoff Design

**Goal:** Define how decisions and approval points will be recorded once official governance is named.

**Safe outputs now:**

- placeholder gate types
- evidence requirements
- signoff record shape
- escalation questions queued in the decision register

**Depends on:** current guardrails and trust boundaries

**Waits for:** named approvers, severity thresholds, enterprise review path

## Workstream 4: Jira Migration Readiness

**Goal:** Reduce future migration friction between repo-native truth and enterprise tooling.

**Safe outputs now:**

- draft mapping between repo planning concepts and likely Jira concepts
- assumptions about one-way versus two-way flow
- list of decisions that must precede Jira enablement

**Depends on:** current repo operating model

**Waits for:** Jira project, workflow, fields, governance policy, and any formal planning-control-plane decision

## Workstream 5: ADR Readiness

**Goal:** Queue the high-value architectural or governance decisions that are likely to arise immediately after kickoff.

**Safe outputs now:**

- ADR topic backlog
- trigger conditions
- consequence framing

**Depends on:** current ADR set and architecture docs

**Waits for:** approved implementation slice and stakeholder choices

## Workstream 6: Pilot Readiness Framing

**Goal:** Prepare the minimum framing for pilot evidence and rollout discussion without committing to rollout details.

**Safe outputs now:**

- candidate evidence categories
- pilot-readiness questions
- placeholder review gates

**Depends on:** current pilot baseline and non-production boundaries

**Waits for:** success metrics, environments, rollout sequence, and operational owners

## Dependency Order

1. Readiness Packet
2. Canonical Planning Readiness
3. Governance And Signoff Design
4. Jira Migration Readiness
5. ADR Readiness
6. Pilot Readiness Framing

This order is intended to maximize speed-to-start while minimizing rework if leadership narrows or redirects the first approved slice.
