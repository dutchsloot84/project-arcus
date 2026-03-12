# Prompts

This directory holds active prompt assets for planner-oriented workflows.

Prompt storage rules:

- Prompts are stored as Markdown files.
- Canonical schemas and invariants must not live in prompts.
- Prompts support planning and validation workflows only.

Current pivot constraints:

- planners may only propose structured `ScenarioSpec` payloads
- policy evaluation must occur before any generator execution
- the deterministic generator remains the only component allowed to create final synthetic records
