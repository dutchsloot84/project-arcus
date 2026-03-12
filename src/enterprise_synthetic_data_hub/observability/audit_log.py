"""Audit log placeholders for planner, policy, and execution decisions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class AuditLogEntry:
    """Minimal audit record shape for future orchestration events."""

    event_type: str
    message: str
    details: dict[str, Any] = field(default_factory=dict)
