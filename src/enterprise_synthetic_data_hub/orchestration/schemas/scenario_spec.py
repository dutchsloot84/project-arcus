"""Planner-to-policy/generator contract boundary for versioned ScenarioSpec payloads."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Annotated, Any, Literal, TypeAlias

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    field_validator,
    model_validator,
)

CURRENT_SCHEMA_VERSION = "1.0"
ALLOWED_SEED_STRATEGIES = ("explicit", "randomized")

ScenarioSpecPayload: TypeAlias = Mapping[str, Any]
SeedStrategy: TypeAlias = Literal["explicit", "randomized"]
NonEmptyString = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
PositiveRecordTarget = Annotated[int, Field(strict=True, gt=0)]
OptionalStrictInt = Annotated[int, Field(strict=True)] | None


class ScenarioSpec(BaseModel):
    """Code-owned planner output contract evaluated before policy and generation."""

    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)

    schema_version: Literal["1.0"]
    scenario_id: NonEmptyString
    scenario_name: NonEmptyString
    requested_entities: list[NonEmptyString]
    record_targets: dict[NonEmptyString, PositiveRecordTarget]
    constraints: dict[NonEmptyString, Any]
    seed_strategy: SeedStrategy
    seed: OptionalStrictInt = None
    planner_metadata: dict[NonEmptyString, Any]

    @field_validator("requested_entities")
    @classmethod
    def validate_requested_entities(
        cls, requested_entities: list[NonEmptyString]
    ) -> list[NonEmptyString]:
        if not requested_entities:
            raise ValueError("requested_entities must contain at least one entity.")
        return requested_entities

    @field_validator("record_targets")
    @classmethod
    def validate_record_targets(
        cls, record_targets: dict[NonEmptyString, PositiveRecordTarget]
    ) -> dict[NonEmptyString, PositiveRecordTarget]:
        if not record_targets:
            raise ValueError(
                "record_targets must contain at least one positive integer target."
            )
        return record_targets

    @model_validator(mode="after")
    def validate_seed_rules(self) -> "ScenarioSpec":
        if self.seed_strategy == "explicit" and self.seed is None:
            raise ValueError("seed is required when seed_strategy is 'explicit'.")
        return self
