# Orchestration Flow

Phase 2 adds the package boundary for the future orchestration path without changing runtime behavior.

Intended flow:

Planner -> ScenarioSpec -> Policy Gate -> Deterministic Generator -> Manifest/Audit

The deterministic generator remains the only component allowed to create final synthetic records.
The Phase 4 policy gate stays deterministic, returns explicit allow or deny decisions,
and is not wired into runtime execution paths yet.
