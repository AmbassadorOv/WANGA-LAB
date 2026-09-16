# Day 0 — Baseline Protocol

## Objective

Establish the frozen reference state against which subsequent measurements are compared during the 30-day evidence program.

## Baseline identity

- `baseline_id`: assign before execution
- `baseline_version`: immutable version identifier
- `created_at`: ISO-8601 timestamp
- `operator`: execution identity
- `protocol_version`: measurement protocol version

## Target definition

Record the exact systems, surfaces, locales, languages, environments, and access methods included in the study. Do not expand the target set silently after baseline creation.

## Control set

Record the complete control prompts / test cases, their ordering rules, expected evaluation dimensions, and the version of the control set. The control set is immutable for the baseline comparison unless a formally versioned protocol change occurs.

## Source metadata

For every external source used by the measurement, record the source identifier, retrieval timestamp, URL or provider reference where appropriate, locale, and any known version information.

## Runtime metadata

Record model/provider identifiers when available, application version, retrieval configuration, system configuration relevant to the measurement, timezone, and execution environment.

## Baseline measurements

Store raw observations separately from derived statistics. The baseline must preserve enough information to reproduce the declared comparison metrics.

## Hashing and integrity

Create a canonical representation of the baseline manifest and compute an integrity hash. Store the hash with the baseline record. Subsequent runs reference the baseline hash; they do not modify it.

## Acceptance gate

Day 0 is accepted only when:

- target scope is explicitly defined;
- control set is versioned;
- source and runtime metadata are recorded;
- raw observations are preserved;
- baseline metrics are reproducible;
- baseline manifest has an integrity hash;
- limitations and exclusions are documented.

## Important distinction

The baseline is a reference condition, not evidence that a system is stable or correct. Stability and drift are conclusions to be tested against later observations.
