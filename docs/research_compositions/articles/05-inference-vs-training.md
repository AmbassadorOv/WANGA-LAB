# Inference-Time Reasoning and the Cost of Search

**Evidence class:** PRIMARY RESEARCH REPORT  
**Window:** 2026-09-15 to 2026-09-19.

## Abstract

Google Research reported a Retrieve-for-Train approach intended to reduce inference-time bottlenecks for complex AI search by shifting part of the computational burden into training.

This provides a useful systems distinction:

**capability acquisition during training** versus **computation performed during inference**.

## Composition

A research architecture should track at least:

1. capability source;
2. training-time computation;
3. inference-time computation;
4. retrieval or external-tool dependency;
5. verification cost;
6. latency and resource constraints.

## WANGA connection

For drift analysis, the distinction matters because two systems can expose the same interface while relying on different computational paths.

A behavioral comparison should therefore preserve:

**model version + runtime configuration + tool state + retrieval state + evaluation conditions.**

## Cross-domain fractals

The same distinction can be studied in:

- scientific search;
- theorem proving;
- code generation;
- laboratory planning;
- optimization;
- simulation control.

## Source

Google Research, “Bypassing inference bottlenecks: Accelerating complex AI search with Retrieve-for-Train,” 15 September 2026. citeturn0news9

**Status:** RESEARCH DRAFT based on the primary research report; independent replication is not asserted.
