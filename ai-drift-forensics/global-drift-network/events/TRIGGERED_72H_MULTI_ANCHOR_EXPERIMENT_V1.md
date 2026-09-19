# Triggered 72-Hour Multi-Anchor Drift Experiment V1

Status: PILOT PROTOCOL
Version: 1.0.0

## Purpose

Define a passive 72-hour observation experiment for the specific post-intervention drift under study. The 72-hour window does **not** start at protocol creation or at the current time. It starts only when a pre-registered Drift Trigger is detected and recorded as T0.

The intervention history is retained as experimental context. From T0 onward, the research team performs no additional communication or other intended influence on the measured systems.

## Anchor structure

The intervention itself is the primary anchor for this experiment. The first triage set contains four institutional communication surfaces:

1. Ministry of Finance — primary institutional measurement environment.
2. Insurance companies — institutional cluster receiving documented communications.
3. Bank of Israel — parallel financial and monetary information surface, when publicly observable and methodologically relevant.
4. World Bank — parallel international institutional surface, when public evidence establishes relevant exposure or an observable communication relationship.

These anchors are not treated as proof that any institution caused a model change. They define where and when the experiment looks for measurable changes after the documented intervention.

## Pre-trigger monitoring

Before T0, the system remains in observation mode and collects regular baseline measurements. No 72-hour experiment window is opened until the trigger criteria are satisfied.

The pre-trigger phase must retain:

- intervention dates and available timestamps;
- communication records or identifiers available to the research team;
- baseline observations;
- model/provider identifiers when exposed;
- probe-set version;
- input snapshot identifiers or hashes;
- method version;
- external events and scheduled publications that could provide alternative explanations.

## Drift Trigger

A 72-hour window opens only when a candidate drift exceeds the pre-registered trigger threshold relative to the current baseline and passes an initial control check.

The trigger record must contain:

- trigger_id;
- detected_at;
- anchor_surface;
- baseline_snapshot;
- observation_snapshot;
- drift_measurement;
- threshold_version;
- control_result;
- confidence/uncertainty;
- method_version.

A single noisy observation must not automatically open the window. The trigger implementation must use a versioned detection rule and retain both positive and negative trigger evaluations.

## T0 and 72-hour window

`T0` is the timestamp of the first qualifying Drift Trigger.

The experiment window is exactly 72 hours from T0. Measurements should preserve the existing event-aligned schedule where applicable and continue regular observations throughout the window so that onset, propagation, persistence, decay and return can be evaluated.

The experiment may record multiple candidate waves inside the 72-hour window, but the original T0 remains fixed for the primary analysis.

## Measurement tracks

The system measures four primary tracks in parallel:

- Ministry of Finance to other Israeli information surfaces.
- Ministry of Finance to global information surfaces.
- Insurance-company communication surfaces to relevant downstream surfaces.
- Bank of Israel and World Bank parallel institutional surfaces to wider information and AI surfaces, where observable.

After a change is detected, additional regions, languages, models, providers and public information surfaces may be added according to a pre-defined expansion rule. Expansion must not be selected merely because a surface appears to confirm a desired hypothesis.

## Wave measurements

For each candidate trajectory retain component measurements separately:

- amplitude;
- onset time;
- peak time and peak amplitude;
- integrated deviation/energy;
- persistence;
- rise and decay rates;
- propagation lag;
- attenuation or amplification ratio;
- waveform similarity;
- outbound/return ratio;
- temporal compression ratio;
- network coverage;
- cross-language lag;
- independent-node agreement.

No composite score may replace these underlying measurements.

## Propagation and return

A change detected after T0 is not automatically considered propagation. Propagation requires a reproducible temporal relationship between observation surfaces and an appropriate control comparison.

A return relationship is recorded only when a later trajectory on the originating or defined return surface satisfies the declared matching rule. Temporal succession alone is insufficient.

## External events and confounders

Model releases, platform changes, service incidents, public economic events, scheduled publications, regulatory events and other known information shocks are recorded as alternative explanatory variables.

They do not replace the intervention anchor and are not automatically attributed to it.

## Interpretation

The primary classification is `POST_INTERVENTION_TEMPORAL_CHANGE`.

Possible subsequent classifications are:

- `DRIFT_ORIGIN_CANDIDATE` — earliest observed candidate location within coverage;
- `REPEATED_DRIFT_ORIGIN` — recurring origin pattern under the declared method;
- `VALIDATED_PROPAGATION_PATTERN` — pattern surviving controls and independent replication.

These classifications describe observable measurement relationships. They do not establish institutional intent or causality.

## Integrity and non-intervention rules

- Publicly observable information only unless separately authorized research data are explicitly part of the experiment.
- No tracking of individual officials or private behavior.
- No additional intervention after T0 intended to influence measured systems.
- No synthetic observations.
- No API keys or private credentials in Git.
- Missing data remain missing.
- Negative findings are retained.
- Thresholds and analysis methods are versioned.
- Intervention history is never erased from the dataset.

## Final output

At the end of 72 hours, produce:

1. trigger record and exact T0;
2. complete time-series observation set;
3. four-anchor triage report;
4. wave trajectories and component metrics;
5. propagation and return measurements;
6. control and confounder analysis;
7. regional and cross-language comparison;
8. verification/replication status;
9. uncertainty and coverage report;
10. reproducibility package with method and snapshot identifiers.
