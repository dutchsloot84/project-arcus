# ADR Backlog

This backlog lists likely future ADR topics that can be prepared before kickoff without pre-deciding outcomes. Use it to reduce startup latency after approval, then turn items into real ADRs only when the triggering decision is active.

Related packet:

- [Pre-Kickoff Readiness Matrix](../governance/pre_kickoff_readiness_matrix.md)
- [Open Decision Register](../governance/open_decision_register.md)
- [Pre-Approval Workstreams](../roadmap/pre_approval_workstreams.md)

## Backlog Rules

- Do not treat this file as a decision record.
- Do not assign approval dates or named approvers here.
- Promote an item into a real ADR only when a decision is live and evidence exists.

## Candidate ADR Topics

| Topic | Trigger Condition | What The ADR Would Settle | Why It Is Safe To Queue Now |
| --- | --- | --- | --- |
| Official task ID issuance model | The first new canonical task needs to be created | How Arcus receives and validates stable task IDs | The need is clear even though the chosen mechanism is not |
| Repo-to-Jira authority boundary | Jira migration or dual-tracking becomes active | Whether Jira is a mirror, a projection target, or a shared control surface | The migration question is foreseeable even without Jira approval |
| Approval severity tiers | Governance asks for different gate strengths | Which changes require what level of review and evidence | Current docs already require approval boundaries, but not the tier model |
| Pilot readiness evidence pack | Leadership wants a go/no-go review | What evidence is required before a pilot is treated as ready | Current pilot baseline exists, but acceptance evidence is still open |
| Provider selection boundary | Provider-specific planner work enters scope | Which provider families are allowed and under what constraints | Provider choice is unresolved but likely material |
| Retrieval scope policy | Retrieval-backed planning is proposed | What repo or enterprise context planners may access and how it is audited | Current architecture leaves this intentionally open |
| Environment scope and drift ownership | Pilot environments are formally selected | Which environments are in scope and who owns drift remediation | Current docs name lower environments only at a high level |
| Canonical change approval workflow | Implementation starts changing canonical contracts or generator boundaries | Which reviews, records, and approvals are mandatory | Trust-boundary docs already imply the need for formal review |
| Integration enablement policy | Jira, Confluence, GitHub, or Postgres integration work is approved | How external integrations get approved, validated, and audited | MCP docs already defer these integrations pending explicit contracts |

## Promotion Checklist

Before converting a backlog item into an ADR:

1. Confirm the decision is active, not hypothetical.
2. Link the triggering work or approval.
3. State the alternatives under real consideration.
4. Capture the consequences for repo policy, workflow, or architecture.
