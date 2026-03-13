"""Explicit rule set for deterministic ScenarioSpec policy review."""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from typing import Any, Callable

from enterprise_synthetic_data_hub.orchestration.policy.policy_config import (
    ALLOWED_CONSTRAINT_KEYS,
    FORBIDDEN_PLANNER_METADATA_KEYS,
    MAX_RECORD_TARGET_PER_ENTITY,
    SUPPORTED_ENTITIES,
    SUPPORTED_SCHEMA_VERSIONS,
)
from enterprise_synthetic_data_hub.orchestration.policy.policy_models import PolicyViolation
from enterprise_synthetic_data_hub.orchestration.schemas import ScenarioSpec

PolicyRule = Callable[[ScenarioSpec], list[PolicyViolation]]


def evaluate_supported_schema_version(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject ScenarioSpec versions that the policy gate does not support."""

    if spec.schema_version in SUPPORTED_SCHEMA_VERSIONS:
        return []
    return [
        _build_error_violation(
            rule_id="unsupported_schema_version",
            path="schema_version",
            message=(
                f"ScenarioSpec schema_version '{spec.schema_version}' is not supported."
            ),
        )
    ]


def evaluate_supported_entities(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject unsupported entity names in requested entities or record targets."""

    violations: list[PolicyViolation] = []
    for index, entity in enumerate(spec.requested_entities):
        if entity not in SUPPORTED_ENTITIES:
            violations.append(
                _build_error_violation(
                    rule_id="unsupported_entity",
                    path=f"requested_entities[{index}]",
                    message=f"Entity '{entity}' is not supported by the policy gate.",
                )
            )

    for entity in sorted(spec.record_targets):
        if entity not in SUPPORTED_ENTITIES:
            violations.append(
                _build_error_violation(
                    rule_id="unsupported_entity",
                    path=f"record_targets.{entity}",
                    message=f"Entity '{entity}' is not supported by the policy gate.",
                )
            )
    return violations


def evaluate_record_targets(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject record targets that exceed the configured per-entity maximum."""

    violations: list[PolicyViolation] = []
    for entity, target in sorted(spec.record_targets.items()):
        if target > MAX_RECORD_TARGET_PER_ENTITY:
            violations.append(
                _build_error_violation(
                    rule_id="excessive_record_target",
                    path=f"record_targets.{entity}",
                    message=(
                        f"record_targets.{entity} exceeds the maximum of "
                        f"{MAX_RECORD_TARGET_PER_ENTITY}."
                    ),
                )
            )
    return violations


def evaluate_constraint_keys(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject unknown top-level constraint keys."""

    violations: list[PolicyViolation] = []
    for key in sorted(spec.constraints):
        if key not in ALLOWED_CONSTRAINT_KEYS:
            violations.append(
                _build_error_violation(
                    rule_id="unsupported_constraint_key",
                    path=f"constraints.{key}",
                    message=f"Constraint key '{key}' is not allowed.",
                )
            )
    return violations


def evaluate_seed_configuration(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject disallowed seed combinations that should never reach execution."""

    violations: list[PolicyViolation] = []
    if spec.seed_strategy == "explicit" and spec.seed is None:
        violations.append(
            _build_error_violation(
                rule_id="invalid_seed_configuration",
                path="seed",
                message="seed is required when seed_strategy is 'explicit'.",
            )
        )
    if spec.seed_strategy == "randomized" and spec.seed is not None:
        violations.append(
            _build_error_violation(
                rule_id="invalid_seed_configuration",
                path="seed",
                message="seed must be omitted when seed_strategy is 'randomized'.",
            )
        )
    return violations


def evaluate_planner_metadata(spec: ScenarioSpec) -> list[PolicyViolation]:
    """Reject operational metadata fields embedded into planner_metadata."""

    violations: list[PolicyViolation] = []
    for key, path in _walk_forbidden_metadata_fields(
        spec.planner_metadata,
        base_path="planner_metadata",
    ):
        violations.append(
            _build_error_violation(
                rule_id="forbidden_planner_metadata",
                path=path,
                message=(
                    f"planner_metadata contains operational field '{key}', which must "
                    "remain in observability metadata."
                ),
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
) -> Iterable[tuple[str, str]]:
    if isinstance(value, Mapping):
        for key in sorted(value):
            item = value[key]
            path = f"{base_path}.{key}"
            if key in FORBIDDEN_PLANNER_METADATA_KEYS:
                yield key, path
            yield from _walk_forbidden_metadata_fields(item, base_path=path)
        return

    if isinstance(value, Sequence) and not isinstance(value, str):
        for index, item in enumerate(value):
            yield from _walk_forbidden_metadata_fields(
                item,
                base_path=f"{base_path}[{index}]",
            )


def _build_error_violation(
    *,
    rule_id: str,
    message: str,
    path: str | None = None,
) -> PolicyViolation:
    return PolicyViolation(
        rule_id=rule_id,
        message=message,
        path=path,
        severity="error",
        blocking=True,
    )
