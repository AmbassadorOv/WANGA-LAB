# Thinking Machine Bootstrap

This directory is a minimal runtime for a recursively generated AI computation network.

## Objective

The runtime does **not** let a language model execute arbitrary self-generated code. Each iteration produces a versioned **layer specification**. A layer is admitted only after schema validation and deterministic structural tests.

Pipeline:

`task → planner → layer proposal → validation → activation → next iteration`

The scheduled GitHub Actions workflow runs the loop periodically and commits accepted layer specifications.

## Runtime model

- `config.json` — bounded generation parameters.
- `runtime.py` — proposal, validation, scoring, promotion and state management.
- `layers/` — accepted generated layer specifications.
- `state/` — current runtime state.
- `.github/workflows/thinking-machine.yml` — scheduled execution.

## Required secret

Set `MODEL_API_KEY` in the repository Actions secrets.

Optional variables:

- `MODEL_API_BASE` — OpenAI-compatible endpoint.
- `MODEL_NAME` — model identifier.

The runtime can therefore be connected to whichever model provider is selected later without changing the architecture.

## Important boundary

The first bootstrap intentionally generates **architecture/data specifications, not executable source code**. This makes recursive generation observable and reversible.

Once the generated layer structure is empirically useful, a separate builder can translate an accepted specification into executable components.
