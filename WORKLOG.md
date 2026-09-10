# Jadu — Worklog

---

## 2026-06-16 — Multi-agent Jadu documentation and Codex skills

### What we built

| Feature | Files |
|---|---|
| Shared agent guide | `AGENTS.md` |
| Claude command rename from tamam to payan | `.claude/commands/jadu-payan.md`, `.claude/commands/jadu-tamam.md` deleted |
| Codex skill set | `.codex/skills/jadu-*/SKILL.md`, `.codex/skills/jadu-*/agents/openai.yaml` |
| Multi-agent user documentation | `README.md`, `README.fa.md`, `PROJECT.md`, `CLAUDE.md` |
| 30-minute-only reminder policy | `.claude/commands/jadu-bidar.md`, `.codex/skills/jadu-bidar/SKILL.md`, `sounds/60.mp3` deleted |

### Decisions

#### 1. AGENTS.md as shared source of truth
**Why:** The repository should support multiple agents instead of being Claude-only.
**How:** Added `AGENTS.md` for shared rules and kept `CLAUDE.md` as Claude-specific compatibility notes.

#### 2. jadu-payan replaces jadu-tamam
**Why:** The user wanted the session-end workflow renamed to Payan.
**How:** Renamed the Claude command and documented the old name only as a migration note.

#### 3. 30-minute reminder only
**Why:** The user wanted to remove the 60-minute reminder and keep the recurring focus check simple.
**How:** Removed 60-minute schedule instructions and deleted `sounds/60.mp3`.

### Challenges & Solutions

| Challenge | Solution |
|---|---|
| Codex metadata generator stripped `$skill` names from default prompts | Rewrote each `.codex/skills/jadu-*/agents/openai.yaml` prompt manually so it explicitly names the matching skill |

### Pending / TODO

- [ ] Optionally install/update the global Codex skills from this repo copy if desired.

---

## 2026-09-10 — Add jadu-loop, retire jadu-kar/jadu-push and the sound-reminder feature

### What we built

| Feature | Files |
|---|---|
| New `jadu-loop` workflow (opt-in, autonomous `LOOP_TASK.md` subtask execution) | `.claude/commands/jadu-loop.md`, `.codex/skills/jadu-loop/` |
| Supporting scripts (queue gate, usage-margin gate, Telegram notifier) | `scripts/jadu-loop/*.py`, `scripts/jadu-loop/README.md` |
| `LOOP_TASK.md` templates (blank + worked example) | `templates/jadu-loop/*.md` |
| Authoring rules distilled from a real multi-day run elsewhere | `docs/jadu-loop-authoring-guide.md` |
| `jadu-kar` and `jadu-push` removed entirely | `.claude/commands/jadu-kar.md`, `jadu-push.md`, `.codex/skills/jadu-kar/`, `jadu-push/` deleted |
| Sound/focus-reminder feature removed entirely | `sounds/30.mp3` deleted, `AGENTS.md` "Focus reminder policy" section removed |
| `jadu-bidar` cleanup + jadu-loop awareness | `.claude/commands/jadu-bidar.md`, `.codex/skills/jadu-bidar/SKILL.md` |
| `jadu-payan` push-check fix + Claude/Codex parity | `.claude/commands/jadu-payan.md`, `.codex/skills/jadu-payan/SKILL.md` |
| Docs refreshed to match | `README.md`, `README.fa.md`, `AGENTS.md`, `CLAUDE.md`, `PROJECT.md` |
| Oldest 3 worklog entries archived | `WORKLOG_ARCHIVE.md` created |

### Decisions

#### 1. jadu-loop ported in as a genericized, opt-in workflow
**Why:** The mechanism (a human writes fully-specified `ACTION`/`VERIFY` subtasks into `LOOP_TASK.md`, an agent executes them unattended with no per-step approval) was proven on another project over a real multi-day, 30+ subtask run — including several authoring bugs that only surfaced once the loop actually hit them. Worth sharing as a Jadu workflow rather than staying project-specific.
**How:** Ported the command/skill, gate/usage/notify scripts, and templates, stripping every project-specific reference (branding, personal Telegram setup, framework-specific test commands). The hard-won lessons became `docs/jadu-loop-authoring-guide.md` so they're not lost in translation. Explicitly documented as the one deliberate exception to Jadu's normal "confirm before implementing" rule — see the new `AGENTS.md` section.

#### 2. jadu-kar and jadu-push removed
**Why:** User decision — not explained further beyond wanting them gone. No functional dependency on either remained after removal (jadu-payan and jadu-loop don't call them).
**How:** Deleted both commands/skills, their table rows, and their mentions in the "Typical session flow" section of both READMEs. `jadu-payan`'s "explicit push request" fallback description was kept (a user can still just ask to push), but the standing `AGENTS.md` rule that auto-triggered `add + commit + push` on the bare word "push" was removed along with `jadu-push` itself, since that rule *was* jadu-push's behavior inlined — keeping it would have left jadu-push alive in spirit. Flagged this specific call explicitly to the user rather than assuming silently.

#### 3. Sound/focus-reminder feature removed entirely
**Why:** User decision, following on from having already trimmed it down to 30-minutes-only in an earlier session (see 2026-06-16 above). Rather than maintaining a shrinking feature, removed it outright.
**How:** Deleted `sounds/30.mp3` (and the now-empty `sounds/` directory), the `AGENTS.md` "Focus reminder policy" section, and every remaining reference in `CLAUDE.md`/`PROJECT.md`. `jadu-bidar` no longer runs `date '+%M %H %d %m'` — that step existed only to feed the reminder and had gone vestigial.

#### 4. jadu-bidar surfaces a blocked jadu-loop task first
**Why:** A returning session is exactly the moment a stuck autonomous task most needs to be seen — it's easy to otherwise miss that `LOOP_TASK.md` is sitting at `STATUS: blocked`.
**How:** Added a step that checks `LOOP_TASK.md`'s `STATUS` (only if the file exists) and, if blocked, requires the final report to lead with it.

#### 5. jadu-payan's "skip push silently if no remote" claim made actually true
**Why:** Code review while touching this file found the documented behavior wasn't implemented — `git push` ran unconditionally and would have errored (not "skipped silently") in a repo with no remote.
**How:** Changed the script line to `git remote get-url origin >/dev/null 2>&1 && git push` in both the Claude command and the Codex skill, so the `&&` short-circuit actually produces the documented behavior. Also brought the Claude command's `Rules` section up to parity with the Codex skill's (it was missing the "documentation/task updates only" and "closing = explicit push request" rules).

### Pending / TODO

- [ ] P2: Set up GitHub Actions for automatic Claude PR review (carried over, still open)

---

> Older entries archived in WORKLOG_ARCHIVE.md
