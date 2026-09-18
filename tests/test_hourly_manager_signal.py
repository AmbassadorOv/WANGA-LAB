import json
import tempfile
import unittest
from pathlib import Path

from scripts.hourly_manager_signal import actionable_tasks


class HourlyManagerSignalTests(unittest.TestCase):
    def test_detects_actionable_status(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "plan.json"
            p.write_text(json.dumps({"tasks": [{"status": "READY"}, {"status": "COMPLETE"}]}), encoding="utf-8")
            self.assertEqual(len(actionable_tasks(str(p))), 1)

    def test_missing_plan_is_not_actionable(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(actionable_tasks(str(Path(d) / "missing.json")), [])


if __name__ == "__main__":
    unittest.main()
