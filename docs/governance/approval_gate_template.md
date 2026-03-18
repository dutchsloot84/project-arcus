# Approval Gate Template

Use this template to prepare review points before official kickoff without assuming named approvers, dates, or approved scope. It defines the gate structure and required evidence only.

Related packet:

- [Pre-Kickoff Readiness Matrix](pre_kickoff_readiness_matrix.md)
- [Open Decision Register](open_decision_register.md)
- [Pre-Approval Workstreams](../roadmap/pre_approval_workstreams.md)

## Gate Design Rules

- A gate may be prepared before approval, but it is not active until official governance confirms it.
- Approver fields must remain `TBD by official governance` until named by leadership or the change-review body.
- A gate should describe evidence, decision location, and outcomes clearly enough that Jira or enterprise governance can mirror it later.

## Standard Gate Fields

| Field | What To Record |
| --- | --- |
| Gate name | Short, stable label |
| Trigger | What kind of work or decision causes this gate to apply |
| Purpose | Why the gate exists |
| Scope | What artifacts, changes, or decisions it covers |
| Required evidence | The minimum packet needed for review |
| Decision record location | Where the authoritative outcome will be recorded |
| Approver role placeholder | `TBD by official governance` until confirmed |
| Preconditions | What must already be true before review can happen |
| Outcome states | `approved`, `approved with conditions`, `deferred`, `rejected` |
| Downstream action | What happens after each outcome |

## Gate Template

### Gate Name

`TBD gate name`

### Trigger

`Describe the event or change that requires review.`

### Purpose

`Describe the governance or delivery risk this gate is meant to control.`

### Scope

`List the artifacts, boundaries, or decisions this gate applies to.`

### Required Evidence

- `Relevant source-of-truth docs`
- `Decision summary or change summary`
- `Validation evidence`
- `Dependency or impact summary`
- `Open questions, if any`

### Decision Record Location

`TBD: ADR / SOP / canonical planning task / Jira projection / leadership record`

### Approver Role Placeholder

`TBD by official governance`

### Preconditions

- `Scope is stated without ambiguity`
- `Dependencies are visible`
- `Required evidence is attached or linked`
- `Open questions are either resolved or explicitly escalated`

### Outcome States

| Outcome | Meaning | Required Follow-Up |
| --- | --- | --- |
| approved | Work may proceed within the reviewed boundary | Record approval and continue |
| approved with conditions | Work may proceed only if listed conditions are satisfied | Track conditions explicitly before execution |
| deferred | Decision is postponed pending more information | Record blockers and return with updated evidence |
| rejected | Work must not proceed in its current form | Record why and what must change before resubmission |

## Candidate Gate Types To Prepare Now

These are safe placeholders, not active approvals:

- kickoff scope confirmation
- canonical change review
- policy or trust-boundary change review
- integration enablement review
- pilot readiness review
- Jira migration readiness review
