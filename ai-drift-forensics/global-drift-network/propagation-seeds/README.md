# Propagation Seeds

Weekend-to-Monday public Drift observation lane.

## Objective
Capture timestamped, publicly observable seed events during the weekend and compare them with independently observed changes on Monday and Tuesday.

## Pipeline

`SEED -> EVIDENCE CAPTURE -> NORMALIZE -> DEDUPLICATE -> DRIFT EXTRACTION -> PROPAGATION LINK -> MONDAY AGGREGATE -> TUESDAY CLOSURE`

## Evidence boundary

- Public sources only.
- Preserve the original source URL and timestamp.
- Do not infer private communications or private individual activity.
- Treat prior outreach as an external stimulus timestamp, not as proof of causality.
- Never convert a single observation into network-level Drift without independent supporting observations.

## Analysis lanes

1. **Seed Intake** — collect and normalize timestamped candidate seeds.
2. **Evidence / Provenance** — preserve source, timestamp, capture metadata and evidence references.
3. **Drift Extraction** — identify measurable deltas against an explicit baseline.
4. **Propagation Analysis** — link matching signatures across independent points.
5. **Persistence / Return** — measure continuation, reversal and recurrence.
6. **Synthesis** — produce the Monday network picture and Tuesday closure report.

## Minimum seed record

`seed_id, source, timestamp, entity_or_system, signal_type, baseline_ref, direction, magnitude, evidence_ref, confidence`

Counts are evidence-limited. No synthetic or duplicated observations are counted.
