# Project Context

This page distills the Phase 0 architecture ingestion artifact at [context/confluence_ingestion/20260311_arcus_phase0_architecture_first_pass.md](../context/confluence_ingestion/20260311_arcus_phase0_architecture_first_pass.md). Items labeled `Inferred` are synthesis carried forward from that artifact and are not direct source statements.

## Mission / Purpose

- Establish a governed, deterministic, and auditable way to generate synthetic test data scenarios for QA, automation, performance testing, and future AI-driven testing across Guidewire applications.
- Reduce release triage noise by removing non-reproducible failures caused by environment data drift.
- Provide a synthetic data foundation for the broader Test Intelligence stack.

`Inferred`: Arcus treats test data as governed infrastructure so reproducibility and auditability are built into delivery rather than added after failures occur.

## Pilot Scope

- Business lane: Commercial Auto new business in PolicyCenter.
- Consumer path: one consuming application path centered on RapidBotz plus the Guidewire integration path.
- Scenario volume: 1-3 foundational Tier 1 scenarios.
- Environments: 1-2 lower environments such as Dev2 and QA.
- Data guarantees: deterministic seed-based generation, manifest audit logging, and golden snapshot reproducibility.
- Explicit limits: no endorsements, renewals, fleet scenarios, or multi-vehicle expansion during Phase 0.

`Inferred`: Phase 0 is intentionally a single-lane, low-scenario pilot that proves governance and reproducibility before any broader expansion.

## Explicit Non-Goals

- Using masked production data or introducing production write paths.
- Treating the platform as an uncontrolled AI-generated data system.
- Replacing application business logic validation or unit tests.
- Owning application rating logic or other Guidewire business rules.
- Expanding to ClaimCenter, BillingCenter, or multi-application hydration in Phase 0.
- Introducing enterprise marketplace features, large scenario-library growth, or autonomous schema mutation during the pilot.

## Key Invariants

- The canonical synthetic model is not directly editable by QA, RapidBotz, CI/CD, or environment-specific workflows.
- Generation is allowed only inside a controlled execution boundary and must remain non-production in scope.
- Reproducibility requires a fixed seed, fixed logic state, fixed schema or canonical version, and logged manifests.
- Dataset variations must be seed-derived; manual post-generation edits are not part of the pilot model.
- Scope expansion triggers formal review rather than informal consumer-driven changes.

## Architecture Layers

The Phase 0 architecture uses a six-layer Test Intelligence stack with Synthetic Data Hub as the foundation:

- Foundation: Synthetic Data Hub provides the canonical model, generation engine, manifests, registry metadata, and audit controls.
- Layer 1: Unit testing consumes deterministic fixtures and scenario outputs.
- Layer 2: DevOps CI/CD coordinates repeatable execution paths that request governed datasets.
- Layer 3: Performance tooling consumes deterministic datasets for non-production test runs.
- Layer 4: RapidBotz and API automation request and use datasets through adapter boundaries.
- Layer 5: DIRR and AI test intelligence analyze results using traceable synthetic data inputs.
- Layer 6: Release governance and risk visibility use reproducible evidence from the lower layers.

See [docs/architecture/architecture_at_a_glance.md](architecture/architecture_at_a_glance.md) for the layer map and [docs/architecture/trust_boundaries.md](architecture/trust_boundaries.md) for control-plane, usage-plane, and mutation boundaries.
