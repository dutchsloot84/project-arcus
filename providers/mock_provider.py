from __future__ import annotations

from typing import Mapping

from orchestration.scenario_spec import ScenarioSpec

from .base_provider import PlannerProvider, ProviderKind


class MockProvider(PlannerProvider):
    """Deterministic placeholder provider for orchestration tests and scaffolding."""

    provider_kind = ProviderKind.MOCK

    def propose_scenario(
        self,
        prompt: str,
        *,
        seed: int,
        context: Mapping[str, object] | None = None,
    ) -> ScenarioSpec:
        resolved_context = dict(context or {})
        requested_records = resolved_context.get("record_count", 1)
        record_count = requested_records if isinstance(requested_records, int) else 1

        return ScenarioSpec(
            scenario_id=str(resolved_context.get("scenario_id", "mock-scenario")),
            seed=seed,
            record_count=max(1, record_count),
            provider=self.provider_kind.value,
            prompt_version="mock-v1",
            parameters={
                "prompt": prompt,
                "context_keys": sorted(resolved_context.keys()),
            },
        )
