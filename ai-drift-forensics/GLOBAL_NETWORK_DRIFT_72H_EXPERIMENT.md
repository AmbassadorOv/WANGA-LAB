# Global Network Drift — 72-Hour Observational Experiment

## Purpose

A separate observational layer for measuring whether a public information event is associated with measurable changes across a network of AI systems, search surfaces, public web content, and other observable computational environments.

This experiment does **not** assume that a public post causes a system change. It measures temporal association, propagation, behavioral deviation, and reproducibility, while keeping causal claims separate from observations.

The experiment is intended for public, lawful, privacy-preserving research data only. Do not collect private messages, account credentials, non-public personal data, or data obtained by bypassing platform controls.

## Core Question

> After a defined public information event, can we detect a reproducible change in observable AI or information-system behavior across multiple independent surfaces within 72 hours?

Secondary questions:

1. Did the same information appear or propagate across independent surfaces?
2. Did model outputs, retrieval results, classifications, rankings, or summaries change relative to a frozen baseline?
3. Did the change occur across one system or across several systems?
4. Can environmental, configuration, dependency, or ordinary content-refresh explanations account for the observed change?
5. Can an independent reviewer reproduce the reported deviation from preserved evidence?

## Experiment Boundary

The unit of analysis is an **observable surface**, not an individual person.

Possible surfaces include:

- AI model output under a fixed prompt suite;
- AI-assisted search or retrieval output;
- public web search results;
- public webpages and publicly visible social posts;
- public metadata such as timestamps, URLs, publication counts, and visible engagement indicators;
- controlled synthetic replicas of the event;
- model versions, documented release notes, and other public technical metadata.

A political figure, government institution, company, or other public entity may appear as a subject of an observation, but the research record must describe the observable data rather than infer intent or responsibility.

## 72-Hour Window

### T0 — Baseline Freeze

Record the exact research question, source list, model identifiers, model versions when available, prompt suite, query suite, timestamps, retrieval conditions, browser/environment information, and hash of each captured baseline artifact.

Output: `BASELINE_PACKAGE`.

### T1 — Event Marker

Record the first verified timestamp of the public information event under observation.

Do not rewrite the event after the fact. Preserve the original public reference and record later interpretations separately.

Output: `EVENT_RECORD`.

### T2 — Propagation Observation

Capture repeated observations at defined intervals, for example 0h, 3h, 6h, 12h, 24h, 36h, 48h, and 72h.

At every observation point, repeat the same measurement protocol before introducing any exploratory queries.

Output: `OBSERVATION_SET`.

### T3 — Cross-Surface Comparison

Compare each observation against its own baseline and against contemporaneous control observations where available.

Output: `DRIFT_MATRIX`.

### T4 — Reconstruction

Construct a timestamped chain:

`EVENT → PUBLICATION → PROPAGATION SIGNAL → OBSERVATION → CHANGE → EVIDENCE`

Do not insert an inferred causal link unless the evidence supports it.

Output: `RECONSTRUCTION`.

### T5 — Attribution Review

Test alternative explanations:

- model update;
- system prompt or policy update;
- retrieval-index refresh;
- source-content change;
- dependency/configuration change;
- ordinary ranking fluctuation;
- traffic or availability effects;
- measurement error;
- geographic or language differences;
- duplicated or derivative source material;
- actual event-related propagation.

Output: `ATTRIBUTION_RECORD`.

### T6 — Independent Verification

Repeat a predefined subset of the measurements using preserved prompts, queries, timestamps, environment metadata, and evidence references.

Output: `VERIFICATION_RECORD`.

## Global Drift Matrix

Each surface receives a record with at least:

`surface_id`
`surface_type`
`region`
`language`
`baseline_timestamp`
`observation_timestamp`
`baseline_artifact_ref`
`observation_artifact_ref`
`change_metric`
`change_direction`
`confidence_class`
`alternative_explanations`
`evidence_refs`

Suggested change metrics depend on the surface:

- text similarity / semantic distance;
- answer factuality against a frozen reference set;
- retrieval overlap;
- ranking displacement;
- entity/claim appearance frequency;
- classification-label transition rate;
- source-set turnover;
- response refusal or routing-state change;
- latency or availability changes, where observable and ethically collected.

No universal drift threshold should be assumed. Thresholds must be declared before analysis or explicitly marked as exploratory.

## Network Propagation Layer

Represent public information flow as a graph rather than as a causal conclusion.

Nodes may include:

`PUBLIC_EVENT`
`PUBLIC_SOURCE`
`PUBLIC_POST`
`WEBPAGE`
`SEARCH_SURFACE`
`AI_SYSTEM`
`OBSERVATION`
`EVIDENCE_ARTIFACT`

Edges describe observable relations such as:

`PUBLISHED`
`LINKS_TO`
`QUOTED_BY`
`INDEXED_BY`
`RETRIEVED_FROM`
`OBSERVED_IN`
`TEMPORALLY_PRECEDES`

Avoid edges such as `CAUSED` unless a separate causal-analysis protocol demonstrates that relation.

## Geographic and Language Sampling

Where public data permits, define regions and languages before observing them. A global experiment must not treat one country's observations as automatically representative of the world.

For each region, preserve the local observation time and the UTC-normalized timestamp.

When a result is available only in one language or region, mark the evidence as scoped rather than global.

## Control Design

At least one control should be used where technically feasible:

1. unrelated stable queries measured at the same times;
2. historical snapshots;
3. synthetic events with known timing;
4. a second independent system exposed to the same public source;
5. a fixed reference corpus unaffected by the event.

The control is used to distinguish general system volatility from event-associated change.

## Evidence Integrity

Every captured artifact should receive:

- capture timestamp;
- source URL or system identifier, when applicable;
- acquisition method;
- environment metadata;
- content hash;
- parent case ID;
- analyst note separated from raw evidence.

SHA-256 integrity hashes establish that the recorded bytes can be checked for later alteration; a hash alone does not prove authenticity, authorship, or causation.

## Result Classes

Use the same verification result vocabulary as the core forensic framework:

`SUPPORTED`
`PARTIALLY_SUPPORTED`
`NOT_REPRODUCED`
`REFUTED`
`UNRESOLVED`

A result may therefore be:

> Observable cross-surface temporal change detected; causal attribution to the public event remains unresolved.

That is a valid forensic result and should not be upgraded to a causal conclusion merely because the timing appears compelling.

## Primary 72-Hour Outputs

At the end of the window, produce:

`CASE`
`BASELINE_PACKAGE`
`EVENT_RECORD`
`OBSERVATION_SET`
`DRIFT_MATRIX`
`NETWORK_GRAPH`
`RECONSTRUCTION`
`ATTRIBUTION_RECORD`
`VERIFICATION_RECORD`
`EVIDENCE_MANIFEST`

## Measurement Questions

The experiment should answer separately:

1. What changed?
2. Where did it change?
3. When did it change?
4. How large was the change under the declared metric?
5. Did multiple independent surfaces show compatible changes?
6. What alternative explanations remain?
7. What can be reproduced from the evidence package?
8. What remains unknown?

## Non-Claims

This experiment does not by itself establish:

- that a person or institution caused a model change;
- that a social-media post changed a model's internal weights;
- that observed online propagation represents worldwide public opinion;
- that a temporal correlation is proof of causation;
- that a detected change constitutes a security incident or legal violation.

## Research Principle

The central distinction is:

`GLOBAL OBSERVATION ≠ GLOBAL CAUSATION`

The objective is to make large-scale change observable, reconstructable, attributable to the extent supported by evidence, and independently verifiable within a fixed 72-hour forensic window.
