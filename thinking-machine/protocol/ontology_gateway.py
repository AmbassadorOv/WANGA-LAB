"""
Ontology Communication Gateway

External AI does not enter a governed Thinking Machine namespace by
default. It requests a scoped communication lease.

ONTO_CREDIT is a non-monetary access/coordination credential.
Commercial licensing can later map to credits, but this module
does not implement payments or financial settlement.
"""

from dataclasses import dataclass
from typing import Dict, List
import hashlib
import json
import time

from weight_engine import WeightFactors, structural_weight, access_weight_required

@dataclass(frozen=True)
class OntologyCredit:
    token_id: str
    issuer: str
    subject: str
    ontology_scope: str
    credits: int
    iteration: int
    issued_at: int
    nonce: str
    signature: str

def mint_credit(issuer: str, subject: str, ontology_scope: str,
                credits: int, iteration: int, nonce: str) -> OntologyCredit:
    body = {
        "issuer": issuer,
        "subject": subject,
        "ontology_scope": ontology_scope,
        "credits": int(credits),
        "iteration": int(iteration),
        "nonce": nonce,
    }
    raw = json.dumps(body, sort_keys=True, ensure_ascii=False)
    sig = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    token_id = "ONTO-" + sig[:20]
    return OntologyCredit(
        token_id=token_id,
        issuer=issuer,
        subject=subject,
        ontology_scope=ontology_scope,
        credits=int(credits),
        iteration=int(iteration),
        issued_at=int(time.time()),
        nonce=nonce,
        signature=sig,
    )

def validate_handshake(request: Dict, credit: OntologyCredit,
                       required_scope: str, factors: WeightFactors) -> Dict:
    reasons: List[str] = []
    if request.get("subject") != credit.subject:
        reasons.append("subject_mismatch")
    if request.get("ontology_scope") != required_scope:
        reasons.append("ontology_scope_mismatch")
    if request.get("ontology_scope") != credit.ontology_scope:
        reasons.append("credit_scope_mismatch")
    if credit.credits < int(request.get("credits_required", 1)):
        reasons.append("insufficient_ontology_credit")
    if not request.get("provenance"):
        reasons.append("provenance_required")

    weight = structural_weight(factors)
    threshold = access_weight_required(factors)
    claimed_weight = float(request.get("structural_weight", 0.0))
    if claimed_weight < threshold:
        reasons.append("structural_weight_below_gate")

    return {
        "status": "REJECTED" if reasons else "ALLOWED",
        "reasons": reasons,
        "structural_weight": weight,
        "required_weight": threshold,
        "token_id": credit.token_id,
        "scope": credit.ontology_scope,
    }
