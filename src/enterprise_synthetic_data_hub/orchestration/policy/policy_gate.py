"""Standalone policy gate for ScenarioSpec review."""

from __future__ import annotations

from enterprise_synthetic_data_hub.orchestration.policy.policy_models import PolicyDecision
from enterprise_synthetic_data_hub.orchestration.policy.policy_rules import evaluate_policy_rules
from enterprise_synthetic_data_hub.orchestration.schemas import ScenarioSpec


def evaluate_scenario_spec(spec: ScenarioSpec) -> PolicyDecision:
    """Return a deterministic allow/deny decision for a validated ScenarioSpec."""

    violations = evaluate_policy_rules(spec)
    if not violations:
        return PolicyDecision.allow()
    return PolicyDecision.deny(violations)
