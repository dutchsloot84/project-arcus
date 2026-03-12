# Orchestration Flow

Phase 2 adds the package boundary for the future orchestration path without changing runtime behavior.

Intended flow:

Planner -> ScenarioSpec -> Policy Gate -> Deterministic Generator -> Manifest/Audit

The deterministic generator remains the only component allowed to create final synthetic records.
