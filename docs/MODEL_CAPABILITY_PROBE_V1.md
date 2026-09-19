# WANGA Model Capability Probe V1

Status: BUILD SPECIFICATION

## Purpose

Provide a bounded, repeatable test layer for verifying what a model can actually do, rather than trusting labels alone.

## Probe classes

- identity_probe
- text_generation_probe
- reasoning_probe
- structured_output_probe
- tool_use_probe
- vision_probe
- audio_probe
- embedding_probe
- reranking_probe
- long_context_probe
- multilingual_probe
- code_probe
- mathematics_probe
- domain_probe
- latency_health_probe

A probe is executed only when the candidate declares the corresponding capability or when a verification policy explicitly requires it.

## Probe result

Each result records candidate_id, probe_id, declared_capability, observed_capability, pass/fail/inconclusive status, normalized evidence, timestamp, and adapter_id.

## Promotion

PASS across required probes plus successful health and policy checks permits VERIFIED.

INCONCLUSIVE, mismatch, or failed required probes prevent automatic ENABLE.

## Drift compatibility

Probe results are versioned so the same candidate can be re-probed after provider/model changes. Differences become evidence for Drift Forensics rather than silent state mutation.
