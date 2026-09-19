"""WANGA System Governance Kernel V1."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
import json
from typing import Any

class Status(str, Enum):
    UNKNOWN="UNKNOWN"; DECLARED="DECLARED"; PARTIALLY_VERIFIED="PARTIALLY_VERIFIED"
    VERIFIED="VERIFIED"; CHANGED="CHANGED"; CONTESTED="CONTESTED"; EXPIRED="EXPIRED"

@dataclass(frozen=True)
class Link:
    relation: str
    target: str

@dataclass
class GovernanceObject:
    object_id: str
    object_type: str
    status: Status = Status.UNKNOWN
    source_refs: list[str] = field(default_factory=list)
    links: list[Link] = field(default_factory=list)
    verification_refs: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def canonical(self) -> dict[str, Any]:
        return {
            "id": self.object_id, "type": self.object_type, "status": self.status.value,
            "source_refs": sorted(self.source_refs),
            "links": [{"relation": x.relation, "target": x.target}
                      for x in sorted(self.links, key=lambda x:(x.relation,x.target))],
            "verification_refs": sorted(self.verification_refs),
            "metadata": self.metadata,
        }

class GovernanceKernel:
    def __init__(self) -> None:
        self.objects: dict[str, GovernanceObject] = {}

    def add(self, obj: GovernanceObject) -> None:
        if obj.object_id in self.objects:
            raise ValueError(f"duplicate object_id: {obj.object_id}")
        self.objects[obj.object_id] = obj

    def link(self, source_id: str, relation: str, target_id: str) -> None:
        if source_id not in self.objects or target_id not in self.objects:
            raise KeyError("both source and target must exist")
        self.objects[source_id].links.append(Link(relation, target_id))

    def set_status(self, object_id: str, status: Status) -> None:
        self.objects[object_id].status = status

    def connected(self, object_id: str) -> list[GovernanceObject]:
        ids = {x.target for x in self.objects[object_id].links}
        return [self.objects[i] for i in sorted(ids) if i in self.objects]

    def audit_digest(self) -> str:
        payload = [self.objects[k].canonical() for k in sorted(self.objects)]
        encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        return sha256(encoded).hexdigest()

    def export(self) -> dict[str, Any]:
        return {"schema":"wanga-governance-v1",
                "objects":[self.objects[k].canonical() for k in sorted(self.objects)],
                "audit_digest":self.audit_digest()}

def demo_network() -> GovernanceKernel:
    k=GovernanceKernel()
    k.add(GovernanceObject("asset:001","asset",Status.DECLARED,["doc:001"]))
    k.add(GovernanceObject("doc:001","document",Status.VERIFIED,["source:001"]))
    k.add(GovernanceObject("insurer:001","institution",Status.VERIFIED,["registry:001"]))
    k.add(GovernanceObject("policy:001","insurance",Status.DECLARED,["policy-doc:001"]))
    k.add(GovernanceObject("verify:001","verification",Status.VERIFIED,["verifier:001"]))
    k.link("asset:001","supported_by","doc:001")
    k.link("asset:001","insured_by","insurer:001")
    k.link("asset:001","covered_under","policy:001")
    k.link("policy:001","verified_by","verify:001")
    return k
