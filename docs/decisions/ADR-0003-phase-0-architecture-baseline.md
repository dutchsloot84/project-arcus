# ADR-0003: Phase 0 Architecture Baseline

- Status: Accepted
- Date: 2026-03-12

## Context

The Phase 0 architecture ingestion artifact at [context/confluence_ingestion/20260311_arcus_phase0_architecture_first_pass.md](../../context/confluence_ingestion/20260311_arcus_phase0_architecture_first_pass.md) consolidates the current pilot baseline from Confluence and Jira source material. The repo needs a concise in-repo architecture decision that freezes the pilot operating shape without expanding it beyond what the source material confirms.

The documented baseline centers on a deterministic synthetic data foundation for Guidewire testing. The pilot is intentionally narrow: a single Commercial Auto new business lane in PolicyCenter, a RapidBotz-centered consumer path, 1-3 foundational scenarios, and 1-2 lower environments. The sources also define strong governance requirements around canonical ownership, trust boundaries, and replayable generation.

## Decision

Project Arcus adopts the following Phase 0 architecture baseline:

- Use Synthetic Data Hub as the deterministic foundation beneath the six-layer Test Intelligence stack.
- Keep the pilot scope locked to Commercial Auto new business in PolicyCenter with a single RapidBotz-centered consumer path, a small Tier 1 scenario set, and 1-2 non-production environments.
- Place the trust boundary at the controlled generator execution boundary and the canonical control plane, with a metadata-only dataset registry.
- Require consumer access through request and adapter boundaries rather than direct canonical-model mutation.
- Treat reproducibility as a combined guarantee of deterministic seed, fixed logic version, fixed schema or canonical version, and manifest logging.
- Disallow production write paths, environment-specific canonical overrides, manual post-generation dataset edits, runtime schema mutation, and multi-application expansion during Phase 0.

## What Is Frozen In Phase 0

- The six-layer architecture framing with Synthetic Data Hub as the foundation
- The single-lane PolicyCenter scope and RapidBotz-centered consumer path
- The non-production-only blast radius
- The request-only usage-plane relationship to the canonical control plane
- Deterministic replay as a release-blocking invariant for the pilot

## What Is Allowed To Evolve

The source material leaves these items open, so they are not frozen by this ADR:

- The physical implementation of the dataset registry
- The formal approval workflow tooling used for canonical changes
- Manual versus pipeline-triggered generation patterns
- Risk tier definitions, telemetry thresholds, and cleanup ownership for stored artifacts
- Future expansion decisions for additional Guidewire domains or consumers, but only through later ADRs

## Consequences

- Phase 0 favors governance, auditability, and traceability over breadth, realism, and scale.
- Consumer teams get a clear boundary: request datasets, do not redefine canonical semantics.
- Expansion to other domains, adapters, or more autonomous flows now requires explicit follow-on decisions instead of quiet scope creep.
