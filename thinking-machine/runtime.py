import json
import os
import hashlib
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text())
LAYERS = ROOT / "layers"
STATE = ROOT / "state"
AGENTS = ROOT / "agents"
for p in (LAYERS, STATE, AGENTS):
    p.mkdir(exist_ok=True)

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def issue_ontology_credit(agent_id, scope, iteration, credits):
    payload = f"{agent_id}|{scope}|{iteration}|{credits}"
    return {
        "token_id": "ONTO-" + sha(payload)[:16],
        "type": "ONTO_CREDIT",
        "agent_id": agent_id,
        "scope": scope,
        "credits": credits,
        "iteration": iteration,
        "non_monetary": True
    }

def call_model(prompt):
    key = os.environ.get(CONFIG["model"]["key_env"])
    base = os.environ.get(CONFIG["model"]["provider_env"], "https://api.openai.com/v1")
    model = os.environ.get(CONFIG["model"]["name_env"])
    if not key:
        raise RuntimeError("MODEL_API_KEY is not configured")
    if not model:
        raise RuntimeError("MODEL_NAME is not configured")
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": (
                "You are the governor/trainer of a bounded multi-agent Thinking Machine. "
                "Propose topology and agent specifications, never executable code. "
                "Agents must not overwrite another agent's state, invent provenance, or "
                "operate outside their ontology scope. Every proposed action must carry "
                "an ontology scope and evidence requirement."
            )},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }).encode()
    req = Request(base.rstrip("/") + "/chat/completions", data=body,
                  headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urlopen(req, timeout=120) as response:
        payload = json.loads(response.read().decode())
    return json.loads(payload["choices"][0]["message"]["content"])

def current_layers():
    return sorted(LAYERS.glob("layer-*.json"))

def validate_layer(layer):
    required = {"layer_id", "purpose", "nodes", "edges", "tests"}
    if not required.issubset(layer):
        return False, "missing required fields"
    nodes, edges = layer["nodes"], layer["edges"]
    if not isinstance(nodes, list) or not nodes:
        return False, "nodes must be non-empty"
    if len(nodes) > CONFIG["max_nodes_per_layer"] or len(edges) > CONFIG["max_edges_per_layer"]:
        return False, "topology limit exceeded"
    ids = {n.get("id") for n in nodes}
    if None in ids or len(ids) != len(nodes):
        return False, "node ids must be unique"
    for e in edges:
        if e.get("from") not in ids or e.get("to") not in ids:
            return False, "edge references unknown node"
    if not isinstance(layer["tests"], list) or not layer["tests"]:
        return False, "layer requires tests"
    return True, "ok"

def validate_agent(agent, issued_token):
    required = {"agent_id", "role", "ontology_scope", "actions"}
    if not required.issubset(agent):
        return False, "missing agent governance fields"
    if agent["agent_id"] != issued_token["agent_id"]:
        return False, "token-agent mismatch"
    if CONFIG["agent_governance"]["require_scope_match"] and agent["ontology_scope"] != issued_token["scope"]:
        return False, "ontology scope mismatch"
    if not agent["actions"]:
        return False, "agent has no declared actions"
    return True, "ok"

def structural_score(layer):
    nodes, edges, tests = len(layer["nodes"]), len(layer["edges"]), len(layer["tests"])
    return round(min(1.0, 0.30 + 0.02 * nodes + 0.01 * edges + 0.08 * tests), 3)

def load_state():
    p = STATE / "state.json"
    if not p.exists():
        return {"iteration": 0, "active_layers": [], "agents": [], "history": []}
    return json.loads(p.read_text())

def save_state(state):
    (STATE / "state.json").write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")

def main():
    state = load_state()
    existing = current_layers()
    if len(existing) >= CONFIG["max_total_layers"]:
        print("Layer ceiling reached; no generation performed.")
        return
    iteration = state["iteration"] + 1
    prompt = f"""
Iteration: {iteration}
Accepted layers: {len(existing)}
Active agents: {len(state.get("agents", []))}

Generate up to {CONFIG["max_layers_per_run"]} NEW layer specifications and, where useful,
one or more agent specifications that can operate those layers.

Agent format:
{{"agent_id":"agent-N","role":"...","ontology_scope":"...",
"actions":["observe","compare","propose"],"conflict_policy":"lease_then_arbitrate",
"provenance_required":true}}

Layer format:
{{"layer_id":"layer-N","purpose":"...",
"nodes":[{{"id":"n1","role":"...","operation":"..."}}],
"edges":[{{"from":"n1","to":"n2","condition":"..."}}],
"tests":[{{"name":"...","assertion":"..."}}]}}

Rules:
- no executable code;
- no invented provenance;
- no agent may write another agent's state;
- every agent has one explicit ontology scope;
- agents may propose but the governor validates;
- do not create duplicate agents merely to increase count;
- a new layer must add a genuinely new structural relation.
Return JSON object: {{"layers":[...],"agents":[...]}}.
"""
    proposal = call_model(prompt)
    layers = proposal.get("layers", []) if isinstance(proposal, dict) else []
    agents = proposal.get("agents", []) if isinstance(proposal, dict) else []
    promoted, accepted_agents = [], []

    for agent in agents:
        scope = agent.get("ontology_scope", "")
        token = issue_ontology_credit(agent.get("agent_id", "unknown"), scope, iteration,
                                      CONFIG["agent_governance"]["default_ontology_credits"])
        ok, reason = validate_agent(agent, token)
        if ok and len(state["agents"]) + len(accepted_agents) < CONFIG["agent_governance"]["max_active_agents"]:
            record = {**agent, "ontology_token": token}
            path = AGENTS / f"{agent['agent_id']}.json"
            path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
            accepted_agents.append(record)
        else:
            print(f"Rejected agent: {reason}")

    for layer in layers[:CONFIG["max_layers_per_run"]]:
        ok, reason = validate_layer(layer)
        score = structural_score(layer) if ok else 0.0
        if ok and score >= CONFIG["promotion_threshold"]:
            text = json.dumps(layer, indent=2, ensure_ascii=False) + "\n"
            digest = sha(text)
            path = LAYERS / f"{layer['layer_id']}-{digest[:10]}.json"
            path.write_text(text)
            promoted.append({"layer_id": layer["layer_id"], "sha256": digest, "score": score})
        else:
            print(f"Rejected layer: {reason}; score={score}")

    state["iteration"] = iteration
    state["active_layers"].extend(promoted)
    state["agents"].extend([{
        "agent_id": a["agent_id"], "role": a["role"],
        "ontology_scope": a["ontology_scope"],
        "token_id": a["ontology_token"]["token_id"]
    } for a in accepted_agents])
    state["history"].append({"iteration": iteration, "promoted_layers": promoted,
                             "accepted_agents": [a["agent_id"] for a in accepted_agents]})
    save_state(state)
    print(json.dumps({"iteration": iteration, "promoted_layers": promoted,
                      "accepted_agents": [a["agent_id"] for a in accepted_agents]}, indent=2))

if __name__ == "__main__":
    main()
