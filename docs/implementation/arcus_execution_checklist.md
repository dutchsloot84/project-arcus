# Arcus Execution Checklist

Use this tracker to mark orchestration-pivot work as it lands. Keep checklist updates aligned with real repo changes, not intent alone.

## Phase 1 - Architecture Freeze

- [x] Confirm architecture rules are consistent across ADRs, guardrails, and AI context
- [x] Publish migration plan, execution checklist, and open questions tracker
- [x] Lock `ScenarioSpec` as Pydantic, prompts as Markdown, and scenario packs as YAML

## Phase 2 - Repo Scaffolding

- [x] Create active orchestration, provider, prompt, and scenario-pack paths
- [x] Add minimal placeholders or examples for each new path
- [x] Verify scaffolding does not weaken current generator boundaries

## Phase 3 - ScenarioSpec Contract

- [ ] Define the Pydantic `ScenarioSpec` model
- [ ] Add validation tests for accepted and rejected planner output
- [ ] Decide and document schema versioning for `ScenarioSpec`

## Phase 4 - Policy Gate

- [ ] Add a policy gate interface between planner output and generator execution
- [ ] Define rejection reasons and audit logging expectations
- [ ] Add tests for allow, reject, and malformed-input flows

## Phase 5 - Mock Orchestration Pipeline

- [ ] Implement the shared planner-provider interface
- [ ] Add a mock provider that emits structured `ScenarioSpec` proposals
- [ ] Prove the mock path preserves manifests, replayability, and generator ownership

## Phase 6 - Bedrock Provider Integration

- [ ] Add the Bedrock provider adapter behind the shared provider interface
- [ ] Capture cost, audit, and runtime metadata for Bedrock planner calls
- [ ] Validate Bedrock output still flows through `ScenarioSpec` validation and the policy gate

## Phase 7 - Prompt Governance And Scenario Packs

- [ ] Create prompt conventions for Markdown assets
- [ ] Create scenario-pack conventions for YAML assets
- [ ] Add review and traceability rules so prompt or pack edits cannot bypass code-owned invariants

## Phase 8 - Operational Hardening

- [ ] Add golden tests and replay checks for orchestration flows
- [ ] Strengthen lineage and cost-reporting coverage
- [ ] Update runbooks, SOPs, or companion docs needed for sustained maintenance
