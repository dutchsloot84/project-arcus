# Prompts

This directory holds active prompt assets for planner providers.

Current pivot constraints:

- planners may only propose structured `ScenarioSpec` payloads
- policy evaluation must occur before any generator execution
- the deterministic generator remains the only component allowed to create final synthetic records
