"""Structural validation helpers for planner-proposed ScenarioSpec payloads."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from pydantic import ValidationError

from .scenario_spec import ScenarioSpec


class ScenarioSpecValidationError(ValueError):
    """Raised when planner output falls outside the allowed ScenarioSpec shape."""


def validate_scenario_spec(payload: Mapping[str, Any] | ScenarioSpec) -> ScenarioSpec:
    """Return a validated ScenarioSpec or raise a clear structural validation error."""

    if isinstance(payload, ScenarioSpec):
        return payload
    if not isinstance(payload, Mapping):
        raise ScenarioSpecValidationError("ScenarioSpec payload must be an object.")

    try:
        return ScenarioSpec.model_validate(dict(payload))
    except ValidationError as exc:
        raise ScenarioSpecValidationError(_format_validation_error(exc)) from exc


def _format_validation_error(error: ValidationError) -> str:
    details: list[str] = []
    for issue in error.errors(include_url=False):
        location = ".".join(str(part) for part in issue["loc"]) or "scenario_spec"
        details.append(f"{location}: {issue['msg']}")
    return "Invalid ScenarioSpec payload: " + "; ".join(details)
