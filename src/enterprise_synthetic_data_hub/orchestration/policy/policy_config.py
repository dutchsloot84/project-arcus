"""Configuration boundaries for deterministic ScenarioSpec policy evaluation."""

from __future__ import annotations

from enterprise_synthetic_data_hub.orchestration.schemas import CURRENT_SCHEMA_VERSION

MAX_RECORD_TARGET_PER_ENTITY = 500
SUPPORTED_ENTITIES = {"person", "vehicle", "profile"}
ALLOWED_CONSTRAINT_KEYS = {
    "state",
    "risk_tier",
    "vehicle_count",
    "household_size",
}
FORBIDDEN_PLANNER_METADATA_KEYS = {
    "cost",
    "tokens",
    "latency",
    "retry",
    "provider",
    "model",
}
POLICY_VERSION = "1.0"
SUPPORTED_SCHEMA_VERSIONS = frozenset({CURRENT_SCHEMA_VERSION})
