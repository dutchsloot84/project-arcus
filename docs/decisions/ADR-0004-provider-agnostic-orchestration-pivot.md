# ADR-0004: Provider-Agnostic Orchestration Pivot

- Status: Accepted
- Date: 2026-03-12

## Context

Project Arcus started from a local-first prototype posture, but the active architecture now needs a provider-agnostic orchestration layer that can support mock, local, and future Bedrock-backed planning without weakening deterministic generation guarantees.

The existing Arcus baseline remains non-negotiable:

- the deterministic generator is the only component allowed to create final synthetic records
- LLM-backed planners may only propose structured `ScenarioSpec` objects
- seed replayability, manifests, golden snapshots, smoke gates, and `synthetic_source` governance markers must remain intact
- policy must be enforced between planner output and generator execution
- observability must cover audit, trace, and provider cost tracking

## Decision

Arcus will pivot the active architecture to a provider-agnostic orchestration model with a strict planner-to-generator boundary.

- Planner providers produce `ScenarioSpec` proposals only.
- `ScenarioSpec` remains a clean, provider-agnostic planning contract and excludes runtime cost, token usage, latency, retries, and related execution metadata.
- A policy gate evaluates planner output before any generator execution is allowed.
- Policy gates may enforce configured budget thresholds, but budget and cost are not embedded into `ScenarioSpec`.
- The deterministic generator remains the sole writer of final synthetic records and their `synthetic_source` markers.
- Provider integration will follow a shared abstraction that reserves support for `mock`, `local`, and `bedrock`.
- Bedrock runtime calls are explicitly deferred in this slice; only the abstraction and placeholders land now.
- Observability hooks and provider execution records own audit, trace, cost, token, latency, and retry capture after execution.

## Consequences

- Arcus can evolve planner providers without allowing provider-specific runtime behavior to bypass governance.
- The architecture preserves deterministic replay guarantees by keeping scenario proposal separate from record generation.
- Swapping mock, local, and Bedrock providers does not require changing the `ScenarioSpec` contract.
- Future Bedrock or local-provider work must implement the shared provider contract and pass through the same policy gate.
- Observability expectations become an interface requirement instead of an afterthought, including post-execution runtime metadata capture.

## Alternatives Considered

### Keep The Local-First Planner Coupled To Execution

This would move faster short term, but it would hard-code provider assumptions into the active architecture and make later provider expansion riskier.

### Allow Providers To Emit Final Synthetic Records

This was rejected because it breaks Arcus's determinism and governance model by moving canonical record creation outside the approved generator boundary.

### Defer Policy And Observability Until Provider Runtime Integration

This was rejected because it would create early orchestration paths without the audit and control points Arcus requires.
