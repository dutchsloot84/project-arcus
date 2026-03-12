# Arcus Open Questions

This file is the parking lot for unresolved design decisions that should be answered before or during implementation. Move resolved items into code, docs, ADRs, or SOPs instead of leaving them here.

## Policy Gate

- What exact policy checks must run before the generator is allowed to execute a validated `ScenarioSpec`?
- Should policy failures be hard-stop only, or do any cases allow bounded warnings with explicit approval?
- What audit record is required for each policy decision so reviewers can reconstruct why a scenario was allowed or rejected?

## Cost Ceilings

- What cost ceiling should apply per orchestration request, per scenario pack, and per CI run?
- Should cost enforcement happen in the provider layer, the policy gate, or both?
- What is the fallback behavior when a provider estimate or live run exceeds the allowed ceiling?

## Retrieval Scope

- Will planner providers be retrieval-free in the first implementation slice, or may they read approved repo context beyond prompt files and scenario packs?
- If retrieval is allowed, what paths are in scope and how is that scope recorded for audit and replay?
- Do prompt authors need an explicit allowlist for any retrieval-backed context source?

## Schema Versioning

- How will `ScenarioSpec` versions be named, stored, and validated across examples, tests, prompts, and scenario packs?
- What compatibility promise applies when a scenario pack references an older schema version?
- When should version changes require an ADR versus a smaller contract update?

## Bedrock Runtime Behavior

- Which Bedrock model families and runtime settings are acceptable for planner use in the first supported slice?
- What retry, timeout, and error-normalization rules should the Bedrock adapter enforce?
- What provider response fields must be preserved for lineage, audit, and cost reporting?
