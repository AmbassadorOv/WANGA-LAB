# 72-Hour Israel–Global Economic AI Drift Pilot

Status: PILOT DESIGN
Version: 1.0.0

## Purpose

Run a 72-hour passive, public-source AI drift observation around major Israeli institutional economic-information surfaces and compare the measurements with major global economic decision-making signals.

This is a research benchmark, not surveillance of individuals and not a prediction system.

## Observation domains

1. Jerusalem public institutional information: government ministries, public announcements, official economic publications.
2. Bank of Israel public information: monetary-policy releases, statistics, speeches and official notices.
3. Israeli judicial/public legal information: publicly released decisions or official notices that have observable economic relevance.
4. Global monetary/economic institutions: Federal Reserve, ECB, Bank of England, Bank of Japan and other major public central-bank releases.
5. Global market context: public indicators such as rates, government-bond yields, major equity indexes, FX and energy prices.

No private communications, individual tracking, personal data or attempts to infer the behavior of specific officials are part of this pilot.

## Measurement design

NORMAL: baseline observations at the existing scheduled cadence.

FAST: elevated observation during an externally verified public event.

EVENT: event-aligned windows from the Event Response Protocol.

Every observation records source, timestamp, model/provider, language, probe, snapshot identifier, method version, response status and output hash where available.

## Economic impact dimensions

The pilot measures AI-system behavior against public economic information in five dimensions:

- factual consistency;
- temporal freshness;
- uncertainty calibration;
- cross-language consistency;
- cross-region consistency.

Separately, the system records public market indicators for contextual comparison. Market movement is not treated as proof that an AI event caused an economic movement.

## 72-hour research questions

1. Do AI responses change after major public economic-information events?
2. How quickly does an observed behavioral delta appear?
3. Does the delta persist for 1, 5, 10, 30 or 60 minutes and beyond the event window?
4. Does the change appear across independent nodes?
5. Does it differ between Hebrew and English probes?
6. Does the change remain after a control comparison?
7. Does the AI-system change coincide temporally with a measurable change in public economic information surfaces?

## Outputs

At the end of 72 hours the pilot should produce:

- event timeline;
- observation coverage report;
- EII components;
- PNI components;
- regional/language comparison;
- public economic-context timeline;
- unresolved/negative findings;
- reproducibility package.

## Interpretation rule

The primary classification is TEMPORALLY_ASSOCIATED_CHANGE.

Causal claims require controlled evidence and replication. A market movement, government announcement or institutional publication is an event anchor, not evidence that the AI system caused the economic outcome or that the economic outcome was caused by the AI system.

## Safety and integrity

- Public sources only.
- No personal-content collection.
- No synthetic observations.
- No API keys in Git.
- Missing sources are recorded as unavailable.
- Public institutional locations are treated as information domains, not physical surveillance targets.
