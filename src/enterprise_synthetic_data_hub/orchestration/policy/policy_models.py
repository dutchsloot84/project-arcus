"""Deterministic policy decision models for ScenarioSpec review."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class PolicyViolation(BaseModel):
    """Machine-readable detail describing why a ScenarioSpec was denied."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    code: str
    path: str
    message: str
    value: Any = None


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
