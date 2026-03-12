"""Stub local planner provider placeholder with no runtime behavior yet."""

from __future__ import annotations

from typing import Any, Mapping

from enterprise_synthetic_data_hub.orchestration.schemas import ScenarioSpecPayload

from .base_provider import PlannerProvider, ProviderKind


class LocalProvider(PlannerProvider):
    """Placeholder for a local planner implementation added in a later phase."""

    provider_kind = ProviderKind.LOCAL

    def plan(
        self,
        *,
        system_prompt: str,
        scenario_prompt: str,
        context: Mapping[str, Any] | None = None,
    ) -> ScenarioSpecPayload:
        raise NotImplementedError("Local provider wiring is deferred beyond Phase 2 scaffolding.")
