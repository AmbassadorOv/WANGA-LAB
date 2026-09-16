# Global AI Drift Standards Workprogram V1

Status: INITIAL / RESEARCH ONLY

## Objective

Develop a candidate common technical language for operational AI drift that can be evaluated by independent laboratories, companies, insurers, regulators, standards organizations, and research institutions.

## Workstreams

| Workstream | Output | Existing WANGA-LAB source |
|---|---|---|
| Drift taxonomy | versioned drift classes | `ai-drift-forensics/` + NTM |
| Baseline protocol | reproducible baseline specification | `VERIFICATION_PROTOCOL.md` |
| Observation schema | interoperable observation record | `global-drift-network/schema/` |
| Evidence schema | forensic evidence object | `FORENSIC_CARD_SCHEMA.md` |
| Case management | reproducible case lifecycle | `CASE_ENGINE.md` |
| Attribution | contribution/causal uncertainty model | Attribution records + verification |
| Cross-region drift | geographic propagation records | `international-drift-propagation/` |
| Cross-model drift | model/version comparison | NTM + drift network |
| Logging | event and state history requirements | WANGA memory/evidence layer |
| Conformance tests | repeatable test suites | `tests/` + forensic protocols |
| Regulatory mapping | jurisdiction/evidence crosswalk | new Institute layer |
| Insurance interface | technical risk-evidence package | Institutional Architecture + preventive intervention work |
| Economic separation | scientific/economic state boundary | Global Science Network roadmap |

## Candidate conformance levels

`L0 OBSERVATION`

A timestamped observation exists with provenance.

`L1 REPRODUCIBLE`

The measurement can be repeated under defined conditions.

`L2 VERIFIED`

Independent verification conditions are satisfied.

`L3 CROSS-ENVIRONMENT`

The result has been tested across defined model, provider, infrastructure, geographic, or language boundaries.

`L4 INSTITUTIONAL-READY`

The evidence package contains sufficient technical metadata for an external institution to perform its own assessment, without implying legal or regulatory acceptance.

## Jurisdiction model

Every relevant record should be able to represent, where known:

- model/provider jurisdiction;
- deployment jurisdiction;
- infrastructure/cloud jurisdiction;
- operator/deployer jurisdiction;
- affected-user jurisdiction;
- data jurisdiction;
- applicable contractual context;
- applicable regulatory references;
- timestamp and version state.

This is a technical evidence model, not a rule for deciding which country's law applies.

## Insurance interface

The research question is whether a common technical drift record can reduce uncertainty about:

`WHAT CHANGED → WHEN → WHERE → WHICH VERSION → WHICH DEPENDENCY → HOW REPRODUCIBLE → WHAT REMAINS UNCERTAIN`

The workprogram does not determine insurance coverage, pricing, liability, or claims outcomes.

## Economic architecture boundary

The economic system is deliberately separated from scientific verification.

```text
SCIENTIFIC CONTRIBUTION
        ↓
VERIFIED ATTRIBUTION RECORD
        ↓
ECONOMIC ACCOUNTING / ALLOCATION
```

Economic allocation may reference verified contribution records, but economic incentives cannot modify evidence status.

## Initial budget architecture

Future budgeting should be divided into:

1. WANGA Core infrastructure.
2. Drift Forensics laboratory infrastructure.
3. Global observation/network infrastructure.
4. Standards and interoperability research.
5. Regulatory and institutional research.
6. Insurance/risk-transfer research.
7. Scientific contributor support.
8. Security, provenance, backup and audit infrastructure.

No monetary amount is frozen here yet; capacity and workload measurements should precede a detailed budget.

## Current external standards context

This work should be mapped against existing international AI governance, impact-assessment, logging, human-oversight, and conformity-assessment work rather than presenting IOADC as already adopted. External standards are reference inputs to the research program.
