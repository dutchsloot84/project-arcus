# Arcus Orchestration Migration Plan

This plan tracks the documentation-first migration from the current baseline to a provider-agnostic orchestration layer without weakening Arcus determinism or governance guarantees.

## Phase 1 - Architecture Freeze

### Objective

Lock the orchestration direction, repo invariants, and tracking artifacts before runtime work begins.

### Key Deliverables

- Accepted architecture decision and companion tracking artifacts
- Durable AI guardrails for orchestration work
- Phase plan aligned to a provider-agnostic `ScenarioSpec` Pydantic contract, prompts in Markdown, and scenario packs in YAML

### Exit Criteria

- Architecture rules are explicit and consistent across the repo
- `ScenarioSpec` is documented as planning-only and runtime cost metadata is assigned to observability
- Tracking artifacts exist for migration planning, execution, and open questions
- Future implementation work has a clear read path and source of truth

### Risks / Dependencies

- Depends on ADR-0004 remaining the active architecture decision
- Risk of policy drift if new orchestration docs diverge from repo guardrails

## Phase 2 - Repo Scaffolding

### Objective

Create the active directory and module layout for orchestration, providers, prompts, scenario packs, and observability without implementing provider runtime behavior yet.

### Key Deliverables

- Initial folder structure for orchestration-related subsystems
- Minimal placeholder modules and README-level orientation where needed
- Companion tests or examples proving the scaffold is coherent

### Exit Criteria

- Repo paths for orchestration work are present and discoverable
- Scaffolding reflects the provider-swappable architecture
- No runtime path bypasses the generator boundary

### Risks / Dependencies

- Depends on the architecture freeze and repo naming conventions staying stable
- Risk of over-scaffolding before the `ScenarioSpec` contract is fixed

## Phase 3 - ScenarioSpec Contract

### Objective

Define the canonical planner output contract as a clean, provider-agnostic, Pydantic-validated `ScenarioSpec`.

### Key Deliverables

- `ScenarioSpec` model and validation rules
- Schema versioning approach for the contract
- Contract boundary stating that runtime cost, token usage, latency, retries, and similar execution metadata are out of scope
- Examples and tests for valid and invalid planner output

### Exit Criteria

- Planner output cannot proceed without successful Pydantic validation
- Contract ownership is clearly code-first, not prompt-first
- `ScenarioSpec` excludes budget, cost, and other runtime observability metadata
- Versioned examples exist for replay and regression checks

### Risks / Dependencies

- Depends on agreement about required fields, invariants, and versioning policy
- Risk of freezing a contract too early without enough representative scenarios

## Phase 4 - Policy Gate

### Objective

Insert a deterministic policy evaluation step between planner output and generator execution.

### Key Deliverables

- Policy gate interface and enforcement flow
- Rejection reasons and audit-friendly decision records
- Configured budget-threshold checks that operate outside `ScenarioSpec`
- Tests covering allow, reject, and malformed planner output paths

### Exit Criteria

- Generator execution is blocked unless planner output passes policy evaluation
- Policy outcomes are logged for audit and lineage review
- Budget enforcement is configuration-driven and not embedded into planner contract fields
- Failure modes are explicit and deterministic

### Risks / Dependencies

- Depends on a stable `ScenarioSpec` contract
- Risk of ambiguous policy outcomes if rejection semantics are underspecified

## Phase 5 - Mock Orchestration Pipeline

### Objective

Stand up the end-to-end orchestration path using a mock planner provider and the real validation and policy boundaries.

### Key Deliverables

- Shared provider interface exercised by a mock implementation
- Planner -> validation -> policy -> generator handoff flow
- Audit, lineage, and post-execution observability hooks stubbed through the pipeline

### Exit Criteria

- Mock orchestration can drive deterministic generator execution through approved paths only
- Provider swapping is proven at the interface level
- Replay and manifest expectations still hold for the executed scenarios

### Risks / Dependencies

- Depends on the policy gate and `ScenarioSpec` contract landing first
- Risk of mock-only assumptions leaking into the shared provider abstraction

## Phase 6 - Bedrock Provider Integration

### Objective

Add a Bedrock-backed planner provider behind the shared provider abstraction without changing governance boundaries.

### Key Deliverables

- Bedrock provider adapter and configuration surface
- Runtime behavior expectations for retries, errors, and response parsing
- Provider-specific observability records for cost, token usage, latency, and retries

### Exit Criteria

- Bedrock planner output still resolves to validated `ScenarioSpec` objects only
- Policy gate enforcement is unchanged for Bedrock calls
- Cost and runtime metadata are captured post-execution alongside provider execution records

### Risks / Dependencies

- Depends on Bedrock runtime decisions, credentials, and environment support
- Risk of provider-specific response behavior complicating deterministic replay evidence

## Phase 7 - Prompt Governance And Scenario Packs

### Objective

Govern prompt assets and curated scenario definitions as first-class repo artifacts.

### Key Deliverables

- Prompt file conventions in Markdown
- Scenario pack conventions in YAML
- Governance rules for review, versioning, and traceability of prompt and pack changes

### Exit Criteria

- Prompt and scenario-pack assets are discoverable, reviewable, and versioned
- Prompts do not own canonical schema or invariants
- Scenario packs map cleanly onto validated `ScenarioSpec` inputs

### Risks / Dependencies

- Depends on the shared contract and provider flow already existing
- Risk of prompt changes drifting from code-owned invariants if review rules are weak

## Phase 8 - Operational Hardening

### Objective

Strengthen the orchestration stack for repeatable delivery, governance, and long-term maintenance.

### Key Deliverables

- Golden tests, replay checks, and manifest coverage for orchestration paths
- Stronger audit, lineage, and runtime metadata reporting support
- Operational runbooks or SOP updates for future contributors

### Exit Criteria

- Determinism and replayability remain intact under orchestration
- Governance markers, manifests, and golden tests cover the new path
- The repo operating model can sustain mock, local, and Bedrock providers safely

### Risks / Dependencies

- Depends on earlier phases being complete enough to harden rather than redesign
- Risk of incomplete observability or test coverage masking governance regressions
