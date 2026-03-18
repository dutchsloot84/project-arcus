# Open Decision Register

Track unresolved questions here so leadership and stakeholders can answer them quickly once Project Arcus is officially directed. This register records uncertainty; it does not grant approval or commit scope.

Related packet:

- [Pre-Kickoff Readiness Matrix](pre_kickoff_readiness_matrix.md)
- [Approval Gate Template](approval_gate_template.md)
- [Pre-Approval Workstreams](../roadmap/pre_approval_workstreams.md)
- [Jira Mapping Draft](../integrations/jira_mapping_draft.md)

## Status Values

- `awaiting official input`
- `recommended default prepared`
- `resolved and ready to propagate`

## Decision Register

| ID | Decision / Question | Category | Why It Matters | Dependency | Owner Role Placeholder | Needed By | Recommended Default | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ODR-001 | What exact kickoff scope is approved for the first execution window? | Scope | Determines what can move from preparation into canonical planning | Leadership approval | Executive sponsor (TBD) | Before first canonical backlog task creation | Keep scope limited to the current pilot baseline unless expanded explicitly | awaiting official input |
| ODR-002 | Who is accountable for sponsor, delivery, platform, and change-review decisions? | Ownership | Work cannot claim approval, signoff, or activation without named roles | Staffing and governance direction | Delivery governance owner (TBD) | Before in-scope execution begins | Use role placeholders only; do not assign individuals yet | awaiting official input |
| ODR-003 | Which environments are officially in scope for the initial slice? | Environment | Affects testing, replay expectations, and rollout readiness | Environment and platform input | Platform owner (TBD) | Before environment-dependent execution tasks | Assume 1-2 lower environments only, per current pilot baseline | awaiting official input |
| ODR-004 | What enterprise security/compliance review tier applies to Arcus work? | Security / Compliance | Determines gate strength, evidence, and approval path | Enterprise governance input | Security reviewer (TBD) | Before sensitive integration or mutation work | Use existing least-privilege and non-production principles as baseline only | awaiting official input |
| ODR-005 | What approval path is required for canonical model, policy-gate, and integration changes? | Governance | Defines signoff points and prevents ad hoc approval behavior | Governance process definition | Change review lead (TBD) | Before the first material implementation ADR after kickoff | Require explicit human review for boundary-changing work | recommended default prepared |
| ODR-006 | What Jira project/workflow/field model should represent repo-native planning? | Tooling / Migration | Avoids rework when migrating or mirroring planning state | Jira administration input | Jira admin / PMO contact (TBD) | Before Jira migration begins | Repo `planning/` stays canonical; Jira starts as a downstream projection | recommended default prepared |
| ODR-007 | What success metrics and pilot exit criteria will leadership judge? | Metrics | Determines what evidence is worth collecting now | Sponsor and delivery alignment | Executive sponsor (TBD) | Before pilot acceptance planning | Measure readiness by determinism, governance, and speed-to-start until targets are defined | awaiting official input |
| ODR-008 | What staffing capacity exists by role for the first approved slice? | Staffing | Affects sequencing, task batching, and ownership assumptions | Resource planning | Delivery manager (TBD) | Before converting provisional workstreams into dated plans | Keep sequencing dependency-driven, not person-driven | awaiting official input |
| ODR-009 | What budget and provider constraints apply to planner integrations? | Budget / Provider | Impacts provider selection, approval gates, and backlog ordering | Architecture and budget direction | Platform owner (TBD) | Before provider-specific integration work | Keep provider choices documented as options, not commitments | awaiting official input |
| ODR-010 | What retrieval scope and policy-gate rules are acceptable for planner flows? | Architecture / Policy | Directly affects control-plane design and validation rules | Architecture and security decisions | Architecture owner (TBD) | Before advanced orchestration implementation | Start with minimal approved repo context and hard-stop validation failures | recommended default prepared |
| ODR-011 | What evidence pack is required before a pilot can be treated as operationally valid? | Rollout / Pilot | Drives demo strategy, verification work, and approval gates | Sponsor and operational stakeholders | Delivery lead (TBD) | Before pilot readiness review | Require manifests, replay evidence, and signoff artifacts | awaiting official input |
| ODR-012 | What official process issues new task IDs for canonical `planning/` files? | Planning control plane | Prevents accidental task creation that breaks repo planning rules | Planning governance direction | Planning owner (TBD) | Before first new canonical task is added | Prepare task content outside `planning/` until IDs are issued | recommended default prepared |

## Maintenance Rule

When an item resolves:

1. Update its status here.
2. Propagate the decision to the right source-of-truth artifact such as an ADR, SOP, roadmap doc, or canonical planning task.
3. Remove obsolete placeholder language from related readiness docs.
