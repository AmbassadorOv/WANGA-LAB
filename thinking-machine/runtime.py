import json
import os
import hashlib
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text())
LAYERS = ROOT / "layers"
STATE = ROOT / "state"
LAYERS.mkdir(exist_ok=True)
STATE.mkdir(exist_ok=True)

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def call_model(prompt):
    key = os.environ.get(CONFIG["model"]["key_env"])
    base = os.environ.get(CONFIG["model"]["provider_env"], "https://api.openai.com/v1")
    model = os.environ.get(CONFIG["model"]["name_env"], "gpt-5.6")
    if not key:
        raise RuntimeError("MODEL_API_KEY is not configured")

    body = json.dumps({
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are the architecture generator for a bounded recursive "
                    "Thinking Machine. Return JSON only. Never return executable code. "
                    "Design a small computational graph that can be validated structurally."
                )
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }).encode()

    req = Request(
        base.rstrip("/") + "/chat/completions",
        data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    )
    with urlopen(req, timeout=120) as response:
        payload = json.loads(response.read().decode())

    content = payload["choices"][0]["message"]["content"]
    return json.loads(content)

def current_layers():
    return sorted(LAYERS.glob("layer-*.json"))

def validate(layer):
    required = {"layer_id", "purpose", "nodes", "edges", "tests"}
    if not required.issubset(layer):
        return False, "missing required fields"

    nodes = layer["nodes"]
    edges = layer["edges"]

    if not isinstance(nodes, list) or not nodes:
        return False, "nodes must be non-empty"
    if len(nodes) > CONFIG["max_nodes_per_layer"]:
        return False, "node limit exceeded"
    if len(edges) > CONFIG["max_edges_per_layer"]:
        return False, "edge limit exceeded"

    ids = {n.get("id") for n in nodes}
    if None in ids or len(ids) != len(nodes):
        return False, "node ids must be unique"

    for e in edges:
        if e.get("from") not in ids or e.get("to") not in ids:
            return False, "edge references unknown node"

    if not isinstance(layer["tests"], list) or not layer["tests"]:
        return False, "layer requires tests"

    return True, "ok"

def structural_score(layer):
    nodes = len(layer["nodes"])
    edges = len(layer["edges"])
    tests = len(layer["tests"])
    score = min(1.0, 0.30 + 0.02 * nodes + 0.01 * edges + 0.08 * tests)
    return round(score, 3)

def load_state():
    p = STATE / "state.json"
    if not p.exists():
        return {"iteration": 0, "active_layers": [], "history": []}
    return json.loads(p.read_text())

def save_state(state):
    (STATE / "state.json").write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")

def main():
    state = load_state()
    existing = current_layers()

    if len(existing) >= CONFIG["max_total_layers"]:
        print("Layer ceiling reached; no generation performed.")
        return

    prompt = f"""
Current iteration: {state['iteration']}
Accepted layer count: {len(existing)}

Generate up to {CONFIG['max_layers_per_run']} NEW computational layers.

Each layer must be JSON:
{{
  "layer_id": "layer-N",
  "purpose": "...",
  "nodes": [
    {{"id":"n1","role":"...","operation":"..."}}
  ],
  "edges": [
    {{"from":"n1","to":"n2","condition":"..."}}
  ],
  "tests": [
    {{"name":"...","assertion":"..."}}
  ]
}}

The layers must extend the current network rather than merely rename existing nodes.
Do not output code, credentials, shell commands, or network instructions.
"""

    proposal = call_model(prompt)
    proposals = proposal if isinstance(proposal, list) else [proposal]

    promoted = []
    for layer in proposals[:CONFIG["max_layers_per_run"]]:
        ok, reason = validate(layer)
        score = structural_score(layer) if ok else 0.0

        if ok and score >= CONFIG["promotion_threshold"]:
            text = json.dumps(layer, indent=2, ensure_ascii=False) + "\n"
            digest = sha(text)
            path = LAYERS / f"{layer['layer_id']}-{digest[:10]}.json"
            path.write_text(text)
            promoted.append({
                "layer_id": layer["layer_id"],
                "sha256": digest,
                "score": score,
                "path": str(path.relative_to(ROOT))
            })
        else:
            print(f"Rejected layer: {reason}; score={score}")

    state["iteration"] += 1
    state["active_layers"].extend(promoted)
    state["history"].append({
        "iteration": state["iteration"],
        "promoted": promoted
    })
    save_state(state)

    print(json.dumps({
        "iteration": state["iteration"],
        "promoted": promoted
    }, indent=2))

if __name__ == "__main__":
    main()
