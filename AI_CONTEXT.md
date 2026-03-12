# AI Context

This file defines durable guardrails for AI-assisted development related to the Arcus orchestration pivot. Treat it as a persistent repo rule set for planning, implementation, and review work that touches orchestration behavior.

## Core Architecture Rules

1. The deterministic generator is the only component allowed to create final synthetic records.
2. LLMs may only produce structured `ScenarioSpec` objects.
3. `ScenarioSpec` is a clean, provider-agnostic Pydantic planning contract. Runtime cost, token usage, latency, retries, and related execution details are excluded.
4. `ScenarioSpec` must be validated with Pydantic before any execution.
5. A policy gate must evaluate planner output before the generator runs.
6. Policy gates may enforce configured budget thresholds, but budget and cost must not be embedded into `ScenarioSpec`.
7. Providers must remain swappable: mock, local, bedrock.
8. Canonical schemas and invariants are code-owned, not prompt-owned.
9. Prompts live in Markdown files.
10. Scenario packs live in YAML.
11. All orchestration activity must support audit, lineage, and post-execution runtime metadata capture through observability and provider execution records.
12. Determinism, replayability, manifests, golden tests, and governance markers must remain intact.

## Working Expectations

- Treat orchestration work as contract-first and governance-first.
- Do not let prompts, provider-specific behavior, or convenience tooling bypass code-owned validation and policy enforcement.
- Keep planner output, policy enforcement, deterministic record generation, and runtime observability as separate responsibilities.
- Treat cost and budget controls as policy and observability concerns, not `ScenarioSpec` fields.
- Preserve repo-level truth alignment with ADRs, guardrails, and implementation docs when making orchestration changes.
