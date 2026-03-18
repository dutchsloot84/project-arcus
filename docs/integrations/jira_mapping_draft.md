# Jira Mapping Draft

This draft prepares Project Arcus for later Jira migration or mirroring without making Jira authoritative today.

Related packet:

- [Pre-Kickoff Readiness Matrix](../governance/pre_kickoff_readiness_matrix.md)
- [Open Decision Register](../governance/open_decision_register.md)
- [Pre-Approval Workstreams](../roadmap/pre_approval_workstreams.md)

## Canonical Authority Rule

Until leadership explicitly decides otherwise:

- repo-native artifacts remain the source of truth for active policy, workflow, and planning intent
- Jira should be treated as a downstream projection or migration target, not the active source of truth
- if Arcus later formalizes a repo-native planning control plane, Jira should mirror that model rather than replace it

## Mapping Goals

- preserve stable task identity
- preserve readiness semantics
- preserve dependency visibility
- preserve the distinction between `potential`, `committed`, and `completed`
- make later enterprise reporting easier without weakening repo truth

## Draft Concept Mapping

| Repo-Native Arcus Concept | Likely Jira Analog | Draft Mapping Note |
| --- | --- | --- |
| Scoped but not yet committed work | Backlog / To Do issue state | Represents prepared work that is not yet approved for execution |
| Committed but not started work | Selected for delivery / committed but not started | Commitment should be intentional, not automatic |
| Active execution work | In Progress | Should only occur after readiness and approval conditions are met |
| Blocked work | Blocked / On Hold | Blocker reason should stay visible in repo-linked detail |
| Verified complete work | Done | Completion should reflect verified completion, not mere coding completion |
| Definition maturity | Ready / refinement custom field or workflow gate | Distinguish idea shape from executable definition |
| Priority | Jira priority or custom field | Preserve `P0`-`P3` semantics if allowed |
| Priority rationale | Custom text field | Needed when the repo requires justification for high priority |
| Dependencies | Issue links | Preserve exact identity rather than loose prose references |

## Decisions Still Required Before Jira Becomes Active

- Jira project and issue-key policy
- workflow state design
- required custom fields
- sync direction and cadence
- whether Jira mirrors repo tasks or only approved subsets
- approval and audit expectations for Jira-created or Jira-updated records
- whether Arcus formalizes a dedicated repo-native planning control plane first

## Safe Default Until Those Decisions Exist

- continue using repo artifacts as canonical planning truth
- use this document only as a crosswalk draft
- keep any future Jira setup aligned to repo semantics rather than forcing repo semantics to collapse into default Jira workflow language
