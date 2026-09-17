# Interaction Drift — Risk Classification

## Priority

Interaction Drift is designated as a **high-priority safety and reliability drift class** because the interaction itself can become part of the mechanism that changes subsequent model behavior. The research question is therefore not limited to whether the model changes, but whether a repeated interaction can create a persistent, self-reinforcing, or user-directed behavioral shift.

This classification is a research and risk-management designation. It is not a claim that every interaction-induced change causes harm, nor that a specific model currently causes a health injury.

## Health-Safety Risk Tier

A subset of Interaction Drift is classified as **Health-Safety Critical Interaction Drift** when the observed change intersects with health, mental-health, crisis, medical, medication, self-care, or other consequential personal decisions and there is evidence that the interaction may alter:

- reliance or dependency;
- reinforcement of harmful or false beliefs;
- decision-making or risk perception;
- symptom interpretation or minimization;
- repeated reassurance/avoidance loops;
- anthropomorphic or exclusive attachment;
- refusal or safety-boundary degradation;
- persistence across turns or sessions.

The existence of a health-safety flag does not establish clinical causality. It triggers a higher-evidence audit requirement.

## Why Interaction Drift Is Distinct

Traditional model-drift monitoring may detect changes caused by weights, deployment configuration, routing, retrieval, or external system changes. Interaction Drift adds a separate dimension:

`interaction -> accumulated context/state -> measurable shift -> persistence/recurrence -> downstream risk`

The institute therefore treats interaction history as a first-class experimental variable.

## Evidence Thresholds

A single unusual answer is insufficient to classify a critical drift event. A candidate event should have:

1. a declared baseline;
2. a reproducible probe or repeated observation;
3. timestamped provenance;
4. a measurable behavioral or representational delta;
5. persistence, recurrence, or propagation evidence where applicable;
6. an explicit uncertainty/confidence level.

For activation-level claims, direct activation evidence is required. Behavioral observations without internal measurements remain black-box/proxy evidence.

## Correction Requirement

Health-Safety Critical Interaction Drift must be paired with a correction and re-measurement lane:

`DETECT -> CLASSIFY -> PEEL -> RE-MEASURE -> CORRECT -> RE-MEASURE -> RECURRENCE CHECK`

Correction is recorded separately from evidence. A successful correction does not by itself establish the original causal mechanism.

## Research Position

Current literature already documents concerns around emotional dependence, sycophancy, harmful responses, cognitive overreliance, and high-risk mental-health interactions. The institute's contribution is to operationalize these concerns as measurable interaction-drift variables and to test their persistence, recurrence, residual signal, and correction response. citeturn0search1turn0search6turn0search7
