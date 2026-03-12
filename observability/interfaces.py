from __future__ import annotations

from typing import Mapping, Protocol

from orchestration.scenario_spec import ScenarioSpec


class AuditLogger(Protocol):
    def record_policy_decision(
        self,
        *,
        scenario_spec: ScenarioSpec | None,
        allowed: bool,
        reason: str,
        metadata: Mapping[str, object] | None = None,
    ) -> None:
        """Record audit events for planner proposals and policy outcomes."""


class TraceRecorder(Protocol):
    def record_span(
        self,
        name: str,
        *,
        attributes: Mapping[str, object] | None = None,
    ) -> None:
        """Record orchestration traces across planner, policy, and generator stages."""


class CostTracker(Protocol):
    def record_usage(
        self,
        *,
        provider: str,
        input_tokens: int = 0,
        output_tokens: int = 0,
        estimated_cost_usd: float = 0.0,
    ) -> None:
        """Record provider usage for later cost attribution."""
