# WANGA Model Adapter Contract V1

Status: BUILD SPECIFICATION

An adapter is the controlled boundary between a Digital Model Agent and a provider/runtime.

## Required operations

1. identity() -> exact provider namespace and model identifier
2. capabilities() -> declared capability set
3. probe(request) -> bounded deterministic capability test
4. health() -> connectivity/health result
5. invoke(request) -> execution under an already-authorized task
6. normalize(response) -> canonical response envelope
7. evidence(response) -> provenance/evidence references

## Security boundary

Provider credentials are resolved by the runtime environment or secret manager. They are never passed through or persisted in the model-agent registry, candidate registry, work-memory state, or NTM envelope.

## Adapter result

Every operation returns a normalized result with adapter_id, provider_namespace, model_id, operation, status, timestamp, evidence_refs, and error_class when applicable.

## Activation rule

The adapter may not declare an agent ENABLED. It only supplies evidence. The registration/verification layer decides whether the agent reaches VERIFIED and then ENABLED.

## Failure behavior

Adapters must fail closed for missing identity, authorization, incompatible capabilities, invalid requests, unavailable endpoints, and normalization errors.
