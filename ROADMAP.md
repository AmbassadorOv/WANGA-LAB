# WANGA-LAB — Insurer Intake Readiness Roadmap

## Purpose

Prepare the WANGA-LAB evidence service to handle an initial return of up to 10 insurance-company prospects without confusing market response with operational capacity.

The readiness target is not "10 contracts at once." The target is a controlled intake system that can receive, classify, scope, preserve, analyze, and verify multiple cases while keeping evidence status explicit.

## Operating Gate

`PROSPECT → INTAKE → SCOPE → EVIDENCE PACKAGE → REPLAY → ANALYSIS → VERIFICATION → CLIENT REPORT`

No client case is treated as verified merely because intake is complete.

## Capacity model

### Tier 0 — Commercial response

Handle up to 10 returning companies at the conversation/intake level.

Required:
- standard intake questionnaire
- service-scope statement
- evidence requirements
- clear statement of what WANGA-LAB does and does not provide
- case reference assignment

### Tier 1 — Technical triage

Accept only cases that have enough material for reproducible analysis.

Classify each case:
- READY_FOR_REPLAY
- NEEDS_EVIDENCE
- NEEDS_SCOPE
- OUT_OF_SCOPE
- PENDING_CLIENT_ACCESS

### Tier 2 — Active forensic cases

Do not activate all 10 cases simultaneously by default.

Each active case receives:
- immutable case reference
- baseline/evidence manifest
- provenance record
- replay status
- analysis status
- verification status
- owner and next action
- explicit blockers

Initial operational target: maintain a small verified working set while the remaining cases stay in controlled intake.

### Tier 3 — Verified deliverable

A case can be published as verified only when the required replay/evidence checks pass.

Status vocabulary:
- BUILT
- SPECIFIED
- PROTOTYPED
- TESTED
- VERIFIED
- PLANNED
- HYPOTHETICAL

Rule: specification is never presented as implementation; prototype is never presented as verified.

## First empirical artifact

Primary case package:

`artifacts/drift-known-risk-001/`

Minimum contents:
- `README.md`
- `case.yaml`
- `evidence-manifest.json`
- `replay/`
- `outputs/`
- `verification/`

The artifact is the reference pattern for future insurer cases.

## Intake fields

Every prospect/case should capture:
- client reference
- business domain
- system/model under examination
- claimed or observed drift
- observation period
- available baseline
- available outputs
- provenance availability
- replay availability
- external evidence dependencies
- confidentiality/access constraints
- requested deliverable
- target date
- current gate/status

## Operational controls

Before accepting concurrent client work, verify:
1. case isolation
2. evidence integrity
3. reproducible replay path
4. artifact naming and storage convention
5. audit trail
6. report template
7. escalation/blocker handling
8. verification checklist
9. client-facing scope boundaries
10. no cross-client evidence leakage

## 72-hour response pattern

When a qualified case enters intake:

**0–24h**
- assign case reference
- freeze supplied evidence manifest
- identify missing inputs
- classify scope

**24–48h**
- establish baseline
- execute or prepare deterministic replay
- record deviations
- preserve outputs

**48–72h**
- perform verification checks
- classify evidence state
- produce preliminary forensic finding or blocker report

The 72-hour pattern is an operational target for qualified cases, not a guarantee for every engagement.

## Readiness decision

If 10 companies return at once, the correct response is not to promise 10 simultaneous verified investigations.

The system should:
1. acknowledge all 10
2. run all 10 through intake
3. qualify and prioritize by evidence readiness and scope
4. activate a controlled number of forensic cases
5. keep the remainder in explicit queue states
6. expand concurrency only after replay, evidence handling, and verification remain stable

## Exit criteria for this roadmap

Ready for a first multi-prospect wave when:
- the primary empirical artifact exists
- replay has been executed
- verification output is reproducible
- intake schema exists
- case isolation is documented
- report/status templates exist
- GitHub CI/test state is green for the relevant artifact path

Ready for broader concurrency only after real case throughput demonstrates that the above controls remain stable under load.


## Integrated architecture links

The insurer intake layer now connects to the broader WANGA system through explicit interfaces:

WANGA OS → Global Work Manager → Model Fabric / Digital Model Agents → Runtime → Evidence & Provenance → Drift Forensics → Verification → Human Gate → Research / Publication

Operational components now present on main:
- Insurer intake triage
- Bounded case queue
- Forensic case pipeline
- Machine-readable intake CLI
- Remote oversight report
- Daily read-only operations report
- Deterministic synthetic replay fixture
- Global Drift Network observation/evidence structures
- Vitruvius research index
- WANGA-X research foundation
- Global Work Manager / Model Fabric contracts

The daily operations layer is **READ_ONLY_REPORT**. It does not auto-promote evidence, merge code, or replace the human verification gate.
