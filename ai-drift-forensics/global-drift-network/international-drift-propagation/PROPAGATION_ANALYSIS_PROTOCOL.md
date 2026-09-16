# Propagation Analysis Protocol

## Research question

Determine whether observed drift signatures form reproducible temporal relationships across regions, languages, and information surfaces.

## Null position

No propagation relationship is assumed before measurement. A relationship becomes a candidate only after comparable observations exist.

## Analysis stages

### 1. Normalize

Normalize timestamps, time zones, probe versions, language metadata, surface identifiers, and baseline references.

### 2. Detect

Calculate within-node change relative to baseline. Preserve raw measurements and uncertainty.

### 3. Align

Place observations on a common timeline. Record the maximum allowed alignment error.

### 4. Compare

Compare drift signatures using pre-registered or versioned similarity rules. Avoid changing similarity criteria after seeing the result without recording the change.

### 5. Generate candidate edges

Create a propagation edge only when the compared observations meet minimum temporal, measurement, and evidence requirements.

### 6. Test alternatives

Before attribution, check plausible alternative explanations, including:

- shared external event
- common upstream dependency
- model or system release
- retrieval/index update
- language-specific processing change
- sampling artifact
- measurement error
- independent simultaneous change
- missing or delayed observations

### 7. Reproduce

Repeat the relevant observation under comparable conditions. Where possible, use an independent probe, time window, system instance, or reviewer.

### 8. Attribute

Attribution describes what evidence supports a relationship and what competing explanations remain. Attribution must not be promoted to causation merely because one event preceded another.

### 9. Verify

Apply the repository Verification Protocol. A propagation relationship may be `SUPPORTED`, `PARTIALLY_SUPPORTED`, `NOT_REPRODUCED`, `REFUTED`, or `UNRESOLVED`.

## Temporal relationship rules

`PRECEDES`: source observation occurs before target observation within the declared comparison window.

`FOLLOWS`: source observation occurs after target observation within the declared comparison window.

`COINCIDES`: observations overlap within the declared coincidence tolerance.

The tolerance must be recorded for each analysis version.

## Propagation strength

Do not collapse evidence into a single unexplained score. Preserve component measurements:

- temporal proximity
- signature similarity
- baseline separation
- evidence completeness
- reproduction status
- independence status
- competing-explanation coverage

If a later scoring model is introduced, its formula and version must be stored with every result.

## Longitudinal analysis

After multiple events, compare candidate edges across event families. Recurrent patterns should be evaluated against appropriate controls rather than counted as independent confirmations automatically.

Repeated observations can reveal:

- recurring signatures
- regional persistence
- language-specific persistence
- cross-surface recurrence
- transient event-linked changes
- relationships that disappear under reproduction
- stable null results

## Causality boundary

Temporal order alone is insufficient for a causal claim. The system records temporal relationships and evidence-backed attribution states; it does not convert correlation into causation.

## Reproducibility record

Every published propagation finding must reference:

`event_id + source_node + target_node + probe_version + observation_refs + evidence_refs + analysis_version + reproduction_status + verification_status`
