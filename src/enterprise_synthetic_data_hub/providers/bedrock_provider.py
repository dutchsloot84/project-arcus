"""Stub Bedrock planner provider placeholder without runtime calls."""

from __future__ import annotations

from typing import Any, Mapping

from enterprise_synthetic_data_hub.orchestration.schemas import ScenarioSpecPayload

from .base_provider import PlannerProvider, ProviderKind


class BedrockProvider(PlannerProvider):
    """Placeholder for future Bedrock-backed planning integration."""

    provider_kind = ProviderKind.BEDROCK

    def plan(
        self,
        *,
        system_prompt: str,
        scenario_prompt: str,
        context: Mapping[str, Any] | None = None,
    ) -> ScenarioSpecPayload:
        raise NotImplementedError("Bedrock runtime calls are intentionally deferred in Phase 2.")
