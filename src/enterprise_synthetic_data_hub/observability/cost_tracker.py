"""Cost metadata placeholders kept outside ScenarioSpec and execution contracts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CostRecord:
    """Post-execution provider usage metadata for later attribution."""

    provider: str
    input_tokens: int = 0
    output_tokens: int = 0
    estimated_cost_usd: float = 0.0
