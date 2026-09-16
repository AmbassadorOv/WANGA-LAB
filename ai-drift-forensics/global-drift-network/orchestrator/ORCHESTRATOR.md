# Global Drift Research Orchestrator

## Role

The Orchestrator is the control plane for the Global Drift Network. It coordinates deterministic processing and agent roles without becoming the source of scientific claims.

## Daily cycle

`TRIGGER → SNAPSHOT → CHANGE_SCAN → DEMAND_SYNC → ROUTE → ANALYZE → VERIFY → DIGEST → EVIDENCE_RECORD → QUALITY_GATE → PUBLICATION_QUEUE`

## Routing logic

- New raw observation → Observation Worker
- New baseline/delta → Drift Analysis Worker
- Cross-region or cross-language relationship → Interaction Worker
- Evidence or attribution question → Verification Worker
- New scientist-interest signal → Demand Worker
- Validated daily state → Digest Worker
- Daily evidence package → White Paper Evidence Registry
- Passing public-output gate → Publication Worker

## Evidence integration

Every completed daily run should produce or reference:

1. a run record;
2. observation and analysis IDs;
3. verification results and unresolved alternatives;
4. a state snapshot with content hash;
5. evidence-registry entries for material findings;
6. claim IDs only when a substantive claim is actually supported by the recorded evidence.

The White Paper evidence layer is located at:

`publication/whitepaper-evidence/`

The evidence layer separates measured observations from external support and hypotheses. It must never be used to manufacture evidence for an intended conclusion.

## Agent/worker separation

The current design uses 12 logical agent roles but a smaller execution footprint. Roles are capabilities, not necessarily separate model instances.

### Control roles

1. Orchestrator — schedules and routes work.
2. Evidence Guardian — prevents unsupported claims from entering outputs.
3. Quality Gate — validates publication eligibility.

### Research roles

4. Observation Analyst — normalizes observations.
5. Drift Analyst — detects deltas against baselines.
6. Temporal Analyst — aligns changes in time.
7. Geographic Analyst — compares regions.
8. Language Analyst — compares languages.
9. Cross-Surface Analyst — maps interactions between surfaces.
10. Verification Analyst — reproduction and attribution checks.

### Community/publication roles

11. Research Demand Analyst — aggregates scientist interest.
12. Scientific Editor — converts validated state into a daily brief.

## Initial execution groups

To avoid premature agent proliferation, run these as four Workers:

- `WORKER_OBSERVATION`: roles 4–5
- `WORKER_RELATIONSHIP`: roles 6–9
- `WORKER_VERIFICATION`: role 10 plus control roles 2–3
- `WORKER_PUBLICATION`: roles 11–12

The Orchestrator itself remains a separate control process.

## State machine

`IDLE → SNAPSHOTTING → ANALYZING → VERIFYING → GENERATING → EVIDENCE_RECORDED → GATED → QUEUED → COMPLETE`

Failure states:

`BLOCKED`, `UNRESOLVED`, `RETRY_PENDING`.

A failed or unresolved worker must not be converted into a successful finding by the Orchestrator.

## Provenance

Every task records:

- task ID
- worker ID
- input references
- source commit
- protocol version
- start/end timestamps
- output references
- status
- error or unresolved reason when applicable

Every evidence-bearing run additionally records the run ID, baseline ID, configuration hash where available, snapshot ID, and evidence IDs.

## Operating principle

The Orchestrator coordinates the research system; it does not decide what the evidence means. Scientific interpretation remains traceable to observations, analysis, verification records, and explicit uncertainty.
