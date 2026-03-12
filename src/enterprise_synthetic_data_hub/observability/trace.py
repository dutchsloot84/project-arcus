"""Trace placeholders for future orchestration-stage visibility."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class TraceRecord:
    """Minimal trace span record for planner and policy pipeline instrumentation."""

    name: str
    attributes: dict[str, Any] = field(default_factory=dict)
