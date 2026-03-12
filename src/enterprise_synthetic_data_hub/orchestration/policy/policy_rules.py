"""Explicit rule set for deterministic ScenarioSpec policy review."""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from typing import Any, Callable

from enterprise_synthetic_data_hub.orchestration.policy.policy_models import PolicyViolation
from enterprise_synthetic_data_hub.orchestration.schemas import (
    CURRENT_SCHEMA_VERSION,
    ScenarioSpec,
)

SUPPORTED_ENTITIES = frozenset({"person", "vehicle", "profile"})
SUPPORTED_SCHEMA_VERSIONS = frozenset({CURRENT_SCHEMA_VERSION})
MAX_RECORD_TARGET_PER_ENTITY = 500
ALLOWED_CONSTRAINT_KEYS = frozenset(
    {"state", "risk_tier", "vehicle_count", "household_size"}
)
FORBIDDEN_PLANNER_METADATA_KEYS = frozenset(
    {
        "completion_tokens",
        "cost",
        "cost_usd",
        "latency_ms",
        "prompt_tokens",
        "retries",
        "retry_count",
        "runtime_ms",
        "token_usage",
        "total_cost_usd",
        "total_tokens",
    }
)
PolicyRule = Callable[[ScenarioSpec], list[PolicyViolation]]


def evaluate_supported_schema_version(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject ScenarioSpec versions that the policy gate does not support."""

    if spec.schema_version in SUPPORTED_SCHEMA_VERSIONS:
        return []
    return [
        PolicyViolation(
            code="unsupported_schema_version",
            path="schema_version",
            message=(
                f"ScenarioSpec schema_version '{spec.schema_version}' is not supported."
            ),
            value=spec.schema_version,
        )
    ]


def evaluate_supported_entities(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject unsupported entity names in requested entities or record targets."""

    violations: list[PolicyViolation] = []
    for index, entity in enumerate(spec.requested_entities):
        if entity not in SUPPORTED_ENTITIES:
            violations.append(
                PolicyViolation(
                    code="unsupported_entity",
                    path=f"requested_entities[{index}]",
                    message=f"Entity '{entity}' is not supported by the policy gate.",
                    value=entity,
                )
            )

    for entity in sorted(spec.record_targets):
        if entity not in SUPPORTED_ENTITIES:
            violations.append(
                PolicyViolation(
                    code="unsupported_entity",
                    path=f"record_targets.{entity}",
                    message=f"Entity '{entity}' is not supported by the policy gate.",
                    value=entity,
                )
            )
    return violations


def evaluate_record_targets(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject record targets that exceed the configured per-entity maximum."""

    violations: list[PolicyViolation] = []
    for entity, target in sorted(spec.record_targets.items()):
        if target > MAX_RECORD_TARGET_PER_ENTITY:
            violations.append(
                PolicyViolation(
                    code="excessive_record_target",
                    path=f"record_targets.{entity}",
                    message=(
                        f"record_targets.{entity} exceeds the maximum of "
                        f"{MAX_RECORD_TARGET_PER_ENTITY}."
                    ),
                    value=target,
                )
            )
    return violations


def evaluate_constraint_keys(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject unknown top-level constraint keys."""

    violations: list[PolicyViolation] = []
    for key in sorted(spec.constraints):
        if key not in ALLOWED_CONSTRAINT_KEYS:
            violations.append(
                PolicyViolation(
                    code="unsupported_constraint_key",
                    path=f"constraints.{key}",
                    message=f"Constraint key '{key}' is not allowed.",
                    value=key,
                )
            )
    return violations


def evaluate_seed_configuration(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject disallowed seed combinations that should never reach execution."""

    violations: list[PolicyViolation] = []
    if spec.seed_strategy == "explicit" and spec.seed is None:
        violations.append(
            PolicyViolation(
                code="invalid_seed_configuration",
                path="seed",
                message="seed is required when seed_strategy is 'explicit'.",
                value=spec.seed,
            )
        )
    if spec.seed_strategy == "randomized" and spec.seed is not None:
        violations.append(
            PolicyViolation(
                code="invalid_seed_configuration",
                path="seed",
                message="seed must be omitted when seed_strategy is 'randomized'.",
                value=spec.seed,
            )
        )
    return violations


def evaluate_planner_metadata(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject operational metadata fields embedded into planner_metadata."""

    violations: list[PolicyViolation] = []
    for key, path, value in _walk_forbidden_metadata_fields(
        spec.planner_metadata,
        base_path="planner_metadata",
    ):
        violations.append(
            PolicyViolation(
                code="forbidden_planner_metadata",
                path=path,
                message=(
                    f"planner_metadata contains operational field '{key}', which must "
                    "remain in observability metadata."
                ),
                value=value,
            )
        )
    return violations


POLICY_RULES: tuple[PolicyRule, ...] = (
    evaluate_supported_schema_version,
    evaluate_supported_entities,
    evaluate_record_targets,
    evaluate_constraint_keys,
    evaluate_seed_configuration,
    evaluate_planner_metadata,
)


def evaluate_policy_rules(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Run every policy rule in a fixed order and collect violations."""

    violations: list[PolicyViolation] = []
    for rule in POLICY_RULES:
        violations.extend(rule(spec))
    return violations


def _walk_forbidden_metadata_fields(
    value: Any,
    *,
    base_path: str,
) -> Iterable[tuple[str, str, Any]]:
    if isinstance(value, Mapping):
        for key in sorted(value):
            item = value[key]
            path = f"{base_path}.{key}"
            if key in FORBIDDEN_PLANNER_METADATA_KEYS:
                yield key, path, item
            yield from _walk_forbidden_metadata_fields(item, base_path=path)
        return

    if isinstance(value, Sequence) and not isinstance(value, str):
        for index, item in enumerate(value):
            yield from _walk_forbidden_metadata_fields(
                item,
                base_path=f"{base_path}[{index}]",
            )
