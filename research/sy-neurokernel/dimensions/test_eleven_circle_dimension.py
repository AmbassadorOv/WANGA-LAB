import json
from pathlib import Path

p = Path(__file__).parents[1] / "eleven_circle_dimension.json"
data = json.loads(p.read_text(encoding="utf-8"))

assert data["status"] == "PROTOTYPED"
assert data["invariants"]["dimension_count"] == 11
assert data["invariants"]["source_rows"] == [1,3,5,7,9,11,13,15,17,19,21]
assert len(data["dimensions"]) == 11
assert all(d["circle"] is True for d in data["dimensions"])
assert all(d["source_row"] % 2 == 1 for d in data["dimensions"])
assert data["invariants"]["neural_layer_may_not_create_dimensions"] is True
print("11-circle dimension invariants: PASS")
