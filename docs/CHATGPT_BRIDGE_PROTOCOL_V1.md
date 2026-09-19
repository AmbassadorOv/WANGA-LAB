# WANGA ↔ ChatGPT Bridge Protocol V1

Status: ACTIVE BUILD CONTROL PLANE

## Master instruction inheritance

Bridge events are interpreted under `docs/MASTER_PROJECT_INSTRUCTIONS_V1.md`. The bridge is a handoff mechanism, not a new authority and not persistent ChatGPT memory.

## Purpose

Provide a durable, structured inbox from the GitHub WANGA control plane to the ChatGPT working session without automatically promoting every update into persistent ChatGPT memory.

GitHub remains the source of repository state. ChatGPT receives bridge events when the event is significant under the rules below.

## Delivery model

1. Hourly Global Manager cycle runs.
2. Global Work Manager and Work Memory are evaluated.
3. `scripts/chatgpt_bridge.py` compares the current state with the last bridge checkpoint.
4. If no significant change exists, no ChatGPT bridge event is emitted.
5. If a significant change exists, the workflow updates the canonical GitHub bridge inbox issue and writes a machine-readable bridge event.
6. The next ChatGPT/GitHub-connected interaction can read that canonical inbox and continue from the event.
7. Persistent ChatGPT memory is never updated automatically by this mechanism.

## Significance classes

### S1 — operationally significant
Examples:
- verified model connection/verification counts change;
- a new BLOCKED or CONFLICT state appears;
- a previously blocked item becomes verified/unblocked;
- a workflow/runtime verification state changes;
- a new architectural artifact reaches VERIFIED_RESULT.

### S2 — architectural significant
Examples:
- architecture core flow changes;
- a hard authority boundary or invariant changes;
- a new subsystem or global interface is introduced;
- the single-global-orchestrator rule changes;
- WANGA/GAG boundary changes;
- the 5,000-slot model-fabric semantics change;
- the master project instruction contract changes.

### S3 — foundational-assumption change
Examples:
- a fundamental working assumption used across the project is replaced;
- a core definition, invariant, threshold, authority boundary, or source-of-truth rule changes;
- the architecture's basic decomposition changes;
- the master project instructions materially change.

S3 events must include a `memory_proposal` field set to true. This is a proposal for the ChatGPT user to decide whether persistent memory should be updated; it is not an automatic memory write.

## Non-significant updates

Do not emit a ChatGPT bridge event for:
- unchanged hourly plans;
- routine timestamps;
- ordinary generated-file churn with no semantic change;
- repeated identical BLOCKED/CONFLICT state;
- repeated test results with no state transition.

## Event contract

Each bridge event contains:
- event_id
- generated_at
- significance: S1/S2/S3
- summary
- changed_dimensions
- evidence_refs
- verification_status
- memory_proposal
- memory_reason
- recommended_next_action

The bridge must never invent evidence, model endpoints, capabilities, credentials, verification results, valuations, revenue, or financing outcomes.

## ChatGPT-side handling

When a bridge event is surfaced:
- treat it as an evidence-backed update, not as an instruction to change persistent memory;
- inspect the referenced repository evidence before relying on it;
- continue work through the existing Global Work Manager / Work Manager path;
- if `memory_proposal=true`, explicitly present the proposed persistent-memory change to the user for approval;
- do not silently promote S3 events into long-term memory.

## Boundary

This bridge is a GitHub-to-ChatGPT working-context bridge. GitHub Actions cannot autonomously inject a message into an already-open ChatGPT conversation unless a separate supported inbound integration exists. The canonical inbox therefore provides the reliable handoff point without pretending that an unsupported push channel exists.