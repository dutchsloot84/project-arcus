Below is a first-pass Arcus-ready extraction based only on the Confluence/Jira content you provided and the search results. I’ve kept it tight but explicit about what’s confirmed vs inferred.

## SECTION 1 — Source Inventory

1. Synthetic Data Hub — Pilot Confluence Space
Link: Synthetic Data Hub — Pilot Confluence Space
Relevance: Executive overview of the Synthetic Data Pilot (purpose, what it is/is not, governance guarantees) and direct link to Pilot Scope Lock. Strong baseline for Mission/Purpose, Governance Guarantees, and high-level Pilot framing.
Confidence: High
2. Pilot Scope Lock – Synthetic Data Platform (Phase 1)
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/5013307406/Pilot+Scope+Lock+Synthetic+Data+Platform+Phase+1
Relevance: Canonical “Pilot Scope Lock” document. Defines business objective, tightly locked lane, and explicit out-of-scope list. Contains a “Canonical Data Mutation Policy” that’s central to canonical drift prevention and schema control.
Confidence: High
3. Trust Boundary & Ownership Model – Pilot Phase
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/5013209108/Trust+Boundary+Ownership+Model+Pilot+Phase
Relevance: Defines canonical synthetic model ownership, change governance, and an explicit “Trust Boundary” plus Control Plane vs Usage Plane. Strong material for Trust Boundaries, Shared Responsibility, and guardrails around canonical model drift and mutation.
Confidence: High
4. Governance Foundation & Trust Boundary (Pilot Preparation)
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/4971757862/Governance+Foundation+Trust+Boundary+Pilot+Preparation
Relevance: Details “Trust boundary (Pilot v1)” at AWS IAM Role, dataset registry model, reproducibility model (seed + git hash + schema version + IAM), drift & retirement governance, and key architectural decisions. Directly supports Trust Boundaries, Canonical Data/Drift Prevention Rules, Deterministic/Reproducibility rules.
Confidence: High
5. POC → Pilot Planning & Integration Mapping
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/4961894959/POC+Pilot+Planning+Integration+Mapping
Relevance: Clarifies platform scope vs other domains, POC→Pilot→Platform phases, early architectural boundary diagram (Synthetic Data between CI/CD, RapidBotz, and Performance tools), ownership boundaries, and early pilot scope & governance open questions. Good for Operating Model, System Boundaries, Non-Goals, and Open Questions.
Confidence: High
6. Enterprise AI-Augmented Testing with Synthetic Data Hub: Pilot Implementation and Governance Plan
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/4964909251/Enterprise+AI-Augmented+Testing+with+Synthetic+Data+Hub+Pilot+Implementation+and+Governance+Plan
Relevance: Strategic positioning and “Test Intelligence Stack” with a Six-Layer Test Intelligence Stack where Synthetic Data Hub is the foundation. Strong “architecture-at-a-glance” content, especially for layers/operating model and integration with DIRR/RapidBotz/CI/CD.
Confidence: High
7. Reducing Release Triage Noise with Synthetic Data Platform for Improved Efficiency
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/4985847933/Reducing+Release+Triage+Noise+with+Synthetic+Data+Platform+for+Improved+Efficiency
Relevance: Defines “North Star Problem”, capability statement, and System Boundary (Inside vs Outside Synthetic Data Platform). Good for Mission/Purpose, System Boundaries, and Non-Goals (not owning rating logic/business rules).
Confidence: High
8. Scenario Contract & Drift Governance Model (v0.1)
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/4985979045/Scenario+Contract+Drift+Governance+Model+v0.1
Relevance: Deep content on scenario contract governance, drift detection, ownership, and RapidBotz adapter boundary. Strong for Canonical Data/Drift Prevention Rules, Shared Responsibility, and failure-domain separation.
Confidence: High
9. Operator Runbook Lite: RapidBotz Dataset Execution Path and Failure Management
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/4986470668/Operator+Runbook+Lite+RapidBotz+Dataset+Execution+Path+and+Failure+Management
Relevance: Contains “Pilot Scope Boundary – v0.1” with explicit Pilot limits and explicit out-of-scope list; also describes deterministic seed enforcement, manifest logging, and execution/failure paths. Useful for Pilot Scope, Determinism rules, and guardrails.
Confidence: High
10. Synthetic Data Platform – 12-Month Guidewire Roadmap (PolicyCenter First, ClaimCenter Next)
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/4989157553/Synthetic+Data+Platform+12+Month+Guidewire+Roadmap+PolicyCenter+First+ClaimCenter+Next
Relevance: Roadmap framing, phased evolution, and risks when expanding canonical scope (ClaimCenter). Good context for invariants (keep canonical stable, don’t over-expand) and future-state system boundaries; less central to Phase 0 repo but useful as background.
Confidence: Medium
11. Enterprise Synthetic Data Hub (POC)
Link: https://csaaig.atlassian.net/wiki/spaces/MO/pages/4821287025/Enterprise+Synthetic+Data+Hub+POC
Relevance: POC-level architecture: system architecture overview, deterministic seed strategy (ADR-001), generator/CLI/API/exporters, golden snapshot tests, determinism and governance guarantees. Good for determinism & reproducibility rules; some content superseded by Pilot docs but still authoritative on technical principles.
Confidence: Medium (POC; some details may be superseded)
12. Synthetic Data Platform Pilot Readiness (Jira)
Link: https://csaaig.atlassian.net/browse/MOBRM-215
Relevance: Jira story that encapsulates Pilot readiness goals: canonical schema freeze, deterministic seed enforcement, adapter isolation, dataset lifecycle governance, explicit failure domains, pilot scope lock, and explicit “Out of Scope” list. Useful for constraints, invariants, and Pilot discipline guardrails.
Confidence: High
13. Formalize Six-Layer Architecture Map (Jira)
Link: https://csaaig.atlassian.net/browse/MOBRM-216
Relevance: Confirms intent to formalize a Six-Layer Architecture Map (Infrastructure, Data, Governance, AI, Integration, Business Alignment) and produce an “Architecture at a Glance” diagram. No full map text here, but reinforces the layered architecture framing from the Pilot Governance Plan.
Confidence: Medium (meta-artifact, not full content)
14. Pilot Scope Lock (Jira)
Link: https://csaaig.atlassian.net/browse/MOBRM-222
Relevance: Jira backing the scope lock work: “Explicitly limit: Entities, Consumers, Environments, Integration pathways.” Supports and aligns with the Confluence Pilot Scope Lock page.
Confidence: High (but brief)
15. Synthetic Data POC (Jira)
Link: https://csaaig.atlassian.net/browse/MOBRM-68
Relevance: Summarizes POC scope, what’s in/out, determinism guarantees, and acceptance criteria. Some content overlaps with the POC Confluence page. Good for explicit non-goals (no prod, no PII, limited entities) and core determinism/guardrail statements.
Confidence: Medium
16. Synthetic Data Creation Pilot (older Jira)
Link: SEM-7946: Synthetic Data Creation PilotOn Hold
Relevance: Earlier, more generic synthetic data effort (data science + testing). Likely outdated relative to the current Synthetic Data Hub and Pilot. Only relevant historically; not recommended as source for Arcus repo baseline.
Confidence: Low and Outdated

## SECTION 2 — Consolidated Repo-Ready Summary

I’ll separate Confirmed Facts (directly stated) vs Inferred Summary (tight synthesis consistent with sources, but not literally quoted).
Mission / Purpose
Confirmed Facts
The Synthetic Data Pilot “establishes a governed, deterministic, and auditable way to generate test data scenarios for QA, automation, and future AI-driven testing across Guidewire applications.”
– Source: Synthetic Data Hub — Pilot Confluence Space
Capability focus is to “reduce release triage noise” by introducing “deterministic, governed dataset generation” and to “eliminate environment data drift in QA cycles.”
– Sources: Reducing Release Triage Noise page; Pilot Scope Lock – Synthetic Data Platform (Phase 1)
Capability statement (triage/efficiency framing):
“This capability exists to reduce release triage noise by generating deterministic, governed synthetic datasets that eliminate non-reproducible failures across environments.”
– Source: Reducing Release Triage Noise page
Capability statement (governance framing):
“This capability exists to enable deterministic, governed synthetic dataset generation for QA, automation (RapidBotz), performance testing, and future AI use cases with strong auditability and reproducibility guarantees.”
– Source: Governance Foundation & Trust Boundary page
Inferred Summary
The Arcus/Synthetic Data Hub operating system exists to treat test data as governed infrastructure: deterministic, policy-controlled synthetic scenarios that stabilize QA/automation by removing data randomness and drift as sources of failure.
Pilot Scope
Confirmed Facts
From Pilot Scope Lock – Synthetic Data Platform (Phase 1):
Business Objective:
“Reduce regression triage noise and eliminate environment data drift in QA cycles by enforcing deterministic synthetic data governance within a tightly controlled business lane.”
Locked Business Lane:
Commercial Auto – New Business transaction within PolicyCenter.
Strictly limited to:
Single Gig Economy driver
One vehicle
Deterministic seed-based dataset generation
Golden snapshot reproducibility
Explicitly no: endorsements, renewals, fleet scenarios, multi-vehicle expansion.
Canonical Data Mutation Policy (Pilot Phase):
Canonical model changes must go through formal review.
RapidBotz/QA tweaks cannot bypass seed determinism.
No environment-specific overrides.
All dataset variations must be seed-derived, not manually altered.
Any requested expansion triggers a scope review.
From Operator Runbook Lite – Pilot Scope Boundary – v0.1:
✅ Limited To:
1 consuming application (RapidBotz + Guidewire path)
1 LOB (Basic Auto)
1–3 foundational “Tier 1” scenarios
1–2 environments (e.g., Dev2 + QA)
Deterministic seed enforcement
Manifest audit logging
🚫 Explicitly Out of Scope:
Multi-application canonical expansion
MyQuote integration
Claims/Billing models
AI-assisted auto-generation expansion
Large scenario library growth
Enterprise marketplace features
Inferred Summary
Phase 0/Phase 1 Pilot is a single-lane, single-consumer, low-scenario-count experiment targeting Commercial Auto New Business in PolicyCenter, wired to RapidBotz in 1–2 lower environments, with hard limits on scope expansion and scenario volume.
Explicit Non-Goals
Confirmed Facts
Across Pilot and POC docs:
Not masked production data.
Not uncontrolled AI-generated data.
Not a replacement for business logic validation or unit tests.
Not a one-off testing tool or production service.
Not an enterprise data platform or ML training pipeline.
Pilot explicitly does not:
Expand to ClaimCenter, BillingCenter, other Guidewire apps.
Perform multi-application hydration.
Introduce multi-application adapters.
Enable runtime or autonomous canonical schema mutation.
Provide automated rollback or long-running AI agents.
– Sources: Pilot overview; Synthetic Data POC Jira; Pilot Readiness Jira; Operator Runbook Pilot Scope; Roadmap page.
Inferred Summary
The system intentionally avoids production data, AI-driven generation, and broad platform responsibilities. During Phase 0/Phase 1 it is not about scale, realism, or multi-domain coverage; it is about governance, reproducibility, and pilot-grade value proof.
Architecture Layers
Confirmed Facts
From Enterprise AI-Augmented Testing with Synthetic Data Hub — Test Intelligence Stack:
Layer 6 – Release Governance & Risk Visibility
Layer 5 – DIRR / AI Test Intelligence
Layer 4 – RapidBotz / API Automation
Layer 3 – Performance Tooling
Layer 2 – DevOps CI/CD
Layer 1 – Unit Testing
FOUNDATION – Synthetic Data Hub
From Reducing Release Triage Noise – System Boundary:
Inside Synthetic Data Platform: scenario contracts, seed-based generation engine, contract validation, manifest generation, artifact hashing, S3 storage, dataset registry, audit logging, version control.
Outside: Guidewire apps, RapidBotz, CI/CD, Jira, business logic engines, environment runtime configuration.
Principle: Synthetic Data Platform does not own rating logic or business rules.
From P0/Pilot Integration Mapping – Architectural Boundary Diagram:
CI/CD Pipeline
↓
[ Synthetic Data Platform ]
↓
[ RapidBotz Automation ]
↓
[ Performance Tool (TBD) ]
↓
Quality Gates
From Scenario Contract & Drift Governance Model – Adapter Boundary:
Explicit RapidBotz → Adapter → Synthetic Data Hub pattern, with Adapter owning translation and governance enforcement.
Inferred Summary
Arcus/Hub sits as a deterministic data foundation under a multi-layer Test Intelligence stack:
Foundation: Synthetic Data Hub (canonical model, generator, governance & telemetry).
Layer 1–2: Unit tests and CI/CD use deterministic fixtures/datasets.
Layer 3–4: Performance tools and RapidBotz/API automation consume governed datasets via adapters.
Layer 5–6: DIRR/AI and release governance rely on traceable, reproducible synthetic data contracts.
Trust Boundaries
Confirmed Facts
From Governance Foundation & Trust Boundary (Pilot Preparation):
Trust Boundary Location: AWS IAM Role.
Execution Role: ScenarioGeneratorRole (name TBD).
Only members of SyntheticDataGenerators IAM group can generate; not broad DevOps.
Governance Layers table: IAM boundary, Registry, Git Hash, Deterministic Seed, Golden Snapshot Tests.
Dataset Registry stores metadata only (Scenario ID, git hash, risk classification, owner, approval, pointers to manifests/URIs); does not store full datasets.
From Trust Boundary & Ownership Model – Pilot Phase:
Canonical synthetic model not editable by QA, RapidBotz, or environments.
Usage plane (QA, RapidBotz, CI/CD) can request but cannot mutate canonical definitions.
Non-negotiable boundary: Pilot has zero ability to impact Production systems; no write access to prod data stores; impact limited to non-prod synthetic artifacts and test stability.
From Scenario Contract & Drift Governance Model – RapidBotz Adapter:
RapidBotz submits dataset requests only to an Adapter; never transforms formats or embeds scenario rules.
Adapter validates and normalizes to canonical Scenario Definition Contract, enforces limits, and clearly fails invalid requests.
Synthetic Data Hub only generates data from canonical contract and returns manifest references.
Inferred Summary
Phase 0/Phase 1 positions the trust boundary at:
Infrastructure level: AWS IAM role(s) gating generator execution.
Logical level: Canonical model and Scenario Definition Contracts not directly writable by consumers; interaction strictly via adapters/reg contracts.
Environment level: No production write paths; blast radius limited to non-prod test data and tools.
Shared Responsibility
Confirmed Facts
From Scenario Contract & Drift Governance Model (v0.1):
Synthetic Data Platform owns: contract validation, drift detection, version control, audit logging.
Application teams own: business rule accuracy, schema change communication, required contract updates.
RapidBotz: dataset requester only; no embedded generation logic or rule changes.
Scenario metadata requires both business and technical owners; no owner → cannot activate.
From Trust Boundary & Ownership Model – Pilot Phase:
Canonical synthetic model: accountable owner = Synthetic Data Platform Owner.
Change review group (Platform Owner + QA + optional DevOps + SMEs) evaluates canonical expansions.
From Pilot Readiness Jira:
Explicit failure domains:
Canonical schema → Synthetic Data owner
Adapter mapping → Adapter owner
Test failures → QA
Environment drift → DevOps
Inferred Summary
Ownership is sharply split:
Platform/Arcus: Canonical model, generator logic, drift controls, registry, audit, determinism.
Adapters: Application-specific mapping and integration, but not canonical semantics.
Application teams: Business correctness and communication of schema/rule changes.
QA/Automation teams: Test design, suite stability, proper use of deterministic data.
DevOps: Environment health and drift outside the data platform.
Canonical Data / Drift Prevention Rules
Confirmed Facts
From Pilot Scope Lock – Canonical Data Mutation Policy:
All canonical model changes must go through formal review.
No environment-specific overrides; no direct tweaks bypassing seeds.
All dataset variations must be derived from seed; no manual post-generation edits.
From Governance Foundation & Trust Boundary – Reproducibility Model:
Reproducibility requires:
Fixed deterministic seed
Fixed logic state (git commit hash)
Fixed schema version
Controlled execution boundary (IAM)
Deterministic seed alone is insufficient; all components must be fixed to prevent drift.
From Scenario Contract & Drift Governance Model:
Scenario state management (Active, Failed-Drift, Deprecated).
Drift escalation: failing validation moves a scenario to Failed-Drift, blocks usage, notifies owners.
Retirement triggers and actions ensure retired scenarios can’t silently drift back into use.
From Roadmap & Triage Noise pages:
Canonical growth during Pilot is intentionally constrained to avoid canonical over-expansion and instability.
Explicit ADR requirement for canonical changes.
Inferred Summary
Drift prevention is implemented as a combination of:
Contract governance (Scenario Definition Contracts + states).
Strong immutability references (seed + schema version + git hash logged and required).
IAM-bounded execution and registry-only metadata plane.
Policy that any canonical evolution requires reviewed ADRs and explicit version bumps.
Deterministic or Reproducibility Rules
Confirmed Facts
From Enterprise Synthetic Data Hub (POC):
ADR-001: Deterministic Seed Strategy uses a fixed seed (e.g., 20251101) as baseline anchor.
Same input (seed) must produce the same outputs; changes require golden snapshot regeneration.
Seed is central to reproducibility, but trade-offs in randomness vs realism are known and mitigated with flags.
From Pilot Readiness Jira:
Seed + canonical version logged with every generation and included in manifest.
“Same seed + same canonical version produces identical persona output”; replay validated and documented.
If replay fails, Pilot is considered unstable.
From Operator Runbook / RapidBotz Execution Path:
Request payload includes seed, scenario_key, contract_version, etc.
Hub executes deterministic, seed-based generation, computes hashes, and creates manifests.
Deterministic seed enforcement is a Pilot requirement; success criteria include 100% reproducibility and hash match.
Inferred Summary
Determinism is defined as:
For a given (canonical schema version, git commit, scenario definition, seed), dataset outputs and hashes must be identical across runs and environments.
All operational paths (RapidBotz, CLI, etc.) must propagate and log seeds and versions to allow exact replay.
Key Constraints / Invariants
Confirmed Facts
Pilot must have zero ability to impact Production systems; no prod write access.
Canonical model is not directly mutable by QA, RapidBotz, or environments.
Synthetic Data Platform does not own application rating logic or business rules.
Only members of SyntheticDataGenerators group can assume the execution role; registry is metadata-only.
Pilot scope: single PolicyCenter lane, single consuming application, tightly limited entities and scenarios.
No autonomous or runtime schema mutation allowed in Pilot.
No additional application adapters introduced during Pilot.
– Sources: Trust Boundary & Ownership Model, Governance Foundation, Pilot Scope Lock, Pilot Readiness.
Inferred Summary
Phase 0 invariants are:
Strong separation between canonical model and consumers.
Strict, IAM-enforced generation boundary.
Determinism and traceability are non-negotiable; any violation is considered Pilot failure.
Scope and scenario count remain intentionally small until governance patterns are proven.
Open Questions / Ambiguities
Confirmed Facts (explicit “Open Questions” sections)
From multiple planning pages (POC→Pilot Planning, Pilot Governance, Roadmap):
Who formally owns the Dataset Registry and where it physically lives (DynamoDB vs RDS vs Confluence + API)?
What is the formal approval workflow tool (Jira vs ServiceNow vs Git PRs)?
What defines High vs Moderate business impact for scenarios?
Whether dataset generation should be automatic per pipeline run vs manually triggered.
Whether and how seeds and dataset versions should be embedded in test artifacts, Jira, Xray, etc.
Where large performance datasets should be stored and who owns cleanup.
Whether Synthetic Data is considered infrastructure vs a feature.
Exact success metrics and SLAs for drift remediation, scenario portfolio governance, and telemetric thresholds.
Inferred Summary
Open items primarily concern implementation details of the control plane (registry backing store, workflow tooling), operational integration (CI/CD patterns, logging), and governance severity tiers (risk classifications, escalation paths). These should be tracked as Phase 0/ADR open questions in the repo.

## SECTION 3 — Repo Mapping Recommendation

For each target file: what goes in, what stays out, and which Confluence/Jira sources to lean on.
1. docs/project_context.md
Should Contain (Confirmed + Inferred)
Mission / Purpose (short, non-marketing): governed, deterministic, auditable synthetic datasets to reduce regression triage noise and environment drift, and to underpin Test Intelligence.
North Star Problem & Outcomes: 50% triage reduction; elimination of non-reproducible data failures.
High-Level Scope Summary: Commercial Auto New Business lane, single consumer (RapidBotz), 1–2 environments.
Explicit Non-Goals (bulleted): Not production, not AI generator, not rating logic owner, etc.
Relationship to NextGen / Test Intelligence Stack: one paragraph referencing the layered stack and where Synthetic Data fits.
Best Source Inputs
Synthetic Data Hub — Pilot Confluence Space
Reducing Release Triage Noise page
Enterprise AI-Augmented Testing with Synthetic Data Hub: Governance Plan
Pilot Scope Lock – Synthetic Data Platform (Phase 1)
Should NOT Contain
Low-level architecture diagrams or trust boundary details.
IAM role names, S3 paths, or runbook procedures.
Per-tool integration specifics (RapidBotz adapter payloads).
2. docs/architecture/architecture_at_a_glance.md
Should Contain
Six-Layer Test Intelligence Stack diagram/text with Synthetic Data Hub as foundation (as-is terminology).
System Boundary & Flows:
CI/CD → Synthetic Data Platform → RapidBotz → Performance Tool → Quality Gates diagram (simplified).
Inside vs Outside Synthetic Data Platform list (contracts, generator, registry vs Guidewire apps, RapidBotz, CI/CD).
Core Components (brief): Generator, canonical model, adapters, registry, manifests, telemetry.
Phase 0 View: That this is currently realized as a single PolicyCenter lane + RapidBotz adapter.
Best Source Inputs
Enterprise AI-Augmented Testing Governance Plan (Test Intelligence Stack)
POC → Pilot Planning & Integration Mapping
Reducing Release Triage Noise (System Boundary)
Enterprise Synthetic Data Hub (POC) – System Architecture section
Should NOT Contain
Detailed trust boundary/IAM policies (leave to trust_boundaries.md).
Scenario governance workflow states in detail (leave to guardrails/governance docs).
ADR-style decision rationales (leave to ADR file).
3. docs/architecture/trust_boundaries.md
Should Contain
Explicit Trust Boundary Definition:
IAM-enforced execution role (ScenarioGeneratorRole), SyntheticDataGenerators group, no prod write access.
Separation of Control Plane (canonical, registry, logging) vs Usage Plane (QA, RapidBotz, CI/CD).
Blast Radius Definition: Non-prod only, synthetic artifacts only, test execution stability only.
Dataset Registry Model at Boundary: Metadata-only registry, pointers to artifacts, no raw data.
Interaction Model: RapidBotz → Adapter → Hub and how this preserves boundaries.
Best Source Inputs
Governance Foundation & Trust Boundary (Pilot Preparation)
Trust Boundary & Ownership Model – Pilot Phase
Scenario Contract & Drift Governance Model (adapter boundary)
Operator Runbook Lite (execution path, but only the boundary aspects)
Should NOT Contain
Detailed ownership/responsibility matrix (go to shared_responsibility.md / guardrails).
Roadmap or success metrics.
4. docs/architecture/shared_responsibility.md
Should Contain
Responsibility Matrix:
Synthetic Data Platform owner, Adapter owner, Application teams, QA, DevOps.
Per-Domain Accountability:
Canonical schema integrity, drift detection, dataset lifecycle, test failures, environment drift.
Scenario Ownership Model: required metadata (business owner, technical owner, review cadence, etc.).
Change Review Group Description: how canonical changes are evaluated.
Best Source Inputs
Scenario Contract & Drift Governance Model (ownership + escalation)
Trust Boundary & Ownership Model – Pilot Phase
Pilot Readiness Jira (explicit failure domains)
Should NOT Contain
IAM or network/security plumbing (that’s a trust boundary/infra doc).
Detailed seed strategy (belongs with determinism/ADR/guardrails).
5. docs/guardrails.md
Should Contain
Pilot Scope Guardrails:
From Pilot Scope Lock page + Operator Runbook Pilot Scope Boundary.
In/out of scope lists preserved nearly verbatim.
Canonical Mutation Guardrails:
“No environment-specific overrides”; “seed-derived only”; “no autonomous schema mutation”.
Scenario Portfolio Guardrails: tier model (Tier 1/2/3), retirement policies, drift lifecycle (Active → Failed-Drift → Deprecated).
Risk & Anti-Patterns: second-order risk of scenario sprawl and canonical instability; requirement for ADRs for canonical expansion.
Best Source Inputs
Pilot Scope Lock – Synthetic Data Platform (Phase 1)
Operator Runbook Lite (Pilot Scope Boundary, retirement, scenario sprawl risk)
Scenario Contract & Drift Governance Model (scenario lifecycle and escalation)
Pilot Readiness Jira (Pilot Guardrails, Out-of-Scope list)
Should NOT Contain
Detailed operational runbooks; those belong in a separate runbooks/ or ops-focused docs.
Architecture diagrams or layered stack; point to architecture docs instead.
6. docs/decisions/ADR-0003-phase-0-architecture-baseline.md
Should Contain
Scope of ADR: Phase 0 / Pilot architecture baseline only (not long-term target).
Decisions (each tied to sources):
Use Synthetic Data Hub as deterministic foundation under the Test Intelligence Stack.
Place trust boundary at IAM role + canonical control plane, with metadata-only registry.
Adopt RapidBotz → Adapter → Hub integration model; no direct Tool→Hub calls.
Lock Pilot scope: single lane (Commercial Auto New Business), single consumer (RapidBotz), limited entities and scenarios, 1–2 environments.
Enforce determinism via seed + canonical version + git hash + manifest logging.
Disallow autonomous schema mutation and multi-application adapters for Phase 0.
Consequences:
Limits scale and flexibility in Pilot but maximizes governance and traceability.
Provides a clean baseline for future ADRs on expansion (ClaimCenter, AI, etc.).
Open Questions:
Registry implementation choice, approval tooling, CI triggers, risk tier definitions, etc. (pulled straight from “Open Questions” sections).
Best Source Inputs
Pilot Readiness Jira (explicit acceptance criteria & guardrails)
Enterprise AI-Augmented Testing Governance Plan (Test Intelligence Stack, positioning)
Governance Foundation & Trust Boundary (repro model, registry)
Scenario Contract & Drift Governance Model (integration and drift handling)
Pilot Scope Lock – Synthetic Data Platform (scope, canonical policy)
Should NOT Contain
Step-by-step operational details or runbooks.
Detailed future roadmap; mention only as implications or follow-on ADR references.

### Source Inventory Table (Generated via Pandas)
|   ID | Source                                      | Confidence   |
|-----:|:--------------------------------------------|:-------------|
|    1 | Synthetic Data Hub — Pilot Confluence Space | High         |
|    2 | Pilot Scope Lock – Phase 1                  | High         |