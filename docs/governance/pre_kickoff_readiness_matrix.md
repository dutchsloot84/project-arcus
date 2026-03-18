# Pre-Kickoff Readiness Matrix

This document separates what Project Arcus can responsibly finalize now from what should remain scaffolded or deferred until official approval. It is part of the pre-kickoff readiness packet and should be read alongside:

- [Open Decision Register](open_decision_register.md)
- [Approval Gate Template](approval_gate_template.md)
- [Pre-Approval Workstreams](../roadmap/pre_approval_workstreams.md)
- [ADR Backlog](../decisions/adr_backlog.md)
- [Jira Mapping Draft](../integrations/jira_mapping_draft.md)
- [Task Preparation Template](../../examples/planning/task_preparation_template.md)

## Operating Rule

Arcus may prepare non-canonical planning aids before approval, but pre-kickoff artifacts must remain honest about current repo truth on fresh `main`:

- repo artifacts remain the source of truth for active policy and workflow
- pre-kickoff readiness artifacts must not imply approved scope, funding, staffing, or execution commitment
- any future repo-native planning control plane should be adopted explicitly rather than assumed into existence

## Readiness Matrix

| Category | Readiness Label | Safe To Finalize Now | Must Stay Placeholder Or Await Official Input | Current Repo Truth |
| --- | --- | --- | --- | --- |
| Repo structure | Can finalize now | Root repo OS, active-vs-legacy boundary, and source-of-truth hierarchy | None beyond later maintenance | [README.md](../../README.md), [ADR-0002](../decisions/ADR-0002-phase-0-operating-model.md) |
| Planning system | Can scaffold now, finalize later | Pre-kickoff planning packet, draft task-preparation shape, and migration-ready governance notes | Formal adoption of a canonical repo-native planning control plane and official task ID process | [README.md](../../README.md), [Development Workflow](../../workflows/development_workflow.md), [Phase Plan](../roadmap/phase_plan.md) |
| Task taxonomy / IDs | Can scaffold now, finalize later | Draft task-preparation shape, readiness gates, dependency language | Official ID issuance policy and Jira key policy | [Task Preparation Template](../../examples/planning/task_preparation_template.md) |
| Phase definitions | Can scaffold now, finalize later | Phase 0 baseline and provisional workstream groupings | Later phase commitments, dates, and entry criteria | [Phase Plan](../roadmap/phase_plan.md), [Pre-Approval Workstreams](../roadmap/pre_approval_workstreams.md) |
| Architecture scaffolding | Can scaffold now, finalize later | Pilot boundaries, deterministic flow, trust boundaries, control-plane framing | Deeper implementation decomposition tied to approved scope | [Project Context](../project_context.md), [ADR-0003](../decisions/ADR-0003-phase-0-architecture-baseline.md), [Trust Boundaries](../architecture/trust_boundaries.md) |
| ADR inventory | Can scaffold now, finalize later | Future ADR topic backlog and trigger conditions | ADR outcomes and approval dates | [ADR Backlog](../decisions/adr_backlog.md) |
| Control plane / execution plane boundaries | Can finalize now | Repo-first truth, MCP-as-control-plane, planner-vs-generator separation | Concrete MCP implementation rollout | [ADR-0004](../decisions/ADR-0004-mcp-as-control-plane.md), [MCP Operating Model](../architecture/mcp_operating_model.md) |
| Governance / human signoff points | Can scaffold now, finalize later | Gate types, evidence model, and placeholder approval points | Named approvers, thresholds, and approval SLAs | [Approval Gate Template](approval_gate_template.md), [MCP Change Control](../sops/mcp_change_control.md) |
| Coding standards | Can finalize now | Plan-first, contract-first, schema-first, no-drift rules | Team-specific exceptions, if any | [Guardrails](../guardrails.md), [Contributing](../../CONTRIBUTING.md) |
| Testing strategy | Can scaffold now, finalize later | Determinism, replayability, contract validation, and minimal proof expectations | Coverage targets, environment commitments, and signoff owners | [Project Context](../project_context.md), [Arcus Execution Checklist](../implementation/arcus_execution_checklist.md) |
| Demo strategy | Can scaffold now, finalize later | Placeholder evidence packet and demo objectives | Audience, script, and go/no-go expectations | [Approval Gate Template](approval_gate_template.md) |
| Integration assumptions | Can scaffold now, finalize later | Boundary assumptions for Jira, Confluence, GitHub, and future integrations | Actual system access, workflows, and ownership | [Jira Mapping Draft](../integrations/jira_mapping_draft.md), [MCP Operating Model](../architecture/mcp_operating_model.md) |
| Security / compliance assumptions | Can scaffold now, finalize later | Non-production-only, least privilege, validation, and auditability principles | Enterprise control interpretation and formal signoff | [Guardrails](../guardrails.md), [MCP Trust Boundaries](../architecture/mcp_trust_boundaries.md) |
| Jira migration readiness | Can scaffold now, finalize later | Repo-to-Jira concept crosswalk and migration assumptions | Jira project configuration and automation behavior | [Jira Mapping Draft](../integrations/jira_mapping_draft.md) |
| Stakeholder decision log | Can finalize now | Decision-register format and review-ready question framing | Actual decisions and owners | [Open Decision Register](open_decision_register.md) |
| Success metrics | Can scaffold now, finalize later | Metric families and evidence categories | Targets, baselines, and thresholds | [Open Decision Register](open_decision_register.md) |
| Staffing / ownership assumptions | Must wait | Role placeholders only | Named people, capacity, and accountability assignments | [Trust Boundaries](../architecture/trust_boundaries.md), [Open Decision Register](open_decision_register.md) |
| Rollout / pilot assumptions | Can scaffold now, finalize later | Pilot envelope, prerequisite evidence, and readiness gates | Dates, rollout sequence, and operational commitments | [ADR-0003](../decisions/ADR-0003-phase-0-architecture-baseline.md), [Approval Gate Template](approval_gate_template.md) |

## Use This Matrix

- Treat `Can finalize now` items as durable repo guidance that may be created or refined immediately.
- Treat `Can scaffold now, finalize later` items as placeholders that should stay explicitly provisional.
- Treat `Must wait` items as leadership or stakeholder decisions that should be recorded, not assumed.
