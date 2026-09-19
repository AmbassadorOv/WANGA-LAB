# WANGA Model Discovery and Binding V1

Status: BUILD SPECIFICATION

## Objective

Convert architectural model-agent slots into verified model bindings without inventing provider endpoints or credentials.

## Pipeline

DISCOVER -> NORMALIZE -> CLASSIFY -> ROLE_ASSIGN -> ADAPTER_RESOLVE -> CAPABILITY_PROBE -> HEALTH_CHECK -> POLICY_CHECK -> REGISTER -> VERIFY -> ENABLE

## Candidate record

Each discovered candidate must contain candidate_id, provider_namespace, exact_model_id, model_version when available, endpoint_class, declared_capabilities, modality, context_window when available, tool_support when declared, provenance, discovery_timestamp, and adapter_id.

Secrets and access tokens are never stored in the candidate registry.

## Verification

A candidate becomes CONFIGURED only when its identity is exact enough to address through an adapter.

A candidate becomes VERIFIED only after connectivity succeeds, capability probing matches declarations, health probing succeeds, policy constraints pass, and evidence is recorded.

A candidate becomes ENABLED only from VERIFIED.

## Failure states

NOT_FOUND, UNREACHABLE, CAPABILITY_MISMATCH, POLICY_BLOCKED, PROBE_FAILED, INCONCLUSIVE, CONFLICT.

Failures remain explicit; the system does not guess.

## Scaling

The 5,000-slot registry contains architectural identities first. Discovery binds real models to those identities in controlled batches. Multiple slots may not silently represent the same endpoint unless that relationship is explicitly recorded.

## NTM handoff

After verification, the Digital Model Agent exposes a bounded capability profile and provenance envelope to the Neural Thinking Machine. NTM receives verified metadata and evidence, not raw provider credentials.
