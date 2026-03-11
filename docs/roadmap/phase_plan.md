# Phase Plan

## Phase 0: Repo Reset

- Quarantine the legacy POC under `legacy/poc/`
- Replace the repo root with the initial operating system structure
- Establish guardrails, ADR conventions, workflow, and agent contract

## Phase 1: Operating System Hardening

- Add manifest examples and validation checks
- Add architecture notes for active subsystems and adapter strategy
- Expand repo-level tests for workflow and contract compliance
- Define SOPs for context ingestion, ADR creation, and release preparation

## Phase 2: Adapter and Context Expansion

- Populate `adapters/aws_bedrock/` and `adapters/local/` with concrete integration contracts
- Add structured context ingestion assets and domain knowledge references
- Introduce example manifests and prompt packs for common delivery tasks

## Phase 3: Active Product Work On The New Foundation

- Build new implementation surfaces only after contracts and schemas exist
- Keep legacy POC isolated unless its assets are intentionally migrated
- Use ADRs to document any major deviation from the initial operating model
