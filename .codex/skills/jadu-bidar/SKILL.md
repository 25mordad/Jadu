---
name: jadu-bidar
description: Session-start workflow for Jadu. Use when the user invokes jadu-bidar, starts/resumes a project session, wants Codex to inspect project state, pull latest changes safely, review TASKS/WORKLOG/AGENTS context, expand planning subtasks, and schedule a 30-minute focus reminder without implementing code.
---

# Jadu Bidar — Session Start

Called at the beginning of a work session. Studies the project state, expands the task list with new subtasks, and sets focus timers. This is a planning workflow, not an implementation workflow.

The timers serve two purposes: keeping you focused, and keeping sessions short. Shorter sessions mean smaller context windows, which saves tokens and keeps responses sharp.

## Workflow

### 1. Get current time

Run:

```bash
date '+%M %H %d %m'
```

You'll need this for the reminder schedule.

### 2. Pull latest from remote (if applicable)

Run:

```bash
git remote get-url origin 2>/dev/null
```

If a remote URL is returned, run `git pull --ff-only`. Report what changed (e.g., "pulled 3 commits") or "already up to date". If the pull fails (e.g. local divergence), report the error and continue without aborting the session.

### 3. Read project context

Read the following in parallel:

- `TASKS.md` — the primary task list; focus on P1 and P2 open items and their subtasks.
- `WORKLOG.md` (last 80 lines) — focus on the most recent session's **Pending / TODO**.
- `git log --oneline -20` — understand what was last worked on.
- `AGENTS.md` — shared agent instructions, architecture notes, approval rules, commands, and conventions.
- `CLAUDE.md` — read only if present, for Claude compatibility context.

Skim, but do not deep-read, 2–3 recently modified files from the git log to understand the current shape of the code.

### 4. Expand the task list

Add new subtasks to open tasks in `TASKS.md`. Rules:

- Do not execute anything — only plan.
- Add subtasks that logically follow from what's already done or partially started.
- Break vague items into concrete, actionable steps.
- Flag dependencies between subtasks inline with `← depends on [name]`.
- Keep each new item one line, prefixed with `- [ ]`.
- Add new subtasks under the relevant existing task block — do not create new top-level tasks.
- Do not remove, check off, or re-prioritize any existing items.

If `TASKS.md` is missing, propose creating one but do not create it without approval.

### 5. Schedule 30-minute recurring reminder

If a recurring reminder/timer tool is available in the current environment, schedule one every 30 minutes with the message: "⏱ 30 min — check your focus, review progress on current task". If a sound step is supported, play `~/.claude/sounds/30.mp3` when available.

If no reminder/timer tool is available, do not fake it and do not create OS-level cron jobs. Tell the user to set an external 30-minute reminder.

### 6. Report back

Print a short summary:

- How many new subtasks were added and what area they cover.
- Confirmation that the 30-minute recurring timer is set (or unavailable).
- One-line suggestion for where to start.

Do not ask for confirmation at any step — just do it.

## Rules

- Treat this as planning/session setup only.
- Do not implement feature/code changes.
- Obey repository `AGENTS.md` and user approval rules before changing files.
- Keep only the 30-minute reminder; do not add 60-minute reminders.
