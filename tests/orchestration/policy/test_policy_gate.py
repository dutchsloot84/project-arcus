from __future__ import annotations

from datetime import timezone

from enterprise_synthetic_data_hub.orchestration.policy import (
    MAX_RECORD_TARGET_PER_ENTITY,
    POLICY_VERSION,
    PolicyAuditRecord,
    evaluate_scenario_spec,
)
from enterprise_synthetic_data_hub.orchestration.schemas import (
    CURRENT_SCHEMA_VERSION,
    ScenarioSpec,
    validate_scenario_spec,
)


def build_payload(**overrides: object) -> dict[str, object]:
    payload: dict[str, object] = {
        "schema_version": CURRENT_SCHEMA_VERSION,
        "scenario_id": "scenario-person-001",
        "scenario_name": "Person Scenario",
        "requested_entities": ["person"],
        "record_targets": {"person": 10},
        "constraints": {"state": "AZ"},
        "seed_strategy": "explicit",
        "seed": 101,
        "planner_metadata": {"planner_family": "mock"},
    }
    payload.update(overrides)
    return payload


def test_allows_person_only_scenario() -> None:
    decision = evaluate_scenario_spec(validate_scenario_spec(build_payload()))

    assert decision.allowed is True
    assert decision.decision == "allow"
    assert decision.violations == ()


def test_allows_explicit_seed_with_seed_present() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                scenario_id="scenario-explicit-seed-001",
                scenario_name="Explicit Seed Scenario",
                seed_strategy="explicit",
                seed=2026,
            )
        )
    )

    assert decision.allowed is True
    assert decision.decision == "allow"
    assert decision.violations == ()


def test_allows_randomized_seed_with_no_seed() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                scenario_id="scenario-randomized-001",
                scenario_name="Randomized Scenario",
                seed_strategy="randomized",
                seed=None,
            )
        )
    )

    assert decision.allowed is True
    assert decision.decision == "allow"
    assert decision.violations == ()


def test_denies_unsupported_entity() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                requested_entities=["person", "property"],
                record_targets={"person": 10},
            )
        )
    )

    assert decision.allowed is False
    assert decision.decision == "deny"
    assert [violation.rule_id for violation in decision.violations] == [
        "unsupported_entity"
    ]
    assert decision.violations[0].path == "requested_entities[1]"
    assert decision.violations[0].severity == "error"
    assert decision.violations[0].blocking is True


def test_denies_excessive_record_target() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                record_targets={"person": MAX_RECORD_TARGET_PER_ENTITY + 1},
            )
        )
    )

    assert decision.allowed is False
    assert decision.violations[0].rule_id == "excessive_record_target"
    assert decision.violations[0].path == "record_targets.person"
    assert decision.violations[0].severity == "error"
    assert decision.violations[0].blocking is True


def test_denies_unsupported_schema_version() -> None:
    spec = ScenarioSpec.model_construct(
        **build_payload(schema_version="2.0"),
    )

    decision = evaluate_scenario_spec(spec)

    assert decision.allowed is False
    assert decision.violations[0].rule_id == "unsupported_schema_version"
    assert decision.violations[0].path == "schema_version"
    assert decision.violations[0].severity == "error"
    assert decision.violations[0].blocking is True


def test_denies_randomized_seed_strategy_with_seed_present() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                seed_strategy="randomized",
                seed=2026,
            )
        )
    )

    assert decision.allowed is False
    assert decision.violations[0].rule_id == "invalid_seed_configuration"
    assert decision.violations[0].path == "seed"
    assert decision.violations[0].severity == "error"
    assert decision.violations[0].blocking is True


def test_denies_unknown_constraint_key() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                constraints={"state": "AZ", "market": "commercial-auto"},
            )
        )
    )

    assert decision.allowed is False
    assert decision.violations[0].rule_id == "unsupported_constraint_key"
    assert decision.violations[0].path == "constraints.market"
    assert decision.violations[0].severity == "error"
    assert decision.violations[0].blocking is True


def test_denies_operational_metadata_fields_in_planner_metadata() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                planner_metadata={
                    "planner_family": "mock",
                    "execution": {"latency": 48},
                }
            )
        )
    )

    assert decision.allowed is False
    assert decision.violations[0].rule_id == "forbidden_planner_metadata"
    assert decision.violations[0].path == "planner_metadata.execution.latency"
    assert decision.violations[0].severity == "error"
    assert decision.violations[0].blocking is True


def test_policy_audit_record_defaults_to_utc_timestamp() -> None:
    record = PolicyAuditRecord(
        scenario_id="scenario-person-001",
        schema_version=CURRENT_SCHEMA_VERSION,
        decision="allow",
    )

    assert record.violations == ()
    assert record.policy_version == POLICY_VERSION
    assert record.evaluated_at.tzinfo is not None
    assert record.evaluated_at.utcoffset() == timezone.utc.utcoffset(
        record.evaluated_at
    )
