"""Deterministic policy decision models for ScenarioSpec review."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from enterprise_synthetic_data_hub.orchestration.policy.policy_config import POLICY_VERSION


class PolicyViolation(BaseModel):
    """Machine-readable detail describing why a ScenarioSpec was denied."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    rule_id: str
    message: str
    path: str | None = None
    severity: Literal["error", "warning"]
    blocking: bool


class PolicyAuditRecord(BaseModel):
    """Audit-friendly record describing a completed policy evaluation."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    scenario_id: str
    schema_version: str
    decision: Literal["allow", "deny"]
    violations: tuple[PolicyViolation, ...] = Field(default_factory=tuple)
    policy_version: str = POLICY_VERSION
    evaluated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class PolicyDecision(BaseModel):
    """Allow or deny result for a fully-evaluated ScenarioSpec."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    allowed: bool
    decision: Literal["allow", "deny"]
    violations: tuple[PolicyViolation, ...] = Field(default_factory=tuple)

    @model_validator(mode="after")
    def validate_consistency(self) -> "PolicyDecision":
        if self.allowed != (self.decision == "allow"):
            raise ValueError("allowed must match the decision field.")
        if self.allowed and self.violations:
            raise ValueError("Allowed policy decisions cannot contain violations.")
        if not self.allowed and not self.violations:
            raise ValueError("Denied policy decisions must contain violations.")
        return self

    @classmethod
    def allow(cls) -> "PolicyDecision":
        """Build a successful policy decision."""

        return cls(allowed=True, decision="allow")

    @classmethod
    def deny(cls, violations: list[PolicyViolation]) -> "PolicyDecision":
        """Build a denied policy decision with ordered violations."""

        return cls(allowed=False, decision="deny", violations=tuple(violations))
