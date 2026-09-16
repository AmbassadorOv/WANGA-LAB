# User Drift Forensics — V1

Status: INITIAL / EXPERIMENTAL
Scope: WANGA human-system interaction research

## Purpose

Define a forensic method for measuring change in a user's interaction state with an AI system over time.

This is not a medical, psychological, psychiatric, or personality diagnosis. It measures observable interaction behavior, task performance, semantic preferences, configuration changes, and user-reported state within a defined WANGA environment.

## Core idea

Traditional AI Drift Forensics asks:

`DID THE MODEL CHANGE?`

User Drift Forensics adds:

`DID THE HUMAN-SYSTEM INTERACTION STATE CHANGE?`

and separates that question from:

`DID THE MODEL CHANGE AT THE SAME TIME?`

The test therefore creates a paired longitudinal baseline:

```text
USER BASELINE              SYSTEM BASELINE
      |                          |
      +------------+-------------+
                   |
             CONTROLLED TASKS
                   |
            REPEATED OBSERVATION
                   |
          ┌────────┴────────┐
          ↓                 ↓
      USER DELTA         AI DELTA
          │                 │
          └────────┬────────┘
                   ↓
          INTERACTION DRIFT
```

## Drift dimensions

### 1. Task Strategy Drift

Change in the user's observable strategy for solving equivalent tasks.

### 2. Semantic Calibration Drift

Change in how the user interprets or defines the same controlled terms, instructions, or outputs.

### 3. Preference Drift

Change in explicitly stated preferences for output structure, modality, verbosity, tools, or workflow.

### 4. Interaction Pattern Drift

Change in request structure, correction patterns, iteration depth, tool usage, or delegation behavior.

### 5. Performance Drift

Change in measurable task outcomes under equivalent controlled conditions.

### 6. Configuration Drift

Change caused by WANGA configuration: models, agents, memory, tools, UI, routing, or system prompts.

### 7. External-Context Drift

Documented changes in task environment, workload, data, domain, or other external conditions.

### 8. Residual User-System Drift

Change remaining after known system/configuration/external changes have been controlled or accounted for.

## Required experiment design

A valid test must distinguish at least three states:

`T0 BASELINE`
`T1 OBSERVATION`
`T2 REPEAT / VERIFICATION`

For stronger attribution, use an A/B or crossover design where the same controlled tasks are performed under two known system configurations.

## Evidence collected

Only collect information necessary for the experiment:

- timestamp;
- task identifier;
- system configuration/version;
- model/runtime identifiers;
- relevant WANGA configuration;
- user response or task result;
- correction/acceptance event;
- explicit user-reported preference/state;
- environmental variables required for interpretation;
- provenance and reproducibility metadata.

Do not infer sensitive personal traits from the data.

## Attribution rule

A measured change must not automatically be attributed to the user.

Classification:

`OBSERVED DIFFERENCE`
→ `SYSTEM-CHANGE CANDIDATE`
→ `USER-STATE CANDIDATE`
→ `CONTEXT CANDIDATE`
→ `INTERACTION EFFECT`
→ `UNRESOLVED`
→ `VERIFIED FINDING`

The system should prefer `UNRESOLVED` when competing explanations cannot be separated.

## User Drift Score

V1 does not define a universal numerical score.

Instead, each dimension produces:

`baseline value + current value + delta + confidence + evidence refs + confounders`

A later standards workstream may define normalized metrics after sufficient empirical data exists.

## WANGA integration

The test should be available as a native WANGA diagnostic:

`USER_DRIFT_BASELINE`
`USER_DRIFT_CHECK`
`USER_SYSTEM_DRIFT_SEPARATION`
`USER_DRIFT_RETEST`

NTM may reason over the evidence but must not convert interaction measurements into medical or psychological conclusions.

## Research novelty claim

This repository treats User Drift Forensics as a proposed research extension of the existing AI Drift Forensics framework. It must not claim that no equivalent concept exists anywhere unless a systematic literature and standards review establishes that claim.

## Initial research question

Can longitudinal, reproducible measurement distinguish changes in the user's interaction behavior from changes caused by the AI model, WANGA configuration, tools, memory, or external context?

If yes, User Drift Forensics becomes a second diagnostic axis alongside AI Drift Forensics:

`SYSTEM DRIFT × USER DRIFT × INTERACTION DRIFT`
