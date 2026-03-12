from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .scenario_spec import ScenarioSpec
from .validators import ScenarioSpecValidationError, validate_scenario_spec


@dataclass(frozen=True, slots=True)
class PolicyDecision:
    allowed: bool
    reason: str
    scenario_spec: ScenarioSpec | None = None


def evaluate_planner_output(payload: Mapping[str, object]) -> PolicyDecision:
    """Apply the minimal policy gate between planner output and generation."""

    try:
        scenario_spec = validate_scenario_spec(payload)
    except ScenarioSpecValidationError as exc:
        return PolicyDecision(allowed=False, reason=str(exc))

    return PolicyDecision(
        allowed=True,
        reason="ScenarioSpec passed placeholder policy validation.",
        scenario_spec=scenario_spec,
    )
