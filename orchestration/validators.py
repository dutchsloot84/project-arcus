from __future__ import annotations

from typing import Any, Mapping

from .scenario_spec import DISALLOWED_PLANNER_KEYS, ScenarioSpec


class ScenarioSpecValidationError(ValueError):
    """Raised when planner output falls outside the allowed ScenarioSpec shape."""


def validate_scenario_spec(payload: Mapping[str, Any]) -> ScenarioSpec:
    """Placeholder validation for planner output before policy review."""

    required_keys = {"scenario_id", "seed", "record_count", "provider"}
    missing = sorted(required_keys.difference(payload))
    if missing:
        raise ScenarioSpecValidationError(
            f"ScenarioSpec is missing required keys: {', '.join(missing)}"
        )

    disallowed = sorted(DISALLOWED_PLANNER_KEYS.intersection(payload))
    if disallowed:
        raise ScenarioSpecValidationError(
            "Planner output may not include final synthetic records or governance "
            f"markers: {', '.join(disallowed)}"
        )

    seed = payload["seed"]
    record_count = payload["record_count"]
    scenario_id = payload["scenario_id"]
    provider = payload["provider"]

    if not isinstance(seed, int):
        raise ScenarioSpecValidationError("ScenarioSpec 'seed' must be an integer.")
    if not isinstance(record_count, int) or record_count <= 0:
        raise ScenarioSpecValidationError(
            "ScenarioSpec 'record_count' must be a positive integer."
        )
    if not isinstance(scenario_id, str) or not scenario_id.strip():
        raise ScenarioSpecValidationError(
            "ScenarioSpec 'scenario_id' must be a non-empty string."
        )
    if not isinstance(provider, str) or not provider.strip():
        raise ScenarioSpecValidationError(
            "ScenarioSpec 'provider' must be a non-empty string."
        )

    parameters = payload.get("parameters", {})
    if not isinstance(parameters, Mapping):
        raise ScenarioSpecValidationError(
            "ScenarioSpec 'parameters' must be an object when provided."
        )

    prompt_version = payload.get("prompt_version", "placeholder")
    if not isinstance(prompt_version, str) or not prompt_version.strip():
        raise ScenarioSpecValidationError(
            "ScenarioSpec 'prompt_version' must be a non-empty string."
        )

    return ScenarioSpec(
        scenario_id=scenario_id.strip(),
        seed=seed,
        record_count=record_count,
        provider=provider.strip(),
        prompt_version=prompt_version.strip(),
        parameters=dict(parameters),
    )
