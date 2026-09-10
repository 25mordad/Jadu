# jadu-loop scripts

Three small, dependency-light scripts that make `jadu-loop` safe to run unattended. Copy this whole `jadu-loop/` folder into your project's `scripts/` directory (or wherever you keep project scripts — just update the paths in `.claude/commands/jadu-loop.md` / `.codex/skills/jadu-loop/SKILL.md` if you move it).

```bash
mkdir -p /your-project/scripts
cp -R scripts/jadu-loop /your-project/scripts/
```

## What each script does

| Script | Purpose | Required? |
|---|---|---|
| `check_loop_queue.py` | Reads `LOOP_TASK.md`'s `STATUS` line and whether an open (non-`BLOCKED`) subtask exists. Exits `0` (proceed) only when there's real work to do — so the `&&` chain never spends a token on a "nothing to do" tick. | **Yes** — this is the actual gate |
| `check_usage_margin.py` | A second, free pre-check. Queries `claude -p "/usage"` (zero API cost) and refuses to proceed if your account's session/weekly usage is at or above a margin (default 80%). Assumes Claude Code's `/usage` output format. | Optional — delete it from the invocation chain if you're not on Claude Code, or don't want this gate |
| `notify_telegram.py` | Sends one Telegram message per invocation reporting what happened. | Optional — `jadu-loop`'s "Notify" step is a no-op if this script (or your own replacement) isn't present |

## Install

1. Copy `scripts/jadu-loop/` into your project (see above).
2. Install the one Python dependency these scripts need:
   ```bash
   pip3 install python-dotenv
   ```
3. Make sure `LOOP_TASK.md` (root of your project) and `LOOP_TASK_ARCHIVE/` (a tracked directory) exist — see `templates/jadu-loop/LOOP_TASK.skeleton.md`.
4. Add `.loop_state/` to your project's `.gitignore` — it holds only local run-state (the usage-margin flag file, and a lockfile if you add one — see "Concurrency" below). Never commit it.
5. If you want Telegram notifications, set up a bot (below) and add the two env vars to your project's `.env`.
6. Add whatever commands your `LOOP_TASK.md` subtasks will actually run to your agent's Bash/shell allowlist (e.g. Claude Code's `.claude/settings.local.json`) **before** running the loop — `jadu-loop` deliberately cannot expand its own permissions mid-run.

## Setting up Telegram notifications (optional)

1. Message [@BotFather](https://t.me/BotFather) on Telegram, run `/newbot`, follow the prompts. You'll get a bot token like `123456:ABC-DEF...`.
2. Create (or reuse) a group/channel you want notifications in, add the bot to it.
3. Get the chat ID: send any message in the group, then visit `https://api.telegram.org/bot<TOKEN>/getUpdates` in a browser and read `"chat":{"id": ...}` from the JSON.
4. Add to your project's `.env`:
   ```
   LOOP_TELEGRAM_BOT_TOKEN=123456:ABC-DEF...
   LOOP_TELEGRAM_CHAT_ID=-100123456789
   ```
5. Test it: `python3 scripts/jadu-loop/notify_telegram.py "test message"`.

If your project already uses `TELEGRAM_BOT_TOKEN`/`TELEGRAM_CHAT_ID` (or similar) for something else — a customer-facing bot, an alerting bot — do **not** reuse those names. That's exactly why these are `LOOP_`-prefixed: a name collision makes this script silently post through the wrong bot. Grep your `.env` for existing names before wiring this up.

Don't want Telegram? Swap `send()` in `notify_telegram.py` for Slack/email/a webhook/anything else, or delete the script entirely — `jadu-loop`'s notify step degrades to a no-op if the script isn't there.

## Concurrency (optional, recommended if you'll run this via `cron`)

If you run the invocation chain on a schedule (rather than a single hand-run `while` loop), two overlapping invocations could both pass `check_loop_queue.py` and race on the same subtask. Wrap the whole chain in a `flock` so only one instance ever runs at a time:

```bash
flock -n .loop_state/jadu-loop.lock -c '
  python3 scripts/jadu-loop/check_loop_queue.py \
    && python3 scripts/jadu-loop/check_usage_margin.py \
    && claude -p "/jadu-loop" --permission-mode acceptEdits
'
```

`.loop_state/` must exist and be writable (create it once with `mkdir -p .loop_state`); the lockfile itself is created by `flock` on first run. A hand-run `while ...; sleep N; done` loop in its own terminal doesn't need this — it's inherently single-instance.
