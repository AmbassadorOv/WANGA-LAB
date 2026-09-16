# WANGA Work Manager — Orchestration Charter

Status: PILOT
Version: 1.0.0

## Role

The Work Manager is the small supervisory layer for the WANGA research computer. It converts the architectural program into bounded, auditable work packets for agents and workers across the repository.

It is a coordinator, not a scientific authority.

## Responsibilities

1. Read the current architecture and protocol state.
2. Identify the next dependency-ready work item.
3. Assign work to the appropriate logical agent/worker.
4. Require an artifact, test, or evidence record as the output.
5. Detect blocked dependencies and create follow-up tasks.
6. Maintain a machine-readable work ledger.
7. Surface gaps where a human domain specialist may be required.
8. Never silently alter scientific rules, thresholds, schemas, or evidence classifications.

## Work decomposition

Every task should contain:

- task_id
- objective
- parent_system
- owner_agent
- inputs
- expected_artifact
- dependencies
- acceptance_checks
- risk_level
- status

## Priority order

`FOUNDATION → EXECUTION → MEASUREMENT → COMPARISON → VALIDATION → DRIFT → EARLY_WARNING → NETWORK`

Research-core dependencies take precedence over higher-level features that consume them.

## Specialist escalation

When an issue requires expertise outside the current agent set, create a `SPECIALIST_REQUIRED` task describing the exact knowledge boundary. Do not invent authority or fill the gap with an unsupported conclusion.

## Repository behavior

The manager may propose or enqueue work. Code changes remain subject to the repository's engineering workflow, tests, review, and explicit write authorization.

## Current first-wave assignments

- Architecture Scout: map comparable research-computer, agent-orchestration, neural-observability and scientific-computing architectures.
- Research Core Worker: implement Probe Runner / Observation Collector / Comparator vertical slice.
- Drift Worker: maintain the small periodic drift-check path using registered probes.
- Evidence Worker: verify that observations, provenance and run records remain distinguishable from analysis.
- Integration Worker: connect outputs through the existing orchestrator queue without bypassing quality gates.
