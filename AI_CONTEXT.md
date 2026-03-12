# AI Context

This file defines durable guardrails for AI-assisted development related to the Arcus orchestration pivot. Treat it as a persistent repo rule set for planning, implementation, and review work that touches orchestration behavior.

## Core Architecture Rules

1. The deterministic generator is the only component allowed to create final synthetic records.
2. LLMs may only produce structured `ScenarioSpec` objects.
3. `ScenarioSpec` must be validated with Pydantic before any execution.
4. A policy gate must evaluate planner output before the generator runs.
5. Providers must remain swappable: mock, local, bedrock.
6. Canonical schemas and invariants are code-owned, not prompt-owned.
7. Prompts live in Markdown files.
8. Scenario packs live in YAML.
9. All orchestration activity must support audit, lineage, and cost tracking.
10. Determinism, replayability, manifests, golden tests, and governance markers must remain intact.

## Working Expectations

- Treat orchestration work as contract-first and governance-first.
- Do not let prompts, provider-specific behavior, or convenience tooling bypass code-owned validation and policy enforcement.
- Keep planner output and deterministic record generation as separate responsibilities.
- Preserve repo-level truth alignment with ADRs, guardrails, and implementation docs when making orchestration changes.
