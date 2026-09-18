# WANGA Global Work Manager / Orchestrator V2

Status: BUILD SPECIFICATION
Version: 2.0.0

## Master instruction inheritance

This manager and every subordinate manager operate under the canonical project control contract:
`docs/MASTER_PROJECT_INSTRUCTIONS_V1.md`.

The Master Project Instructions are inherited, not optional. The Global Work Manager is responsible for enforcing them across the manager hierarchy. The priority engine is P0 system integrity → P1 Rational Logic → P2 verification → P3 NTM+Rational Logic+Evidence → P4 Model Fabric → P5 Perspective scale → P6 commercialization → P7 presentation.

## Purpose

Extend the existing WANGA Work Manager and Global Drift Research Orchestrator into one repository-wide supervisory control plane. This is an extension of the existing orchestration layer, not a competing orchestrator.

The manager coordinates the complete WANGA architecture:

WANGA OS -> Global Work Manager -> subsystem workers / Model Fabric / Digital Model Agents / Research Groups / Runtime -> Evidence & Drift Forensics -> Rational Logic (when required) -> Verification -> NTM -> Work Memory -> publication / review queues.

## Global operating loop

CONTEXT -> INSPECT -> CLASSIFY -> PRIORITIZE -> PLAN -> EXECUTE -> TEST -> VERIFY -> RECORD -> INTEGRATE -> SELF-AUDIT -> NEXT ACTION

No manager task may skip INSPECT, TEST, VERIFY, or RECORD when those stages are applicable.

## Scope

The manager coordinates:
- WANGA OS and runtime
- Research Groups and specialized workers
- Model Fabric and Digital Model Agents
- NTM routing/escalation
- Drift Forensics and evidence
- Rational Logic formal reasoning
- Knowledge connectors and ARK runtime
- Virtual GPU / nano runtime
- Algorithmic Governance interfaces
- Wix publication/integration queues
- autonomous architecture construction
- durable Work Memory
- bank/investor technical-data-room alignment

It does not replace domain logic inside these systems.

## Single coordination rule

There is one global work-management authority: the existing WANGA Work Manager / Orchestrator, extended by this V2 contract.

Domain orchestrators may remain as bounded local coordinators, but they must expose work through the global task envelope and cannot create an independent global queue or authority.

## Work lifecycle

INTAKE -> NORMALIZE -> DECOMPOSE -> DEPENDENCY_SCAN -> PRIORITIZE -> ROUTE -> EXECUTE -> COLLECT -> VERIFY -> UPDATE_MEMORY -> FOLLOW_UP

Terminal states:
COMPLETE | BLOCKED | CONFLICT | REVIEW_REQUIRED

No failed task is converted into COMPLETE without verification.

## Evidence and status discipline

Managers must distinguish:
OBSERVATION | RAW_EVIDENCE | NORMALIZED_DATA | DERIVED_METRIC | INFERENCE | HYPOTHESIS | PROPOSED_CHANGE | VERIFIED_RESULT | CONFLICT.

Execution success is not proof. Model output is not proof. Correlation is not causation. Temporal sequence is not causal proof.

## Task classes

ARCHITECTURE, RESEARCH, MODEL_DISCOVERY, MODEL_BINDING, RUNTIME, DRIFT_FORENSICS, EVIDENCE, VERIFICATION, RATIONAL_LOGIC, NTM_ESCALATION, GOVERNANCE_INTERFACE, PUBLICATION, MAINTENANCE, AUTOBUILD, COMMERCIALIZATION_INTERFACE.

## Dependency policy

A task is dependency-ready only when all declared prerequisites are COMPLETE or explicitly accepted as non-blocking.

Priority considers:
1. blocking impact
2. architecture criticality
3. evidence quality
4. verification readiness
5. regression risk
6. age / retry count

Priority is a routing signal, not a scientific conclusion.

## Authority boundaries

The manager may inspect state, create bounded task plans, route work, collect results, record failures, and request verification.

The manager must not:
- push directly to main
- delete, disable, or rewrite preserved branches
- invent models, endpoints, capabilities, evidence, valuations, revenue, or credentials
- silently modify schemas or thresholds
- bypass verification
- merge its own pull requests
- replace the NTM decision gate
- replace the existing Work Manager with another global orchestrator
- turn a future financing scenario into present cash, revenue, collateral, or guaranteed value

## Model Fabric integration

The 5,000 model slots are architectural identities. The manager may route only to candidates that satisfy the Model Agent lifecycle and verification contracts.

DISCOVERED -> CONFIGURED -> VERIFIED -> ENABLED

An UNBOUND or unverified slot cannot receive production work.

## Rational Logic integration

The manager may route work through the Rational Logic layer when a task requires formal premise/rule/relation evaluation. Rational Logic does not replace the manager, DMA, Evidence, or NTM. It receives declared evidence/context and returns explicit reasoning status, contradiction findings, missing-premise findings, and verification requirements. A task may explicitly record Rational Logic as NOT_REQUIRED.

The next major research priority is executable Rational Logic, including syntax, semantics, inference, contradiction handling, incomplete-premise handling, deterministic tests, counterexamples, and formal interfaces.

The manager must not treat a model-generated answer as a proof merely because an agent framework executed successfully.

## NTM integration

The manager routes bounded tasks and verified evidence to the NTM. The NTM is the high-level cognitive CPU and escalation/verification layer; it is not an unrestricted executor.

## Work Memory integration

Every cycle records:
- observed state
- selected work
- dependencies
- changes
- tests
- verification
- blocked/conflict state
- next action

Work Memory is the resume point, not an authority that overrides repository evidence.

## Manager hierarchy

GLOBAL WORK MANAGER
|
+-- OS / Runtime Manager
+-- Research Manager
+-- Model Fabric Manager
+-- Digital Model Agent Manager
+-- Runtime Adapter Manager
+-- Drift Forensics Manager
+-- Evidence & Provenance Manager
+-- NTM / Cognitive Routing Manager
+-- Governance Interface Manager
+-- Publication / Wix Manager
+-- Autonomous Build Manager
+-- Work Memory Manager

All subordinate managers inherit the Master Project Instructions and report through the single Global Work Manager.

## Failure and conflict handling

FAIL -> RECORD -> RETRY or ALTERNATE_ROUTE -> VERIFY

CONFLICT -> PRESERVE_BOTH_STATES -> BLOCK_PROMOTION -> REVIEW_REQUIRED

The manager never guesses through an architectural conflict.

## Global cycle

SNAPSHOT -> HEALTH_SCAN -> WORK_MEMORY_SYNC -> DEPENDENCY_GRAPH -> PRIORITY_QUEUE -> ROUTE -> EXECUTE -> EVIDENCE -> VERIFY -> MEMORY_CHECKPOINT -> NEXT_QUEUE -> SELF_AUDIT

The cycle may be run in dry-run mode. Execution adapters remain separate from planning.

## Final review

Autonomous construction may prepare and validate changes, but final architecture review remains outside the autonomous manager.