from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import Mapping

from orchestration.scenario_spec import ScenarioSpec


class ProviderKind(str, Enum):
    MOCK = "mock"
    LOCAL = "local"
    BEDROCK = "bedrock"


SUPPORTED_PROVIDER_KINDS = tuple(kind.value for kind in ProviderKind)


class PlannerProvider(ABC):
    """Contract for providers that propose ScenarioSpec objects."""

    provider_kind: ProviderKind

    @abstractmethod
    def propose_scenario(
        self,
        prompt: str,
        *,
        seed: int,
        context: Mapping[str, object] | None = None,
    ) -> ScenarioSpec:
        """Return a structured ScenarioSpec proposal and never final records."""
