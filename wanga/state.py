"""
WANGA State Transition Engine Component
"""

import hashlib
import time
from enum import Enum
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field, ConfigDict
from wanga.matrix import OntologicalMatrix


class StateStage(str, Enum):
    POTENTIAL = "POTENTIAL"            # Undifferentiated state / candidate possibilities
    CONFIGURED = "CONFIGURED"          # Relational matrix mapped
    CANDIDATE = "CANDIDATE"            # Formulated state candidates
    BIRUR = "BIRUR"                    # Under constraint evaluation & clarification
    RESOLVED = "RESOLVED"              # Constraint-satisfying state selected
    ACTUALIZED = "ACTUALIZED"          # Executed / Realized


class CandidateState(BaseModel):
    model_config = ConfigDict(extra="ignore")
    candidate_id: str
    payload: Dict[str, Any]
    score: float = 0.0
    valid: bool = True
    reasoning_chain: List[str] = Field(default_factory=list)


class OntologicalStateEngine:
    """
    Manages deterministic state transitions: Potential -> Configured -> Candidate -> Birur -> Resolved -> Actualized
    """

    def __init__(self, matrix: Optional[OntologicalMatrix] = None):
        self.matrix = matrix or OntologicalMatrix()
        self.current_stage = StateStage.POTENTIAL
        self.candidates: List[CandidateState] = []
        self.constraints: List[Dict[str, Any]] = []
        self.resolved_state: Optional[CandidateState] = None
        self.audit_history: List[Dict[str, Any]] = []

    def log_event(self, action: str, details: Dict[str, Any]):
        entry = {
            "timestamp": time.time(),
            "stage": self.current_stage.value,
            "action": action,
            "details": details
        }
        self.audit_history.append(entry)

    def transition_to_configured(self, configuration_params: Dict[str, Any]):
        if self.current_stage != StateStage.POTENTIAL:
            raise ValueError(f"Invalid state transition from {self.current_stage} to CONFIGURED")
        self.current_stage = StateStage.CONFIGURED
        self.log_event("TRANSITION_CONFIGURED", configuration_params)

    def generate_candidates(self, candidate_payloads: List[Dict[str, Any]]):
        if self.current_stage != StateStage.CONFIGURED:
            raise ValueError(f"Invalid state transition from {self.current_stage} to CANDIDATE")
        self.current_stage = StateStage.CANDIDATE
        self.candidates = [
            CandidateState(candidate_id=f"cand-{idx+1}", payload=p)
            for idx, p in enumerate(candidate_payloads)
        ]
        self.log_event("GENERATE_CANDIDATES", {"candidate_count": len(self.candidates)})

    def run_birur_clarification(self, constraint_rules: List[Dict[str, Any]]) -> List[CandidateState]:
        """
        Birur phase: Evaluates candidate states against constraint rules.
        """
        if self.current_stage not in (StateStage.CANDIDATE, StateStage.BIRUR):
            raise ValueError(f"Invalid state transition from {self.current_stage} to BIRUR")
        self.current_stage = StateStage.BIRUR
        self.constraints = constraint_rules

        valid_candidates = []
        for cand in self.candidates:
            cand_valid = True
            cand_score = 100.0
            for rule in constraint_rules:
                req_key = rule.get("required_key")
                min_val = rule.get("min_value")
                if req_key and req_key not in cand.payload:
                    cand_valid = False
                    cand.reasoning_chain.append(f"Failed rule: missing key '{req_key}'")
                    break
                if min_val is not None and cand.payload.get(req_key, 0) < min_val:
                    cand_valid = False
                    cand.reasoning_chain.append(f"Failed rule: '{req_key}' < {min_val}")
                    break

            cand.valid = cand_valid
            cand.score = cand_score if cand_valid else 0.0
            if cand_valid:
                valid_candidates.append(cand)

        self.log_event("BIRUR_CLARIFICATION", {"evaluated": len(self.candidates), "passed": len(valid_candidates)})
        return valid_candidates

    def resolve_state(self) -> CandidateState:
        if self.current_stage != StateStage.BIRUR:
            raise ValueError("Birur clarification must be run before resolution")

        valid_candidates = [c for c in self.candidates if c.valid]
        if not valid_candidates:
            raise RuntimeError("Birur phase produced no valid candidate states; resolution failed")

        selected = max(valid_candidates, key=lambda c: c.score)
        self.resolved_state = selected
        self.current_stage = StateStage.RESOLVED
        self.log_event("STATE_RESOLVED", {"resolved_candidate_id": selected.candidate_id})
        return selected

    def actualize_state(self) -> Dict[str, Any]:
        if self.current_stage != StateStage.RESOLVED or not self.resolved_state:
            raise ValueError("State must be RESOLVED before actualization")

        self.current_stage = StateStage.ACTUALIZED
        canonical_str = str(self.resolved_state.payload)
        state_hash = hashlib.sha256(canonical_str.encode("utf-8")).hexdigest()

        actualized_output = {
            "stage": self.current_stage.value,
            "resolved_id": self.resolved_state.candidate_id,
            "payload": self.resolved_state.payload,
            "state_witness_hash": state_hash,
            "timestamp": time.time()
        }
        self.log_event("STATE_ACTUALIZED", {"witness_hash": state_hash})
        return actualized_output
