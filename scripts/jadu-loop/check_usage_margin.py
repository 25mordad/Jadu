#!/usr/bin/env python3
"""
check_usage_margin.py — cheap, free pre-check gating jadu-loop invocations on
a shared account's rate-limit/usage window. Queries `claude -p "/usage"`
(headless, zero API cost for Claude Code's Max-plan usage command) and blocks
if either the current-session or current-week (all models) percentage is at
or above MARGIN_PERCENT. Notifies once per crossing (not every tick) and
auto-clears once usage drops back under margin — no manual reset needed.

Fails closed: if the usage check itself can't be read (invocation error,
unparseable output), this blocks and notifies rather than silently letting
jadu-loop proceed on an unknown usage state.

This script assumes Claude Code's `/usage` output format. If you're running
jadu-loop with a different agent CLI, either adapt fetch_usage_text()/
parse_percentages() to that CLI's equivalent, or delete this pre-check from
the invocation chain entirely — it's optional, not load-bearing.

Usage:
    python3 scripts/jadu-loop/check_loop_queue.py \
      && python3 scripts/jadu-loop/check_usage_margin.py \
      && claude -p "/jadu-loop"
"""

import json
import re
import subprocess
import sys
from pathlib import Path

MARGIN_PERCENT = 80

REPO_ROOT = Path.cwd()
FLAG_FILE = REPO_ROOT / ".loop_state" / "usage_margin_hit"
NOTIFY_SCRIPT = REPO_ROOT / "scripts" / "jadu-loop" / "notify_telegram.py"

SESSION_RE = re.compile(r"Current session:\s*(\d+)% used")
WEEKLY_RE = re.compile(r"Current week \(all models\):\s*(\d+)% used")


def fetch_usage_text() -> str:
    proc = subprocess.run(
        ["claude", "-p", "/usage", "--output-format", "json"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"claude -p /usage exited {proc.returncode}: {proc.stderr.strip()}")
    data = json.loads(proc.stdout)
    return data.get("result", "")


def parse_percentages(text: str) -> tuple[int | None, int | None]:
    session_match = SESSION_RE.search(text)
    weekly_match = WEEKLY_RE.search(text)
    session = int(session_match.group(1)) if session_match else None
    weekly = int(weekly_match.group(1)) if weekly_match else None
    return session, weekly


def notify(message: str) -> None:
    if not NOTIFY_SCRIPT.exists():
        return
    subprocess.run(
        ["python3", str(NOTIFY_SCRIPT), message],
        capture_output=True,
        text=True,
    )


def main() -> None:
    try:
        text = fetch_usage_text()
        session, weekly = parse_percentages(text)
        if session is None and weekly is None:
            raise ValueError(f"could not parse session/weekly percentages from: {text!r}")
    except Exception as e:
        print(f"usage check failed, failing closed: {e}", file=sys.stderr)
        notify(f"usage-margin check failed ({e}) — blocking jadu-loop until this is fixed")
        sys.exit(1)

    highest = max(v for v in (session, weekly) if v is not None)

    if highest >= MARGIN_PERCENT:
        if not FLAG_FILE.exists():
            FLAG_FILE.parent.mkdir(parents=True, exist_ok=True)
            FLAG_FILE.write_text(f"{highest}\n")
            first_line = text.splitlines()[0] if text else ""
            notify(
                f"usage margin reached ({highest}% >= {MARGIN_PERCENT}%) — "
                f"pausing jadu-loop until usage drops back down.\n{first_line}"
            )
        print(f"usage at {highest}% >= margin {MARGIN_PERCENT}% — blocking", file=sys.stderr)
        sys.exit(1)

    if FLAG_FILE.exists():
        FLAG_FILE.unlink()
        notify(f"usage back under margin ({highest}% < {MARGIN_PERCENT}%) — jadu-loop resuming")

    print(f"usage at {highest}% < margin {MARGIN_PERCENT}% — proceeding", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()
