# Architecture At A Glance

This page distills the Phase 0 architecture ingestion artifact at [context/confluence_ingestion/20260311_arcus_phase0_architecture_first_pass.md](../../context/confluence_ingestion/20260311_arcus_phase0_architecture_first_pass.md). Items labeled `Inferred` are synthesis carried forward from that artifact.

## Six-Layer Architecture

Synthetic Data Hub sits beneath the six-layer Test Intelligence stack as the deterministic data foundation.

| Layer | Responsibility |
| --- | --- |
| Foundation: Synthetic Data Hub | Owns the canonical model, planner-to-generator orchestration contracts, seed-based generation, contract validation, manifests, registry metadata, artifact hashing, and audit logging. |
| Layer 1: Unit Testing | Uses deterministic fixtures and scenario outputs to keep low-level validation repeatable. |
| Layer 2: DevOps CI/CD | Requests governed datasets and carries deterministic run inputs through pipeline execution. |
| Layer 3: Performance Tooling | Consumes synthetic datasets for repeatable non-production performance exercises. |
| Layer 4: RapidBotz / API Automation | Requests datasets through adapters and uses them for automation flows. |
| Layer 5: DIRR / AI Test Intelligence | Interprets test outcomes using traceable synthetic data inputs. |
| Layer 6: Release Governance / Risk Visibility | Uses reproducible evidence from the lower layers to support release decisions. |

## Planner To Generator Flow

The active orchestration path is:

`Planner -> ScenarioSpec -> Policy Gate -> Deterministic Generator`

- Planner providers may propose `ScenarioSpec` objects only.
- The policy gate validates and approves planner output before generation can run.
- The deterministic generator remains the only component allowed to produce final synthetic records, manifests, and `synthetic_source`-marked outputs.
- Provider abstraction reserves support for mock, local, and future Bedrock planners without changing the governed generator boundary.

## Responsibilities Inside The Platform Boundary

Inside the Synthetic Data platform boundary:

- Scenario contracts and canonical scenario definitions
- Planner-provider abstraction and prompt assets that produce `ScenarioSpec` proposals
- Policy-gate evaluation between planner output and generator execution
- Seed-based generation engine
- Contract validation
- Manifest generation and artifact hashing
- Dataset registry metadata
- Audit logging, traceability, cost tracking interfaces, and version control

Outside the Synthetic Data platform boundary:

- Guidewire applications
- RapidBotz as a consumer
- CI/CD orchestration outside dataset governance
- Jira and release-management tooling
- Business logic engines and runtime environment configuration

## Boundaries Between Layers

- The foundation defines canonical data and generation rules; upper layers consume outputs and manifests but do not mutate canonical definitions.
- Planner providers may suggest scenario intent through `ScenarioSpec`, but they do not create canonical records or bypass policy review.
- Layers 1 and 2 may request deterministic datasets, but they do not own platform contracts or schema evolution.
- Layers 3 and 4 consume datasets through application- or tool-specific paths; the adapter layer isolates their formats from canonical platform contracts.
- Layers 5 and 6 interpret outcomes and risk signals; they do not write back scenario rules or alter generation logic.

`Inferred`: In Phase 0, the layered model is realized through a narrow PolicyCenter lane with a single RapidBotz-centered consumer path rather than a broad enterprise rollout.
