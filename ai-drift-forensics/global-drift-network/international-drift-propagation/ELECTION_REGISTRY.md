# Global Election Event Registry

Status: research infrastructure specification under development.

## Purpose

The registry converts elections and referendums into standardized event anchors for international AI and information-drift observation. An election is an observation trigger, not a claim about political causation or preference.

The registry should maintain, for every event:

- event identifier
- jurisdiction and region
- election type
- scheduled date and actual event dates when known
- source references and source confidence
- languages relevant to observation
- observation surfaces available for the event
- baseline window
- high-resolution observation window
- post-event persistence window
- status: scheduled, active, completed, postponed, cancelled, unresolved

## Source hierarchy

Use multiple independent election calendars where practical. International IDEA's Elections List and Global Election Monitor, NDI's elections calendar, and other authoritative electoral sources can provide event metadata. The registry stores source provenance rather than treating any single calendar as infallible.

## Observation windows

Default windows are configurable and must be recorded with each event:

1. Long baseline: establish normal behavior before the event.
2. Pre-event: increased sampling before the event anchor.
3. High-resolution: dense sampling around the event and major phases.
4. Post-event: monitor immediate changes after the anchor.
5. Persistence: determine whether observed changes decay, persist, or recur.

The system must never silently change a window after observations exist. Any revision creates a versioned registry record.

## Event phases

Where applicable, represent:

- campaign / pre-event
- voting period
- result reporting
- certification / formalization
- runoff
- recount or dispute phase
- post-event information phase

## Trigger behavior

A registry event can trigger:

`REGISTRY_UPDATE → BASELINE_TASK → OBSERVATION_TASK → CHANGE_SCAN → CROSS_REGION_ALIGNMENT → CROSS_LANGUAGE_ALIGNMENT → CROSS_SURFACE_ALIGNMENT → PROPAGATION_EDGE_CANDIDATES → VERIFICATION`

The trigger does not itself create a drift finding. Findings require observations and evidence.

## Data principle

Every observation must remain attributable to its event anchor, timestamp, region, language, surface, probe, baseline, and evidence references. Missing data is represented explicitly and is never converted into a zero or a negative finding.

## Neutrality boundary

The registry records technical event context. It must not encode political preference, candidate endorsement, voter targeting, or inferred political intent. Temporal association between two observations is not sufficient for a causal claim.
