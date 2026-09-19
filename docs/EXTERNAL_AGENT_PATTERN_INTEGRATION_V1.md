# WANGA External Agent Pattern Integration V1

Status: ACTIVE BUILD SPECIFICATION
Version: 1.0.0

## Purpose

Integrate useful, documented patterns from open-source agent frameworks into WANGA without copying third-party implementation code and without creating a second global orchestrator.

The integration is pattern-level and provider-neutral. WANGA remains the source architecture.

## Sources reviewed

| Source | License / status | Pattern adopted |
|---|---|---|
| OpenAI Agents SDK | MIT | agents-as-tools / handoffs, guardrails, structured workflow tracing |
| Google Agent Development Kit (ADK) | Apache-2.0 | graph-based workflows, dynamic branching, coordinator/subagent collaboration |
| Microsoft AutoGen | MIT | layered agent runtime, message/event-oriented coordination, benchmark mindset |
| LangGraph | MIT | durable execution, checkpoint/resume, interrupts, stateful long-running workflows |

License status was checked from public project repositories/documentation. This file records architectural patterns, not copied source code.

## WANGA integration map

### 1. Graph-based task execution

Adopt:
- explicit task graph;
- dependency edges;
- deterministic state transitions;
- bounded iterative loops;
- terminal states.

WANGA implementation:
GLOBAL_WORK_MANAGER -> GLOBAL_WORK_PLAN -> task graph -> execution adapters -> verification.

No new global orchestrator is introduced.

### 2. Agent handoff / agents-as-tools

Adopt:
- a model-agent may delegate a bounded subtask;
- delegation must name the target capability and task;
- result returns through a canonical envelope;
- delegation cannot bypass the Global Work Manager or verification gate.

WANGA: DMA -> bounded specialist DMA -> evidence envelope -> parent task.

### 3. Guardrails / tripwires

Adopt:
- pre-execution validation;
- tool/input/output policy checks;
- immediate blocking on invariant violations;
- explicit BLOCKED status.

WANGA guardrails:
- no secret leakage;
- no unverified model execution;
- no unauthorized main-branch mutation;
- no invented endpoint/capability;
- no evidence-free promotion;
- no policy-boundary bypass.

### 4. Durable execution / checkpoint-resume

Adopt:
- checkpoint before and after side effects;
- deterministic task/run identifiers;
- resume from last verified state;
- idempotent retry requirement.

WANGA maps checkpoints into Work Memory and task evidence. A retry must not duplicate a verified side effect.

### 5. Traceability

Adopt:
- end-to-end run ID;
- task spans;
- model-agent identity;
- adapter identity;
- handoff events;
- guardrail events;
- verification events.

WANGA trace is evidence, not merely telemetry. Trace references must be safe to persist and must not contain provider credentials.

### 6. Coordinator + specialist collaboration

Adopt:
- coordinator routes;
- specialists perform bounded work;
- coordinator synthesizes;
- verification can reject synthesis.

WANGA coordinator remains the existing Global Work Manager. NTM remains the high-level reasoning/escalation gate.

### 7. Evaluator / optimizer loop

Adopt as a bounded pattern:
PRODUCE -> EVALUATE -> REVISE -> VERIFY

Rules:
- maximum iteration count;
- evaluator evidence is recorded;
- repeated failure becomes BLOCKED or REVIEW_REQUIRED;
- evaluator cannot silently redefine acceptance criteria.

### 8. Human review interrupt

Adopt:
- durable pause state;
- explicit REVIEW_REQUIRED terminal/intermediate state;
- resume after decision.

For WANGA, this is primarily the final architecture review and any policy-sensitive execution. Autonomous construction must not self-approve.

## What is deliberately NOT imported

- no third-party framework becomes the WANGA global orchestrator;
- no provider-specific agent identity replaces DMA;
- no third-party memory store becomes Work Memory authority;
- no automatic merge authority;
- no copied proprietary or non-open implementation;
- no credentials in agent state;
- no claim that these patterns prove AGI.

## Target runtime flow

INTAKE -> NORMALIZE -> DECOMPOSE -> DEPENDENCY_SCAN -> ROUTE -> GUARD -> EXECUTE -> HANDOFF (optional) -> COLLECT -> EVALUATE (optional bounded loop) -> VERIFY -> CHECKPOINT -> UPDATE_MEMORY -> FOLLOW_UP

Terminal: COMPLETE | BLOCKED | CONFLICT | REVIEW_REQUIRED

## Acceptance criteria

The integration is structurally complete when:
1. task graph state is explicit;
2. every execution has a run/task identity;
3. guardrails can block before execution;
4. execution state can checkpoint and resume;
5. handoffs are bounded and traceable;
6. evaluator loops are bounded;
7. verification remains a promotion gate;
8. final review remains outside autonomous construction.
