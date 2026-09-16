# Measurement Taxonomy V1

Measurements are grouped by what is directly observable. A derived metric must retain links to the observations from which it was calculated.

## INPUT

Token count, input length, language, structured-task parameters, perturbation identifiers, and input snapshot hashes.

## PROCESSING

Runtime timing and other process-level measurements exposed by the research environment. This category does not imply access to hidden model internals.

## REPRESENTATION

Where available and legitimately exposed: activations, logits, attention-related tensors, embedding vectors, layer-level summaries, dimensionality reductions, and representation distances.

## OUTPUT

Response status, output length, token probabilities where available, response hashes, structured task scores, and other directly defined output measurements.

## BEHAVIOR

Instruction following, semantic consistency, refusal behavior, factual consistency under controlled tests, sensitivity to perturbation, cross-language consistency, and latency/status behavior.

## Derived measurements

Derived values may include:

`divergence` — distance between two observations under a declared metric.

`stability` — repeatability under the same controlled condition.

`sensitivity` — change associated with a defined perturbation.

`state_distance` — distance between defined behavioral/representation states.

`transition_rate` — frequency or rate of observed state transitions within a defined window.

`drift` — change relative to a versioned baseline, with baseline definition explicitly stored.

## Boundary

A metric is not an explanation. A correlation between an internal measurement and output behavior does not by itself establish the mechanism producing that behavior.
