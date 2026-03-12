from __future__ import annotations

from enterprise_synthetic_data_hub.orchestration.policy import (
    MAX_RECORD_TARGET_PER_ENTITY,
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


def test_allows_person_vehicle_scenario() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                scenario_id="scenario-person-vehicle-001",
                scenario_name="Person And Vehicle Scenario",
                requested_entities=["person", "vehicle"],
                record_targets={"person": 15, "vehicle": 15},
                constraints={"state": "AZ", "vehicle_count": 1},
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
    assert [violation.code for violation in decision.violations] == [
        "unsupported_entity"
    ]
    assert decision.violations[0].path == "requested_entities[1]"


def test_denies_excessive_record_target() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                record_targets={"person": MAX_RECORD_TARGET_PER_ENTITY + 1},
            )
        )
    )

    assert decision.allowed is False
    assert decision.violations[0].code == "excessive_record_target"
    assert decision.violations[0].path == "record_targets.person"


def test_denies_unsupported_schema_version() -> None:
    spec = ScenarioSpec.model_construct(
        **build_payload(schema_version="2.0"),
    )

    decision = evaluate_scenario_spec(spec)

    assert decision.allowed is False
    assert decision.violations[0].code == "unsupported_schema_version"
    assert decision.violations[0].path == "schema_version"


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
    assert decision.violations[0].code == "invalid_seed_configuration"
    assert decision.violations[0].path == "seed"


def test_denies_unknown_constraint_key() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                constraints={"state": "AZ", "market": "commercial-auto"},
            )
        )
    )

    assert decision.allowed is False
    assert decision.violations[0].code == "unsupported_constraint_key"
    assert decision.violations[0].path == "constraints.market"


def test_denies_operational_metadata_fields_in_planner_metadata() -> None:
    decision = evaluate_scenario_spec(
        validate_scenario_spec(
            build_payload(
                planner_metadata={
                    "planner_family": "mock",
                    "execution": {"latency_ms": 48},
                }
            )
        )
    )

    assert decision.allowed is False
    assert decision.violations[0].code == "forbidden_planner_metadata"
    assert decision.violations[0].path == "planner_metadata.execution.latency_ms"
