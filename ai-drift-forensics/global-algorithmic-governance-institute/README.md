# Global Algorithmic Governance Institute — Research Program

Status: PROPOSED RESEARCH PROGRAM / INITIAL ARCHITECTURE
Version: 0.1.0

## Purpose

This workspace defines a proposed international research and technical-coordination program for Operational AI Drift, cross-jurisdiction evidence, AI system monitoring, and interoperable technical criteria.

It is not a government, regulator, court, insurer, certification body, or adopted international standard. Its role is research: develop measurable methods, evidence structures, interoperability rules, and technical interfaces that institutions may evaluate independently.

## Core problem

AI systems can operate across providers, countries, cloud environments, model versions, agents, and downstream applications. A change may therefore cross organizational and jurisdictional boundaries while the technical evidence remains fragmented.

The program asks:

- What exactly changed?
- When did it change?
- Which model, dependency, configuration, data or environment changed?
- Can the change be reproduced?
- Can alternative explanations be separated?
- What jurisdictional and infrastructure context was active?
- Can independent parties exchange the same evidence representation?
- Can risk-transfer institutions evaluate the technical evidence without treating technical research as a legal conclusion?

## Existing WANGA-LAB assets to integrate

- `ai-drift-forensics/IOADC_POSITIONING.md`
- `ai-drift-forensics/INSTITUTIONAL_ARCHITECTURE.md`
- `ai-drift-forensics/VERIFICATION_PROTOCOL.md`
- `ai-drift-forensics/CASE_ENGINE.md`
- `ai-drift-forensics/FORENSIC_CARD_SCHEMA.md`
- `ai-drift-forensics/PREVENTIVE_INTERVENTION_RECORD.md`
- `ai-drift-forensics/global-drift-network/`
- `ai-drift-forensics/global-drift-network/international-drift-propagation/`
- `ai-drift-forensics/global-drift-network/orchestrator/`
- `wanga-research-groups/`
- Neural Thinking Machine subsystem
- Research Asset Integration Registry

No existing asset is discarded or silently replaced. Integration remains versioned and reversible.

## Institutional interface model

```text
AI PROVIDERS / DEPLOYERS
          |
          v
   DRIFT OBSERVATION
          |
          v
 AI DRIFT FORENSICS
          |
          +--> REPRODUCIBILITY
          +--> PROVENANCE
          +--> ATTRIBUTION
          +--> VERIFICATION
          |
          v
       IOADC
          |
   +------+-------+----------------+
   |              |                |
STANDARDS      INSURANCE       SUPERVISION
   |              |                |
   +--------------+----------------+
                  |
          INTERNATIONAL
       TECHNICAL COORDINATION
```

## Scientific independence

Scientific evidence, economic state, funding, market value, and institutional decisions must remain separate data domains. A contributor must not need to surrender scientific independence in order to participate in research.

## Development rule

The institute program is an interface layer above the existing forensic and WANGA research. It must not become a new monolith.
