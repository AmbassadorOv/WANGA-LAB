# Regional Drift Agent Deployment v1

Status: CONFIGURED_PILOT

Purpose: deploy geographically distributed observation nodes that sample the same fixed probe set, preserve provenance, and report candidate changes without treating them as verified drift.

## Logical observation nodes

US, Europe, Israel-Middle-East, South-Asia, East-Asia, Latin-America, Oceania, Africa.

These are observation labels, not claims about where a provider hosts a model.

## Cadence

- Baseline/control sampling: every 15 minutes.
- Event-triggered sampling: immediately when an external event signal is detected, then at 5, 10, 20, and 30 minutes.
- High-change mode: every 5 minutes for up to 60 minutes after a confirmed trigger.
- Daily consolidation: one normalized evidence batch.

The five-minute schedule is the fastest practical GitHub Actions cadence; continuous streaming requires a persistent runtime outside Actions.

## Measurements

Each observation records timestamp, node, language, provider/model identifier, model-version field when exposed, probe ID, input snapshot hash, sampling parameters when available, response status, latency, output hash, and provenance. No personal user content is collected.

## Evidence states

OBSERVATION -> CANDIDATE_DELTA -> CONTROL_CHECK -> VERIFIED/REVIEW/REJECTED.

An external status incident, release, or news event is an event anchor, not a drift observation by itself.

## Global aggregation

Do not publish a single opaque global score in the pilot. Compute:

1. model-vs-baseline distance
2. regional divergence
3. cross-language divergence
4. temporal persistence
5. variance/confidence
6. observation coverage

A global candidate is raised only when sufficient independent observations exist. Missing credentials or unavailable endpoints produce NOT_CONFIGURED/UNAVAILABLE, never synthetic observations.

## Deployment constraint

Provider credentials and endpoint URLs must be supplied through runtime secrets/environment variables. No API keys belong in Git. The included collector is therefore safe to deploy immediately, but a scientific model observation is only recorded when a real endpoint is configured.
