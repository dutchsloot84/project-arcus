# Trust Boundaries

This page distills the Phase 0 architecture ingestion artifact at [context/confluence_ingestion/20260311_arcus_phase0_architecture_first_pass.md](../../context/confluence_ingestion/20260311_arcus_phase0_architecture_first_pass.md). Items labeled `Inferred` are synthesis carried forward from that artifact.

## Trust Boundaries

| Boundary | What Is Inside | What Is Outside | Phase 0 Effect |
| --- | --- | --- | --- |
| Execution boundary | AWS IAM-governed generator execution | Broad DevOps or general user access | Only approved generator identities may run canonical generation flows. |
| Control plane boundary | Canonical model, registry metadata, audit logging, manifest references | QA, RapidBotz, CI/CD consumers | Consumers can request datasets but cannot directly mutate canonical definitions. |
| Adapter boundary | Adapter validation and normalization into the canonical contract | Tool-specific request shapes and automation logic | RapidBotz submits requests through an adapter instead of embedding scenario rules or transformations. |
| Environment boundary | Non-production synthetic artifacts and test runs | Production systems and production data stores | The pilot has zero production write paths and a non-production-only blast radius. |
| Registry boundary | Metadata such as scenario ID, git hash, owner, approval state, and artifact pointers | Raw datasets stored as a registry payload | The registry is metadata-only and does not become a second canonical data store. |

## Shared Responsibility Model

| Role | Responsibility |
| --- | --- |
| Synthetic Data Platform owner | Canonical model integrity, generator logic, drift detection, registry governance, auditability, and change review. |
| Adapter owner | Request translation, validation, and mapping between consumer inputs and the canonical scenario contract. |
| Application teams and SMEs | Business-rule accuracy, schema-change communication, and contract updates required by application changes. |
| QA and RapidBotz teams | Dataset requests, test design, and handling test failures without bypassing canonical controls. |
| DevOps | Environment stability and drift outside the synthetic data control plane. |

Scenario activation requires identifiable ownership. If business or technical ownership is missing, the scenario should not be treated as active.

## Mutation Permissions For Canonical Data

- Canonical model changes require formal review by the platform owner and the change review group.
- QA, RapidBotz, CI/CD, and environment-specific workflows may request datasets but may not directly edit canonical definitions.
- Environment-specific overrides are not permitted in the canonical model.
- Dataset variations must be seed-derived rather than manually altered after generation.
- Requested scope expansion triggers review instead of direct mutation.

`Inferred`: The practical control point is a request-only usage plane above a tightly governed canonical control plane, with adapters preserving that separation for each consumer.
