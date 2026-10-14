import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "jadu-loop"))
import check_usage_margin as usage  # noqa: E402
import run_loop  # noqa: E402


class RunLoopTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        for name, value in {
            "ROOT": self.root,
            "LOG": self.root / "runs.log",
            "WATCH_SECONDS": 0.2,
        }.items():
            patcher = mock.patch.object(run_loop, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        patcher = mock.patch.object(usage, "notify_change")
        patcher.start()
        self.addCleanup(patcher.stop)

    def fake_claude(self, body: str) -> None:
        script = self.root / "fake_claude.py"
        script.write_text(body, encoding="utf-8")
        run_loop.CLAUDE_CMD = [sys.executable, str(script)]

    def test_wait_sleeps_until_the_limit_resets(self):
        verdicts = [(usage.WAIT, "5-hour at 85%"), (usage.WAIT, "5-hour at 85%"), (usage.GO, "ok")]
        sleeps = []
        with mock.patch.object(usage, "check", side_effect=verdicts):
            self.assertTrue(run_loop.wait_for_go(sleep=sleeps.append))
        self.assertEqual(sleeps, [run_loop.POLL_SECONDS] * 2)

    def test_stop_ends_the_wait(self):
        with mock.patch.object(usage, "check", return_value=(usage.STOP, "not on subscription")):
            self.assertFalse(
                run_loop.wait_for_go(sleep=lambda s: self.fail("must not sleep on STOP"))
            )

    def test_watchdog_kills_a_run_at_the_ceiling(self):
        self.fake_claude("import time; print('working', flush=True); time.sleep(30)")
        started = time.monotonic()
        with mock.patch.object(usage, "check", return_value=(usage.WAIT, "5-hour at 90%")):
            killed = run_loop.run_task("/jadu-loop")
        self.assertEqual(killed, "5-hour at 90%")
        self.assertLess(time.monotonic() - started, 15)

    def test_run_under_the_ceiling_finishes(self):
        self.fake_claude("import time; time.sleep(0.5); print('done')")
        with mock.patch.object(usage, "check", return_value=(usage.GO, "ok")):
            self.assertIsNone(run_loop.run_task("/jadu-loop"))
        self.assertIn("done", (self.root / "runs.log").read_text(encoding="utf-8"))

    def test_loop_exits_when_the_gate_says_stop(self):
        (self.root / "LOOP_TASK.md").write_text(
            "STATUS: idle\n\n- [ ] 1. Do it\n", encoding="utf-8"
        )
        with (
            mock.patch.object(usage, "check", return_value=(usage.STOP, "api key set")),
            mock.patch.object(run_loop, "run_task") as run_task,
        ):
            self.assertEqual(run_loop.main([]), 1)
        run_task.assert_not_called()


if __name__ == "__main__":
    unittest.main()
