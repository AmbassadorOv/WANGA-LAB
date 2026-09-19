# WANGA-LAB Architecture Discovery Program V1

Status: ACTIVE BUILD PROGRAM
Control: docs/MASTER_PROJECT_INSTRUCTIONS_V1.md
Window: September 2026 build cycle → October 2026 Rational Logic publication phase

## Objective

Build a controlled architecture-discovery capability that examines relevant public GitHub repositories and extracts reusable architectural patterns for WANGA-LAB.

This is not a request to copy repositories or ingest all of GitHub indiscriminately. Discovery is targeted, evidence-based, license-aware, and comparative.

## Three architecture agents

### ARCH-01 — Systems Architecture Scout
Scope: orchestration, control planes, distributed systems, agent runtimes, workflow graphs, state machines.

Output:
- repository candidates
- architecture diagrams/entry points
- reusable patterns
- dependency and integration notes
- evidence references
- confidence classification

### ARCH-02 — Cognitive / Agent Architecture Scout
Scope: agent frameworks, memory, planning, routing, tool use, evaluation, multi-agent coordination, model context systems.

Output:
- agent patterns
- memory patterns
- routing/evaluation patterns
- compatibility with NTM, DMA, Rational Logic
- duplication/conflict analysis

### ARCH-03 — Verification / Infrastructure / IP Scout
Scope: testing, evaluation, provenance, observability, security, deployment, licensing and IP-relevant architecture.

Output:
- verification patterns
- runtime/infrastructure patterns
- security boundaries
- license evidence
- adaptation constraints
- IP/commercialization implications

## Common discovery lifecycle

DISCOVER → READ → CLASSIFY → LICENSE CHECK → COMPARE → EXTRACT PATTERN → ADAPT → TEST → VERIFY → RECORD

No discovered repository becomes an architectural dependency merely because it is popular or technically interesting.

## Evidence classes

OBSERVATION
RAW_EVIDENCE
NORMALIZED_DATA
DERIVED_METRIC
INFERENCE
HYPOTHESIS
PROPOSED_CHANGE
VERIFIED_RESULT
CONFLICT

## License and IP rules

Only use patterns whose license and provenance are sufficiently understood for the intended use. Do not copy proprietary code. When a pattern is adopted, record:
- source repository
- source commit/tag when available
- license
- relevant files/sections
- pattern description
- adaptation performed
- compatibility assessment
- verification status

## Search scope

The discovery system should prioritize repositories related to:
agent orchestration, workflow engines, model routing, AI evaluation, provenance, observability, distributed runtimes, memory systems, formal reasoning, verification, security, and infrastructure.

"All GitHub" means broad systematic discovery within defined search domains, not a claim of exhaustive enumeration of the entire GitHub corpus.

## Integration boundary

Discovery feeds the Global Work Manager. It does not create a second global orchestrator.

Discovery may propose:
- architecture changes
- new interfaces
- reusable patterns
- tests
- adapters
- documentation updates

Only verified evidence can promote a proposal into the canonical architecture.

## One-month deliverable

Before the Rational Logic publication phase:
1. establish the discovery registry;
2. run three architecture-agent tracks;
3. collect and classify relevant repositories;
4. identify compatible patterns;
5. produce an Architecture Pattern Matrix;
6. identify conflicts/duplication;
7. propose minimal WANGA adaptations;
8. update investor/bank technical descriptions only from verified state;
9. preserve all source history;
10. leave Rational Logic as the planned next-month formal reasoning work, without prematurely publishing its internal architecture.
