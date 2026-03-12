"""Stub mock provider reserved for future non-production orchestration wiring."""

from __future__ import annotations

from typing import Any, Mapping

from enterprise_synthetic_data_hub.orchestration.schemas import ScenarioSpecPayload

from .base_provider import PlannerProvider, ProviderKind


class MockProvider(PlannerProvider):
    """Placeholder provider for deterministic mock planning in a later phase."""

    provider_kind = ProviderKind.MOCK

    def plan(
        self,
        *,
        system_prompt: str,
        scenario_prompt: str,
        context: Mapping[str, Any] | None = None,
    ) -> ScenarioSpecPayload:
        raise NotImplementedError("Mock provider wiring is deferred beyond Phase 2 scaffolding.")
