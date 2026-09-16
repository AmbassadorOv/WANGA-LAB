# Intervention Anchor Model V1

Status: ACTIVE METHODOLOGY
Version: 1.0.0

## Purpose

For the current post-intervention drift experiment, the primary reference point is the documented intervention exposure: the already-completed research communications sent to the relevant public institutional information surface.

This experiment therefore measures the subsequent drift trajectory relative to that exposure. Later public events are retained as secondary event anchors and alternative explanatory variables.

## Central measurement domain

The Ministry of Finance public information environment is the central measurement domain for this pilot. Other public institutional and international information surfaces are comparison/propagation surfaces, not substitutes for the primary anchor.

No measurement targets private communications, private accounts, individual behavior, or inferred intentions.

## Timeline

`PRE-INTERVENTION BASELINE -> INTERVENTION EXPOSURE -> OBSERVATION FREEZE -> OUTBOUND -> PROPAGATION -> RETURN -> DECAY`

The observation-freeze marks the point after which the research team makes no additional intervention intended to influence the measured systems.

## Anchor fields

Each experiment run should retain:

- `intervention_anchor_id`
- `intervention_window_start`
- `intervention_window_end`
- `observation_freeze_time`
- `primary_surface_id`
- `baseline_snapshot_id`
- `method_version`

Only the minimum metadata needed to reproduce the experiment should be retained about the intervention. Private correspondence content is not required for the measurement model.

## Measurement logic

The first objective is not to prove causality. It is to determine whether a reproducible change occurs after the intervention anchor and whether a structured temporal relationship can be measured across defined public information surfaces.

The primary outputs are:

1. time from intervention anchor to first detectable change;
2. amplitude and energy of the change;
3. persistence and decay;
4. propagation lag to comparison surfaces;
5. attenuation or amplification;
6. return-wave timing and magnitude;
7. outbound/return relationship;
8. independent-node agreement;
9. control comparison;
10. alternative-event overlap.

## Interpretation rule

`POST_INTERVENTION_TEMPORAL_CHANGE` is an observational classification. It must not be converted into `CAUSED_BY_INTERVENTION` without controlled evidence and replication.

The Ministry of Finance environment is therefore the **primary anchor and measurement domain for this specific experiment**, while the wider network provides the comparison needed to determine whether the observed pattern is local, propagated, persistent, or replicated.
