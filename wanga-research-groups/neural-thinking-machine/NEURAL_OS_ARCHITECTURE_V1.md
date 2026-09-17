# Neural OS ↔ Neural Thinking Machine — Architecture V1

Status: DESIGN / EXPERIMENTAL

## 1. Design objective

The system is designed as a computer whose operating environment is itself controlled by a neural control layer. The Neural OS manages the machine and continuously emits structured state updates to the Neural Thinking Machine (NTM). The NTM is the high-level cognitive CPU / Logic Anchor: it interprets state, compares it with rules and history, detects conflicts or drift, and returns bounded decisions or commands.

The architecture must be expressed in formal computational language. Historical or religious source structures may be used as structural inspiration during research, but they are not runtime terminology, ontology, or authority in this implementation.

## 2. Core separation

`MACHINE -> NEURAL OS -> EVENT / STATE BUS -> NTM -> DECISION / COMMAND BUS -> NEURAL OS -> MACHINE`

- **Machine Layer**: CPU, memory, storage, network, sensors, processes and external interfaces.
- **Neural OS Layer**: process supervision, state collection, scheduling, permissions, resource control, event normalization and execution.
- **Event / State Bus**: typed, timestamped, provenance-bearing updates.
- **NTM Layer**: reasoning, semantic interpretation, architecture comparison, drift analysis, verification and escalation.
- **Decision / Command Bus**: bounded outputs from the NTM. A decision is not execution; the Neural OS enforces authorization and executes only permitted commands.

## 3. Formal replacement for a command/action system

The basic unit is a **System Directive (SD)**.

A System Directive is a formal instruction with:

`ID + SCOPE + PRECONDITION + ACTION + TARGET + CONSTRAINTS + EXPECTED_STATE + VERIFICATION + PROVENANCE`

This provides the useful structural property of a rule/action system without importing religious terminology.

### Directive classes

| Code | Formal class | Function |
|---|---|---|
| SD-OBS | Observation Directive | Define what state must be observed or measured. |
| SD-STATE | State Directive | Define a required or permitted system state. |
| SD-BIND | Context Binding Directive | Bind an event/action to its project, process, version, identity and causal context. |
| SD-ACT | Action Directive | Define an executable operation. |
| SD-CON | Constraint Directive | Restrict an action, transition or resource. |
| SD-SEQ | Sequence Directive | Define required ordering between operations. |
| SD-SYNC | Synchronization Directive | Require convergence of state across components. |
| SD-VER | Verification Directive | Define how completion or correctness is established. |
| SD-REC | Recovery Directive | Define permitted recovery or rollback behavior. |
| SD-ESC | Escalation Directive | Route unresolved conflicts or high-risk states to a higher reasoning layer. |

These classes are composable. A real operation normally uses several directives rather than one monolithic rule.

## 4. Formal replacement for different update types

The Neural OS does not send an undifferentiated stream. It emits **Typed State Updates (TSU)**.

`TSU = TYPE + SOURCE + TIMESTAMP + SEQUENCE + STATE_DELTA + CONTEXT + PROVENANCE + CONFIDENCE`

Primary update types:

- `OBSERVE`: raw or normalized observation.
- `STATE`: current machine/component state.
- `EVENT`: discrete transition that occurred.
- `INTENT`: declared operational objective.
- `ACTION`: operation started or requested.
- `RESULT`: operation result.
- `ERROR`: execution or interface failure.
- `CONFLICT`: incompatible states/rules/claims.
- `DRIFT`: detected divergence from a baseline or specification.
- `VERIFY`: verification outcome.
- `ESCALATE`: unresolved issue requiring NTM or architect review.

The key relation is:

`OBSERVE -> STATE -> EVENT -> INTERPRETATION -> DECISION -> ACTION -> RESULT -> VERIFY`

A later message must not silently rewrite an earlier observation. Corrections create a new versioned state with provenance.

## 5. Neural OS as background controller

The Neural OS is the always-on operational layer around the machine. It should:

1. observe machine state;
2. normalize events;
3. attach context and provenance;
4. publish typed updates;
5. receive bounded decisions/commands;
6. validate permissions and preconditions;
7. execute authorized actions;
8. publish results;
9. request verification when required.

The NTM should not need direct unrestricted access to every machine resource. The OS remains the execution boundary.

## 6. NTM control loop

The existing NTM loop remains the cognitive control loop:

`OBSERVE -> REPRESENT -> COMPARE -> REASON -> DETECT CONFLICT -> PROPOSE REPAIR -> VERIFY -> RETURN`

The new Neural OS architecture adds the missing operational interface around it:

`MACHINE -> NEURAL OS -> TSU -> NTM -> DECISION/SD -> NEURAL OS -> EXECUTION -> TSU -> NTM`

## 7. Relation model

Every important system object is connected through explicit relations:

`SOURCE --produces--> UPDATE`

`UPDATE --describes--> STATE`

`STATE --satisfies/violates--> DIRECTIVE`

`DIRECTIVE --permits/requires--> ACTION`

`ACTION --changes--> STATE`

`STATE_CHANGE --verified_by--> VERIFICATION`

`CONFLICT/DRIFT --escalates_to--> NTM`

`NTM_DECISION --bounded_by--> CONSTRAINT`

`EXECUTION_RESULT --feeds--> NTM`

This relation graph is the formal backbone of the system.

## 8. Binding model

The concept of a persistent attachment between a rule/action and its operational context is represented as **Context Binding (CB)**.

`CB = PROJECT + COMPONENT + VERSION + PROCESS + IDENTITY + TIME + SOURCE + CAUSAL_CHAIN`

A directive without a valid binding is incomplete for execution. This prevents a command from being detached from the system state for which it was defined.

## 9. Safety and authority boundaries

- A directive is not evidence.
- An observation is not an interpretation.
- An interpretation is not an authorization.
- A decision is not an execution result.
- A proposed repair is not automatically applied.
- Historical material is evidence for reconstruction, not automatic current authority.

The Neural OS enforces execution boundaries; the NTM provides higher-order reasoning; verification closes the loop.

## 10. Initial implementation order

1. Define typed update schema.
2. Define System Directive schema.
3. Define Context Binding schema.
4. Define Neural OS ↔ NTM message envelope.
5. Implement event/state journal.
6. Implement NTM decision gate.
7. Implement OS-side authorization/precondition gate.
8. Implement verification feedback.
9. Add drift and version graph integration.
10. Test the complete closed loop.
