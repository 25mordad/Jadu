#!/usr/bin/env python3
"""
check_usage_margin.py — free pre-check that keeps jadu-loop inside the plan's
own limits, so it never runs into usage credits (extra usage) unasked.

Queries `claude -p "/usage"` (headless, no model turn, $0) and answers one of:
  GO   (exit 0) — every limit is under its line, run the next task
  WAIT (exit 2) — a limit is at/over its line; sleep and check again later
  STOP (exit 1) — something is wrong (not on the subscription, API key set,
                  wrong login, usage unreadable); a human has to look

The 5-hour and weekly limits are judged separately, each with two lines:
  start   — a new task starts only while usage is under this
  ceiling — a task already running is stopped (by run_loop.py's watchdog) here
The gap between them is room for a started task to finish. Usage only drops
when a limit resets, so "back under the start line" means "it has reset".

Notifies once per pause (not every tick) and once on resume.

Usage:
    python3 scripts/jadu-loop/check_loop_queue.py \
      && python3 scripts/jadu-loop/check_usage_margin.py \
      && claude -p "/jadu-loop" --model opus
    python3 scripts/jadu-loop/check_usage_margin.py --watch   # judge against the ceilings
"""

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# name: (regex on the /usage text, start line %, ceiling %)
LIMITS = {
    "5-hour": (re.compile(r"Current session:\s*(\d+)% used(?:\s*·\s*resets\s*(.+))?"), 80, 90),
    "weekly": (
        re.compile(r"Current week \(all models\):\s*(\d+)% used(?:\s*·\s*resets\s*(.+))?"),
        95,
        98,
    ),
}
SUBSCRIPTION_LINE = "using your subscription"

GO, STOP, WAIT = 0, 1, 2

REPO_ROOT = Path.cwd()
FLAG_FILE = REPO_ROOT / ".loop_state" / "usage_margin_hit"
NOTIFY_SCRIPT = Path(__file__).resolve().parent / "notify_telegram.py"


def _claude(*args: str) -> str:
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    # chat_usage_guard.py skips itself inside this call, so the hook never recurses.
    env["JADU_USAGE_CHECK"] = "1"
    proc = subprocess.run(
        [shutil.which("claude") or "claude", *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
        env=env,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"claude {' '.join(args)} exited {proc.returncode}: {proc.stderr.strip()}"
        )
    return proc.stdout


def fetch_usage_text() -> str:
    return json.loads(_claude("-p", "/usage", "--output-format", "json")).get("result", "")


def fetch_auth_method() -> str:
    return json.loads(_claude("auth", "status")).get("authMethod", "")


def parse_usage(text: str) -> dict[str, tuple[int, str]]:
    """{limit name: (percent used, reset text)} for every limit found in the text."""
    found = {}
    for name, (regex, _, _) in LIMITS.items():
        m = regex.search(text)
        if m:
            found[name] = (int(m.group(1)), (m.group(2) or "").strip())
    return found


def decide(text: str, auth_method: str, env: dict, watch: bool = False) -> tuple[int, str]:
    """Pure decision: (GO/WAIT/STOP, one-line reason)."""
    if env.get("ANTHROPIC_API_KEY"):
        return STOP, "ANTHROPIC_API_KEY is set — runs would bill that key, not the subscription"
    if auth_method != "claude.ai":
        return STOP, f"logged in via {auth_method!r}, not the claude.ai subscription"
    if SUBSCRIPTION_LINE not in text:
        return STOP, "/usage does not say 'using your subscription' — would spend usage credits"
    usage = parse_usage(text)
    missing = [name for name in LIMITS if name not in usage]
    if missing:
        return WAIT, f"could not read {', '.join(missing)} usage from /usage"
    over = []
    for name, (_, start, ceiling) in LIMITS.items():
        pct, resets = usage[name]
        line = ceiling if watch else start
        if pct >= line:
            over.append(f"{name} at {pct}% (line {line}%, resets {resets or '?'})")
    summary = ", ".join(f"{n} {usage[n][0]}%" for n in LIMITS)
    if over:
        return WAIT, "paused: " + "; ".join(over)
    return GO, f"ok: {summary}"


def check(watch: bool = False) -> tuple[int, str]:
    try:
        return decide(fetch_usage_text(), fetch_auth_method(), dict(os.environ), watch)
    except Exception as e:  # unreadable usage is never treated as fine
        return WAIT, f"usage check failed: {e}"


def notify(message: str) -> None:
    if NOTIFY_SCRIPT.exists():
        subprocess.run(
            [sys.executable, str(NOTIFY_SCRIPT), message], capture_output=True, text=True
        )


def notify_change(verdict: int, reason: str) -> None:
    """Message once when a pause/stop starts and once when it ends, not every tick."""
    if verdict == GO:
        if FLAG_FILE.exists():
            FLAG_FILE.unlink()
            notify(f"usage back under the lines — jadu-loop resuming ({reason})")
        return
    kind = "stop" if verdict == STOP else "wait"
    if not FLAG_FILE.exists() or FLAG_FILE.read_text(encoding="utf-8").strip() != kind:
        FLAG_FILE.parent.mkdir(parents=True, exist_ok=True)
        FLAG_FILE.write_text(kind + "\n", encoding="utf-8")
        notify(("STOPPED, needs you: " if verdict == STOP else "") + reason)


def main() -> None:
    verdict, reason = check(watch="--watch" in sys.argv)
    notify_change(verdict, reason)
    print(reason, file=sys.stderr)
    sys.exit(verdict)


if __name__ == "__main__":
    main()
