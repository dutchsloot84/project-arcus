from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

DISALLOWED_PLANNER_KEYS = frozenset(
    {
        "artifacts",
        "bundle",
        "dataset",
        "final_records",
        "metadata",
        "persons",
        "profiles",
        "synthetic_source",
        "vehicles",
    }
)


@dataclass(frozen=True, slots=True)
class ScenarioSpec:
    """Structured planner output that can be evaluated before generation."""

    scenario_id: str
    seed: int
    record_count: int
    provider: str
    prompt_version: str = "placeholder"
    parameters: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "scenario_id": self.scenario_id,
            "seed": self.seed,
            "record_count": self.record_count,
            "provider": self.provider,
            "prompt_version": self.prompt_version,
            "parameters": dict(self.parameters),
        }
