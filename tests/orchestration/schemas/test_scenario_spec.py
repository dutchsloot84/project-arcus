from __future__ import annotations

import pytest

from enterprise_synthetic_data_hub.orchestration.schemas import (
    CURRENT_SCHEMA_VERSION,
    ScenarioSpec,
    ScenarioSpecValidationError,
    validate_scenario_spec,
)


def build_payload(**overrides: object) -> dict[str, object]:
    payload: dict[str, object] = {
        "schema_version": CURRENT_SCHEMA_VERSION,
        "scenario_id": "scenario-person-001",
        "scenario_name": "Person Scenario",
        "requested_entities": ["person"],
        "record_targets": {"person": 10},
        "constraints": {"market": "commercial-auto"},
        "seed_strategy": "explicit",
        "seed": 101,
        "planner_metadata": {"planner_family": "mock"},
    }
    payload.update(overrides)
    return payload


def test_accepts_valid_person_only_scenario_with_explicit_seed() -> None:
    scenario_spec = validate_scenario_spec(build_payload())

    assert isinstance(scenario_spec, ScenarioSpec)
    assert scenario_spec.schema_version == CURRENT_SCHEMA_VERSION
    assert scenario_spec.seed_strategy == "explicit"
    assert scenario_spec.seed == 101


def test_accepts_valid_person_vehicle_scenario_with_randomized_seed_strategy() -> None:
    scenario_spec = validate_scenario_spec(
        build_payload(
            scenario_id="scenario-person-vehicle-001",
            scenario_name="Person And Vehicle Scenario",
            requested_entities=["person", "vehicle"],
            record_targets={"person": 5, "vehicle": 5},
            seed_strategy="randomized",
            seed=None,
        )
    )

    assert scenario_spec.requested_entities == ["person", "vehicle"]
    assert scenario_spec.seed_strategy == "randomized"
    assert scenario_spec.seed is None


@pytest.mark.parametrize(
    ("payload", "expected_message"),
    [
        (build_payload(requested_entities=[]), "requested_entities"),
        (build_payload(seed_strategy="default"), "seed_strategy"),
        (build_payload(record_targets={"person": 0}), "record_targets"),
        (build_payload(record_targets={"person": -1}), "record_targets"),
        (build_payload(constraints=["not", "an", "object"]), "constraints"),
        (build_payload(seed=None), "seed"),
    ],
)
def test_rejects_invalid_scenario_spec_payloads(
    payload: dict[str, object], expected_message: str
) -> None:
    with pytest.raises(ScenarioSpecValidationError, match=expected_message):
        validate_scenario_spec(payload)


def test_rejects_missing_schema_version() -> None:
    payload = build_payload()
    payload.pop("schema_version")

    with pytest.raises(ScenarioSpecValidationError, match="schema_version"):
        validate_scenario_spec(payload)


def test_accepts_randomized_seed_strategy_without_seed() -> None:
    scenario_spec = validate_scenario_spec(
        build_payload(
            scenario_id="scenario-randomized-001",
            scenario_name="Randomized Scenario",
            seed_strategy="randomized",
            seed=None,
        )
    )

    assert scenario_spec.seed_strategy == "randomized"
    assert scenario_spec.seed is None
