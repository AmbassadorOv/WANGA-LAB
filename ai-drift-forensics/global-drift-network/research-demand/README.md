# RESEARCH DEMAND LAYER

The Research Demand Layer connects the public scientific square to the research queue.

## Principle

Scientists and research participants can indicate which domains they want investigated and can submit a short research question. These inputs are treated as demand signals, not as evidence and not as votes on scientific conclusions.

## Flow

```text
Scientist
   ↓
Interest / Question
   ↓
Validation + privacy minimization
   ↓
Topic aggregation
   ↓
Demand signal
   ↓
Research Priority Model
   ↓
Candidate research queue
   ↓
Observation / Analysis / Verification
   ↓
Finding
   ↓
Daily Scientific Digest
```

## Initial topic taxonomy

- `MODEL_DRIFT`
- `AI_RELIABILITY`
- `AI_SAFETY`
- `ELECTION_INFORMATION_SYSTEMS`
- `FINANCIAL_AI_RISK`
- `HEALTHCARE_AI`
- `AI_INFRASTRUCTURE`
- `SEARCH_AI_INTERACTION`
- `MULTILINGUAL_DRIFT`
- `GEOGRAPHIC_PROPAGATION`
- `DEPENDENCY_CONFIGURATION_DRIFT`
- `AI_GOVERNANCE`
- `OTHER`

## Data minimization

Collect only what is necessary for research-demand aggregation: topic selection, optional research question, submission timestamp, and a pseudonymous participant identifier when deduplication is necessary. Do not collect sensitive personal information merely to measure research interest.

## Guardrails

1. Demand never changes an observation record.
2. Demand never changes a verification result.
3. Demand cannot convert a hypothesis into a finding.
4. A highly requested topic can still remain unresolved or unmeasurable.
5. Low-demand research can still be executed when scientific importance or methodological necessity requires it.
