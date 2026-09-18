"""Imperial Account: append-only billable action ledger for institutions."""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from decimal import Decimal
from hashlib import sha256
import json

@dataclass(frozen=True)
class UsageEvent:
    event_id: str
    institution_id: str
    action: str
    audit_id: str
    master_hash: str
    units: int
    unit_price: str
    currency: str
    timestamp: str

class ImperialAccount:
    def __init__(self, institution_id: str, currency: str = "ILS"):
        self.institution_id = institution_id
        self.currency = currency
        self.events: list[UsageEvent] = []

    def record(self, action: str, audit_id: str, master_hash: str,
               unit_price: Decimal, units: int = 1) -> UsageEvent:
        if len(master_hash) != 64:
            raise ValueError("master_hash must be SHA-256 hex")
        int(master_hash, 16)
        if units < 1:
            raise ValueError("units must be >= 1")
        n = len(self.events) + 1
        event_id = "USE-" + str(n).zfill(12)
        event = UsageEvent(event_id, self.institution_id, action, audit_id,
                           master_hash.lower(), units, format(unit_price, "f"),
                           self.currency, datetime.now(timezone.utc).isoformat())
        self.events.append(event)
        return event

    def summary(self):
        totals = {}
        for e in self.events:
            totals[e.action] = totals.get(e.action, 0) + e.units
        amount = sum(Decimal(e.unit_price) * e.units for e in self.events)
        return {"institution_id": self.institution_id, "currency": self.currency,
                "actions": totals, "total_units": sum(totals.values()),
                "total_amount": format(amount, "f"), "events": len(self.events)}

    def export(self) -> str:
        payload = [asdict(e) for e in self.events]
        return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

    def ledger_hash(self) -> str:
        return sha256(self.export().encode("utf-8")).hexdigest()
