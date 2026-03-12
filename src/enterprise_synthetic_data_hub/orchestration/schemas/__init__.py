"""Code-owned orchestration schemas will live here, including the future Pydantic ScenarioSpec."""

from __future__ import annotations

from typing import Any, Mapping

ScenarioSpecPayload = Mapping[str, Any]

__all__ = ["ScenarioSpecPayload"]
