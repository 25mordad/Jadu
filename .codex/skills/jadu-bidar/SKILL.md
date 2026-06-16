---
name: jadu-bidar
description: Session-start workflow for Jadu. Use when the user invokes jadu-bidar, starts/resumes a project session, wants Codex to inspect project state, pull latest changes safely, review TASKS/WORKLOG/AGENTS context, expand planning subtasks, set or suggest a 30-minute focus reminder, and recommend where to begin without implementing code.
---

# Jadu Bidar — Session Start

Start a focused work session by refreshing repository state, reading project context, improving the task plan, and recommending where to begin. This is a planning workflow, not an implementation workflow.

## Workflow

### 1. Get current time

Run:

```bash
date '+%M %H %d %m'
```

Use it only for the session summary and reminder context.

### 2. Pull latest from remote when safe

Run:

```bash
git remote get-url origin 2>/dev/null
```

If a remote URL exists, run:

```bash
git pull --ff-only
```

Report “already up to date” or summarize what changed. If pull fails because of divergence, auth, network, or local changes, report the error and continue without aborting.

### 3. Read project context

Read these if present:

- `TASKS.md` — focus on P1/P2 open items and subtasks.
- `WORKLOG.md` — read the last 80 lines; focus on recent “Pending / TODO”.
- `AGENTS.md` — shared agent instructions, architecture notes, approval rules, commands, and conventions.
- `CLAUDE.md` — read only if present for Claude compatibility context.
- `PROJECT.md` and `README.md` — skim if present for project identity/setup.
- `git log --oneline -20` — understand recent work.

Skim, but do not deep-read, 2–3 recently modified files indicated by git history or status. Do not modify implementation files.

### 4. Expand `TASKS.md` planning only

If `TASKS.md` exists, add useful subtasks under relevant existing open task blocks. Follow these rules:

- Do not execute feature work.
- Add only subtasks that logically follow from existing work or partially started items.
- Break vague items into concrete, actionable lines.
- Flag dependencies inline, e.g. `← depends on [name]`.
- Keep each new item one line, prefixed with `- [ ]`.
- Add subtasks under existing task blocks; do not create new top-level priorities unless the user asked.
- Do not remove, check off, or re-prioritize existing items.
- If repository instructions require approval before file changes, present the proposed `TASKS.md` edits and wait for explicit permission before editing.

If `TASKS.md` is missing, propose creating one but do not create it without approval.

### 5. Focus reminder: 30 minutes only

If an explicit reminder/timer tool is available in the current environment, set one recurring reminder:

- 30-minute recurring reminder: “⏱ 30 min — check your focus, review progress on current task”

If no timer tool is available, do not fake it and do not create OS-level cron jobs. Report that timers are unavailable in this Codex surface and suggest the user set an external 30-minute reminder.

### 6. Report back

Print a short summary:

- current time snapshot
- remote pull status
- which context files were found/read
- how many new subtasks were added, or proposed if approval was required
- whether the 30-minute focus reminder was set or unavailable
- one-line suggestion for where to start

## Rules

- Treat this as planning/session setup only.
- Do not implement feature/code changes.
- Obey repository `AGENTS.md` and user approval rules before changing files.
- Continue gracefully when optional files are missing.
- Keep only the 30-minute reminder; do not add 60-minute reminders.
