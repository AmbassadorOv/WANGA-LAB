"""Provider-neutral executable NTM core for the first local POC."""
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any, Callable

STATUSES={"OBSERVATION","DIFFERENCE","CANDIDATE","VERIFIED_FINDING","ARCHITECTURAL_CHANGE"}

@dataclass
class TaskEnvelope:
    request_id: str
    task_id: str
    node_role: str
    system_spec_version: str
    input: Any
    constraints: list[str]=field(default_factory=list)
    expected_output_schema: dict[str,Any]=field(default_factory=dict)

@dataclass
class NodeResult:
    request_id: str
    task_id: str
    node_role: str
    model_id: str
    output: Any
    evidence_refs: list[str]=field(default_factory=list)
    uncertainty: str="UNKNOWN"
    status: str="COMPLETED"

class ModelAdapter:
    model_id="deterministic-local-v1"
    def health(self)->bool: return True
    def capabilities(self)->list[str]: return ["analysis","deterministic"]
    def generate(self, request: TaskEnvelope)->NodeResult:
        payload={"input":request.input,"constraints":request.constraints}
        return NodeResult(request.request_id,request.task_id,request.node_role,self.model_id,payload)

class NTMOrchestrator:
    def __init__(self, adapters=None):
        self.adapters=adapters or {"deterministic":ModelAdapter()}
    @staticmethod
    def task_id(request_id:str, value:Any)->str:
        raw=f"{request_id}|{repr(value)}".encode()
        return sha256(raw).hexdigest()[:16]
    def run(self, user_input:Any, roles=("planner","verifier"))->dict[str,Any]:
        request_id=f"req-{sha256(repr(user_input).encode()).hexdigest()[:12]}"
        task_id=self.task_id(request_id,user_input)
        results=[]
        for role in roles:
            env=TaskEnvelope(request_id,task_id,role,"NTM_V1",user_input)
            adapter=self.adapters["deterministic"]
            results.append(asdict(adapter.generate(env)))
        verified=all(r["status"]=="COMPLETED" for r in results)
        return {
            "request_id":request_id,
            "task_id":task_id,
            "pipeline":["INGEST","ROUTE","ANALYZE","VERIFY","SYNTHESIZE"],
            "results":results,
            "verification_status":"PASSED" if verified else "FAILED",
            "reasoning_status":"VERIFIED_FINDING" if verified else "CANDIDATE",
            "unresolved_questions":[],
        }
