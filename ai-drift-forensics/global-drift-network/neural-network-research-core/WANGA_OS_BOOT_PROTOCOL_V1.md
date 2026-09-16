# WANGA OS Boot Protocol

Status: ARCHITECTURAL FOUNDATION
Version: 1.0.0

## Purpose

Define how the WANGA research computer initializes a research session before any analysis is allowed to influence higher-level system state.

## Boot sequence

`BOOT → LOAD CONFIG → REGISTER METHODS → INITIALIZE SENSORS → CREATE RUN → COLLECT OBSERVATIONS → VALIDATE INTEGRITY → ENABLE ANALYSIS`

## Boot requirements

A run must establish:

- run identifier
- experiment identifier
- method versions
- probe registry version
- baseline definition
- observation schema version
- provenance policy
- timestamp policy
- credential boundary
- output/evidence destination

## Sensor initialization

Sensors are loaded from the versioned probe registry. A sensor that lacks a defined research question, expected measurement, control strategy or version is not activated as an empirical instrument.

## Data states

`AVAILABLE`, `UNAVAILABLE`, `PARTIAL`, `INVALID`, `PENDING_VERIFICATION` are explicit states. The system must never convert unavailable measurements into synthetic observations.

## Agent initialization

Agents receive declared tasks and permissions. They cannot modify scientific thresholds, promote evidence, or redefine schemas without an explicit versioned change.

## Analysis gate

Higher-level analysis becomes active only after the run records its observation and integrity state. Analysis outputs remain distinguishable from raw observations.

## Human control

The architect/researcher remains the authority for experiment definition, method changes, interpretation boundaries and promotion of validated knowledge.

## First executable target

Implement a local bootable research session that creates a run manifest, loads `PROBE_REGISTRY.json`, initializes the observation collector, executes controlled test probes, and produces a reproducible run record.
