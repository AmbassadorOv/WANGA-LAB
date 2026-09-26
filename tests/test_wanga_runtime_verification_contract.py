import unittest

from wanga_runtime.core import WangaRuntime, Task


class WangaRuntimeVerificationContractTests(unittest.TestCase):
    def test_handler_failure_emits_failed_execution_without_verify_pass(self):
        def failing_handler(task: Task):
            return {
                "role": task.role,
                "task_id": task.task_id,
                "input": task.input,
                "status": "FAILED",
                "reason": "synthetic_failure",
            }

        runtime = WangaRuntime(
            handlers={
                "planner": failing_handler,
                "implementer": failing_handler,
                "verifier": failing_handler,
            }
        )
        report = runtime.run({"question": "failure-boundary"})

        self.assertEqual(report["verification_status"], "FAILED")
        self.assertEqual(
            report["state"],
            ["INGESTED", "ROUTED:planner", "FAILED"],
        )
        self.assertEqual(report["evidence"][-1]["stage"], "PLANNER")
        self.assertEqual(report["evidence"][-1]["status"], "FAILED")
        self.assertNotIn("VERIFY", [item["stage"] for item in report["evidence"]])

    def test_evidence_digest_is_stable_for_identical_failure(self):
        def failing_handler(task: Task):
            return {
                "role": task.role,
                "task_id": task.task_id,
                "input": task.input,
                "status": "FAILED",
                "reason": "stable_failure",
            }

        runtime = WangaRuntime(
            handlers={
                "planner": failing_handler,
                "implementer": failing_handler,
                "verifier": failing_handler,
            }
        )
        first = runtime.run({"question": "stable"})
        second = runtime.run({"question": "stable"})

        self.assertEqual(first, second)
        self.assertEqual(first["evidence"][0]["digest"], second["evidence"][0]["digest"])


if __name__ == "__main__":
    unittest.main()
