# Neural Thinking Machine — Multi-Model Orchestration V1

Status: DESIGN / EXPERIMENTAL

## Purpose

The NTM may use multiple external AI models as specialized reasoning nodes. Models are not treated as interchangeable copies. Each node receives a bounded role, typed input, explicit output contract, and verification responsibility.

The orchestration layer is a router and coordinator. It does not assume that any external model is authoritative.

## Topology

`USER / WANGA UI`

`        ↓`

`NTM GATEWAY`

`        ↓`

`ORCHESTRATOR`

`   ↙    ↓    ↘`

`ANALYST  CRITIC  SYNTHESIZER`

`   ↘    ↓    ↙`

`EVIDENCE / VERIFICATION`

`        ↓`

`NTM DECISION GATE`

`        ↓`

`NEURAL OS`

## Initial node roles

| Node | Role | Primary task | Must not do |
|---|---|---|---|
| `planner` | Task decomposition | Convert user goal into executable subproblems | Change the user's goal |
| `researcher` | Evidence retrieval | Gather and structure source material | Treat unsupported claims as facts |
| `architect` | System architecture | Analyze interfaces, dependencies and structure | Execute arbitrary system changes |
| `coder` | Implementation | Produce or modify code under specification | Override architecture constraints |
| `critic` | Adversarial review | Search for errors, contradictions and omissions | Become the final authority |
| `drift_analyst` | Drift forensics | Trace rule→interpretation→decision→action→result | Infer drift without evidence |
| `verifier` | Validation | Test outputs against contracts and evidence | Rewrite failed results silently |
| `synthesizer` | Integration | Combine verified node outputs into one structured result | Hide disagreement |

Additional specialized nodes may be added without changing the core protocol.

## Orchestration sequence

### Phase 1 — Intake

`USER_INPUT -> INTENT_GATE`

Extract:

`ACTION + OBJECT + TARGET + PROJECT + CONSTRAINTS + EXPECTED_RESULT`

### Phase 2 — Routing

The orchestrator selects nodes according to task type. A task can invoke multiple nodes in parallel when their inputs are independent.

### Phase 3 — Independent reasoning

Each node receives only the context required for its role plus a common task envelope.

### Phase 4 — Cross-review

The critic and verifier receive candidate outputs and test them against the same specification. Disagreement is preserved as structured data.

### Phase 5 — Synthesis

The synthesizer creates a result containing:

- conclusion / proposed output;
- supporting evidence;
- unresolved disagreement;
- confidence/uncertainty;
- actions proposed;
- verification status.

### Phase 6 — Decision gate

The NTM checks:

`RULES -> CONTEXT -> INTENT -> EVIDENCE -> CAPABILITY -> DECISION -> VERIFICATION`

Only after the gate passes can an authorized command be emitted to the Neural OS.

## Real-time API model

External models are connected through a provider-neutral adapter interface:

`ModelAdapter`

Required operations:

- `health()`
- `capabilities()`
- `generate(request)`
- `estimate_cost(request)` when supported
- `record_usage(result)`

The orchestrator must not depend on provider-specific message formats internally. Provider-specific APIs are isolated inside adapters.

## Model registry

A model is registered with:

`MODEL_ID + PROVIDER + ROLE_CAPABILITIES + ENDPOINT + AUTH_REF + VERSION + LIMITS + STATUS`

API credentials are references to environment secrets only. Keys must never be committed to Git.

## Message envelope

Every model invocation carries:

`request_id + task_id + node_role + system_spec_version + context + input + constraints + expected_output_schema`

Every response returns:

`request_id + model_id + node_role + output + evidence_refs + uncertainty + latency + usage + status`

## Parallelism and ordering

Independent nodes may execute concurrently.

Dependent stages are ordered:

`INTAKE -> ROUTE -> ANALYZE -> CRITIQUE -> VERIFY -> SYNTHESIZE -> DECIDE`

No downstream node may receive a result that has been silently altered after verification. Corrections create new versioned records.

## Failure handling

If a model is unavailable, times out, returns malformed output, or violates its contract:

`FAIL -> RECORD -> RETRY/ROUTE_ALTERNATE -> VERIFY`

Provider failure is not equivalent to reasoning failure. The orchestrator records both separately.

## Disagreement protocol

When nodes disagree:

1. preserve all candidate outputs;
2. identify the exact proposition in dispute;
3. request evidence or verification;
4. classify disagreement as factual, semantic, architectural, or methodological;
5. do not manufacture consensus;
6. escalate unresolved high-impact disagreement to the NTM decision gate.

## User interface role

The ChatGPT-facing interface is treated as a **Human Interaction Gateway (HIG)**. It translates user requests into the common task envelope and presents verified results, pending decisions, conflicts and execution outcomes.

The HIG does not become a hidden execution authority. It is an interface into the NTM architecture.

## Security boundary

Secrets remain in GitHub Actions or runtime secret storage. Model outputs are untrusted inputs until validated. External model calls are observable through request IDs and audit records. No model is granted unrestricted repository, OS, network or deployment authority merely because it is registered.

## First implementation target

Build a provider-neutral Python orchestrator that:

1. loads a model registry;
2. loads the System Directive and message schemas;
3. creates a task ID;
4. routes a task to one or more model adapters;
5. collects structured outputs;
6. invokes critic/verifier stages;
7. synthesizes a result;
8. writes an auditable run record;
9. returns the result to the HIG.


## WANGA-X architecture-generation route

The orchestration layer treats architecture generation as a first-class reasoning route rather than a fixed post-processing step.

`DISCOVERY / INTENT -> REQUIREMENT -> ARCHITECTURE REASONING -> BLUEPRINT / IR -> MATERIALIZATION -> EXECUTION -> EVIDENCE -> VERIFICATION`

The architecture reasoning route is informed by established foundations including HLS, SODA-style accelerator synthesis, requirement-to-architecture synthesis, and adaptive/runtime architecture. These are starting mechanisms, not claims that WANGA-X is already implemented by them.

The `architect` and `blueprint_reasoner` nodes may generate multiple candidates. The verifier evaluates them against the computational requirement and explicit constraints. A changed requirement may re-enter the route and generate a new architecture candidate:

`CHANGED REQUIREMENT -> REASON -> NEW BLUEPRINT -> RECOMPOSE / REBUILD / REPLACE`

The materializer remains a separate execution boundary. NTM reasoning proposes and verifies; the materializer constructs the selected virtual architecture.


# Neural Thinking Machine — Multi-Model Orchestration V1

Status: DESIGN / EXPERIMENTAL

## WANGA-X architecture-generation route

Architecture generation is a first-class NTM reasoning route. The route begins with the user's query or system request and explicitly derives the required neural computation before Blueprint generation:

```
USER QUERY / SYSTEM REQUEST
            ↓
        REQUIREMENT
            ↓
REQUIRED NEURAL COMPUTATION
            ↓
NTM ARCHITECTURE REASONING
            ↓
         BLUEPRINT / IR
            ↓
       MATERIALIZATION
            ↓
      NEURAL COMPUTER
            ↓
         EXECUTION
            ↓
     EVIDENCE / VERIFICATION
```

The neural_computation_deriver determines what neural computation is required by the requirement. The architect and blueprint_reasoner then generate and compare candidate computational structures and Blueprints.

The Blueprint is the representation from which the selected neural computer is materialized. The NTM reasons and verifies; the materializer constructs the selected virtual architecture.

## Dynamic neural-system evolution

A changed requirement does not automatically mean that the existing neural architecture must remain fixed.

`CHANGED REQUIREMENT -> NEW REQUIRED NEURAL COMPUTATION -> NEW BLUEPRINT -> RECOMPOSE / REBUILD / REPLACE`

The evolved system may change architecture, topology, modules, connections, routing, parameters/weights, computational resources, and state representation as required by the new computation.

## Existing orchestration remains

The NTM continues to use bounded specialized roles, provider-neutral model adapters, cross-review, evidence preservation, disagreement preservation, and verification gates. This WANGA-X route changes what the architecting process receives as its primary determinant: the required neural computation derived from the user's request.

## Research status

The WANGA-X route is a research architecture. Existing dynamic-neural and architecture-generation mechanisms provide foundations; the integrated query → neural computation → Blueprint → neural computer loop remains subject to implementation and experimental verification.

See `docs/WANGA_X_NEURAL_COMPUTATION_PARADIGM.md` for the core thesis.