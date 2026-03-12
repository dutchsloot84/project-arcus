"""Abstract planner-provider contract for provider-agnostic orchestration."""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Mapping

from enterprise_synthetic_data_hub.orchestration.schemas import ScenarioSpecPayload


class ProviderKind(str, Enum):
    """Supported planner provider families."""

    MOCK = "mock"
    LOCAL = "local"
    BEDROCK = "bedrock"


class PlannerProvider(ABC):
    """Provider contract for proposing structured ScenarioSpec payloads only."""

    provider_kind: ProviderKind

    @abstractmethod
    def plan(
        self,
        *,
        system_prompt: str,
        scenario_prompt: str,
        context: Mapping[str, Any] | None = None,
    ) -> ScenarioSpecPayload:
        """Return planner output for later validation and policy review."""
