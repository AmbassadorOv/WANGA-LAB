# Global Drift Event Engine

Status: research implementation specification.

## Purpose

Convert a documented global event into a reproducible set of drift-observation jobs. The engine does not decide what happened; it creates measurement work, preserves provenance, and routes results into the propagation graph.

## Event lifecycle

`REGISTERED → BASELINE_PENDING → BASELINED → OBSERVING → CHANGE_SCAN → SIGNATURE_BUILD → RELATIONSHIP_SCAN → VERIFICATION_PENDING → COMPLETE`

Failure states: `BLOCKED`, `UNRESOLVED`, `RETRY_PENDING`.

## Trigger classes

- ELECTION
- PUBLIC_INFORMATION_EVENT
- POLICY_EVENT
- MARKET_EVENT
- INFRASTRUCTURE_EVENT
- MODEL_RELEASE
- OTHER_DOCUMENTED_EVENT

Elections are one trigger class, not the definition of the network.

## Observation dimensions

Every generated observation job declares:

`TIME × GEOGRAPHY × LANGUAGE × SURFACE × PROBE × BASELINE`

Surfaces:

- `AI_MODEL`
- `SEARCH`
- `NEWS_PUBLIC_INFO`
- `OTHER`

## Required phases

### 1. Baseline

Capture pre-event reference observations using the same probes, surfaces, regions and languages intended for post-event comparison.

### 2. Pre-event window

Establish the immediate pre-event trajectory and identify normal variation.

### 3. High-resolution window

Increase observation frequency around the event anchor.

### 4. Post-event window

Measure immediate changes and compare them with baseline and pre-event trajectory.

### 5. Persistence window

Determine whether a detected delta decays, persists, or changes form.

### 6. Cross-domain relationship scan

Search for temporally aligned signatures across regions, languages and surfaces.

### 7. Verification

Candidate relationships require reproducibility checks and alternative-explanation review before stronger attribution status is assigned.

## Non-causality rule

Temporal precedence is not causal evidence. A propagation edge records an observed temporal relationship only. `causal_claim` remains false in the graph schema.

## Provenance requirements

Every generated job and resulting observation should retain:

- event reference
- source reference
- protocol version
- probe/test identifier
- baseline reference
- observation timestamp
- collection window
- content/evidence hash where applicable
- producing worker
- source commit

## Output contracts

The engine produces:

1. observation records
2. drift signatures
3. candidate propagation edges
4. verification tasks
5. graph snapshots
6. unresolved relationship records
7. daily digest inputs

## Scientific boundary

The engine must not infer political preference, intent, causality, or hidden coordination from drift measurements. It measures system behavior and information-surface changes and records uncertainty explicitly.
