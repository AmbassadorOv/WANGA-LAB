import json
import tempfile
import unittest
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("global_work_manager", ROOT / "scripts" / "global_work_manager.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class GlobalWorkManagerTests(unittest.TestCase):
    def test_plan_has_all_subsystems(self):
        state = {"repository":"AmbassadorOv/WANGA-LAB","build_branch":"autobuild/architecture-construction","main_branch":"main","review_policy":"review-at-end"}
        plan = module.build_plan(state)
        self.assertEqual(plan["manager"], "WANGA_GLOBAL_WORK_MANAGER_V2")
        self.assertEqual(plan["version"], 2)
        self.assertEqual(plan["task_count"], len(module.SUBSYSTEMS))
        self.assertTrue(all(t["verification_required"] for t in plan["tasks"]))
        self.assertIn("no_direct_main_changes", plan["invariants"])

    def test_external_agent_controls_are_present(self):
        state = {"repository":"AmbassadorOv/WANGA-LAB","build_branch":"autobuild/architecture-construction","main_branch":"main","review_policy":"review-at-end"}
        plan = module.build_plan(state)
        self.assertTrue(plan["graph_policy"]["checkpoint_resume"])
        self.assertTrue(plan["graph_policy"]["verification_is_promotion_gate"])
        for task in plan["tasks"]:
            execution = task["execution"]
            self.assertTrue(execution["idempotency_required"])
            self.assertTrue(execution["trace_required"])
            self.assertEqual(execution["handoff_policy"], "BOUNDED_CAPABILITY_HANDOFF")
            self.assertEqual(execution["evaluation_loop"]["max_iterations"], 3)
            self.assertTrue(execution["evaluation_loop"]["acceptance_criteria_locked"])

    def test_output_is_json(self):
        state = {"repository":"AmbassadorOv/WANGA-LAB","build_branch":"autobuild/architecture-construction","main_branch":"main","review_policy":"review-at-end"}
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "plan.json"
            out.write_text(json.dumps(module.build_plan(state)), encoding="utf-8")
            loaded = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(loaded["task_count"], 12)
            self.assertEqual(loaded["pattern_profile"], "EXTERNAL_AGENT_PATTERN_INTEGRATION_V1")

if __name__ == "__main__":
    unittest.main()
