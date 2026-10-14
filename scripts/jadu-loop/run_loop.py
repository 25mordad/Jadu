#!/usr/bin/env python3
"""
run_loop.py — runs jadu-loop task after task, unattended, without ever
running into usage credits.

Before each run: check_loop_queue.py (anything to do?), then the usage gate
  (check_usage_margin.py). WAIT -> sleep POLL_SECONDS and ask again, however
  long it takes (a weekly limit can mean days). STOP -> notify and exit.
During a run: a watchdog asks the gate against the ceilings every
  WATCH_SECONDS and kills the run once a limit reaches its ceiling (or the
  subscription line disappears). LOOP_TASK.md holds the progress, so the next
  run picks the task back up after the reset.
After a run: three runs in a row that change nothing stop the loop.

Usage:
    python3 scripts/jadu-loop/run_loop.py                        # /jadu-loop
    python3 scripts/jadu-loop/run_loop.py "/jadu-loop-best-practice"
"""

import argparse
import hashlib
import os
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_usage_margin as usage  # noqa: E402

MODEL = "opus"  # always named: Fable models bill usage credits in -p mode
POLL_SECONDS = 600
WATCH_SECONDS = 180
PAUSE_SECONDS = 20
MAX_STALLS = 3

ROOT = Path.cwd()
LOG = ROOT / ".loop_state" / "runs.log"
QUEUE_GATE = Path(__file__).resolve().parent / "check_loop_queue.py"
CLAUDE_CMD = [shutil.which("claude") or "claude"]


def log(line: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')} {line}\n")


def progress_state() -> str:
    h = hashlib.md5()
    task = ROOT / "LOOP_TASK.md"
    if task.exists():
        h.update(task.read_bytes())
    for name in ("LOOP_TASK_ARCHIVE", "LOOP_TASK_QUEUE"):
        folder = ROOT / name
        if folder.is_dir():
            h.update("\n".join(sorted(p.name for p in folder.iterdir())).encode())
    return h.hexdigest()


def wait_for_go(sleep=time.sleep) -> bool:
    """Sleep until the usage gate says GO. False means STOP (a human must look)."""
    while True:
        verdict, reason = usage.check()
        usage.notify_change(verdict, reason)
        log(f"usage: {reason}")
        if verdict == usage.GO:
            return True
        if verdict == usage.STOP:
            return False
        sleep(POLL_SECONDS)


def kill_tree(proc: subprocess.Popen) -> None:
    if os.name == "nt":
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], capture_output=True)
    else:
        os.killpg(proc.pid, signal.SIGTERM)
    proc.wait()


def run_task(prompt: str) -> str | None:
    """One `claude -p` run under the watchdog. Returns why it was killed, or None."""
    out_file = ROOT / ".loop_state" / "last_run.out"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    cmd = [*CLAUDE_CMD, "-p", prompt, "--model", MODEL, "--permission-mode", "acceptEdits"]
    killed = None
    with out_file.open("w", encoding="utf-8") as out:
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=out,
            stderr=subprocess.STDOUT,
            cwd=ROOT,
            env=env,
            start_new_session=os.name != "nt",
        )
        while True:
            try:
                proc.wait(timeout=WATCH_SECONDS)
                break
            except subprocess.TimeoutExpired:
                verdict, reason = usage.check(watch=True)
                if verdict != usage.GO:
                    killed = reason
                    kill_tree(proc)
                    break
    with LOG.open("a", encoding="utf-8") as f:
        f.write(out_file.read_text(encoding="utf-8", errors="replace"))
    return killed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run jadu-loop unattended inside the plan's limits"
    )
    parser.add_argument("prompt", nargs="?", default="/jadu-loop")
    parser.add_argument("--max-runs", type=int, default=80)
    args = parser.parse_args(argv)

    stalls = 0
    for i in range(1, args.max_runs + 1):
        if subprocess.run([sys.executable, str(QUEUE_GATE)], cwd=ROOT).returncode != 0:
            log("queue gate: nothing to do, loop finished")
            return 0
        if not wait_for_go():
            log("usage gate said STOP, loop needs a human")
            return 1
        before = progress_state()
        log(f"=== run {i} ===")
        killed = run_task(args.prompt)
        if killed:
            log(f"watchdog stopped the run: {killed}")
            usage.notify(f"watchdog stopped a run, will resume after the reset: {killed}")
            continue  # wait_for_go sleeps until the limit resets
        stalls = stalls + 1 if progress_state() == before else 0
        if stalls >= MAX_STALLS:
            log(f"no progress in {MAX_STALLS} runs, stopping")
            usage.notify(f"jadu-loop stopped: no progress in {MAX_STALLS} runs")
            return 1
        time.sleep(PAUSE_SECONDS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
