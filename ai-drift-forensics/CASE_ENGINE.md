# AI Drift Forensics — Case Engine

## Purpose

The Case Engine is the structured case-management layer for AI Drift Forensics. It turns a forensic investigation from a collection of notes into a reproducible evidence object with explicit provenance, state transitions, attribution, and verification.

This is a research and engineering framework. It is not a legal certification system, regulatory determination, insurance-coverage determination, or claim that an incident occurred.

## Core object

`ForensicCase` represents one bounded investigation.

Required case properties:

- `case_id` — stable identifier.
- `title` — concise case title.
- `status` — lifecycle state.
- `scope` — system, environment, period, and questions under examination.
- `cards` — structured evidence cards.
- `claims` — propositions being tested.
- `chain_of_custody` — evidence handling history.
- `verification` — reproducibility and independent-review record.

## Case lifecycle

`INTAKE → SCOPED → BASELINED → OBSERVING → DRIFT_DETECTED → EVIDENCE_PRESERVED → RECONSTRUCTING → ATTRIBUTING → VERIFYING → CLOSED`

A case may also enter `UNRESOLVED` when available evidence cannot support a conclusion. Closure does not imply that a hypothesis was confirmed.

## Evidence-state lifecycle

`DECLARED → OBSERVED → CAPTURED → PRESERVED → REPRODUCED → INDEPENDENTLY_VERIFIED`

These states must not be conflated. A provider statement, analyst hypothesis, captured artifact, reproduced result, and independent verification are different evidentiary classes.

## Case workflow

### 1. Intake

Record the question without prematurely deciding its answer.

Examples:

- What changed?
- When did the change become observable?
- Which system boundary is in scope?
- Can the relevant state still be reconstructed?

### 2. Baseline

Freeze or document the comparison state before interpreting deviation.

Baseline dimensions may include:

- model/version/weights where observable;
- prompts and policies;
- routing and agent configuration;
- data characteristics;
- tools and APIs;
- deployment environment;
- dependency versions;
- operational metrics;
- timestamps and clocks;
- relevant external conditions.

### 3. Detection

Record the measured deviation and its measurement method. Do not label a deviation as causal merely because it correlates with a change.

### 4. Preservation

Create evidence records with provenance, acquisition time, source, integrity metadata, and custody events.

### 5. Reconstruction

Build a time-ordered event graph connecting observed system states, changes, outputs, dependencies, and interventions.

### 6. Attribution

Separate:

- observed association;
- dependency relationship;
- temporal precedence;
- experimentally reproduced effect;
- causal conclusion.

Attribution must identify uncertainty and competing explanations.

### 7. Verification

A verification record should state:

- what was tested;
- by whom;
- with which artifacts;
- under which environment;
- whether reproduction succeeded;
- what remains unresolved;
- whether the reviewer was independent of the original analysis.

## Evidence graph

The canonical relationship model is:

`SYSTEM → ENVIRONMENT → MODEL / DATA / CONFIGURATION / DEPENDENCY → EVENT → OBSERVATION → EVIDENCE → RECONSTRUCTION → ATTRIBUTION → RISK INDICATOR → INTERVENTION → VERIFICATION`

This graph is descriptive infrastructure. It does not itself establish legal liability or financial loss.

## Claim discipline

Every material claim should carry a fact class:

- `OBSERVED`
- `REPORTED`
- `DERIVED`
- `HYPOTHESIS`
- `VERIFIED`
- `REFUTED`
- `UNRESOLVED`

A `HYPOTHESIS` cannot silently become `VERIFIED` through repetition. A `REPORTED` statement is not equivalent to an independently observed fact.

## Synthetic case requirement

Development examples must use synthetic identifiers and simulated events unless a real case has been explicitly authorized for repository inclusion. Do not place credentials, personal data, confidential customer information, proprietary model weights, or sensitive institutional evidence in the public repository.

## 72-hour integration

The Case Engine is designed to support the 72-Hour Evidence Challenge:

`BASELINE → CONTROLLED DRIFT → DETECTION → RECONSTRUCTION → ATTRIBUTION → VERIFICATION`

The challenge measures forensic readiness rather than declaring an organization compliant or non-compliant.

## Design objective

The engineering objective is simple:

> Make it harder to make an unsupported claim and easier to reproduce a supported one.
