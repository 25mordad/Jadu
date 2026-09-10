---
name: jadu-bidar
description: Session-start workflow for Jadu. Use when the user invokes jadu-bidar, starts/resumes a project session, wants Codex to inspect project state, pull latest changes safely, review TASKS/WORKLOG/AGENTS context, and expand planning subtasks without implementing code.
---

# Jadu Bidar — Session Start

Called at the beginning of a work session. Studies the project state and expands the task list with new subtasks. This is a planning workflow, not an implementation workflow.

## Workflow

### 1. Pull latest from remote (if applicable)

Run:

```bash
git remote get-url origin 2>/dev/null
```

If a remote URL is returned, run `git pull --ff-only`. Report what changed (e.g., "pulled 3 commits") or "already up to date". If the pull fails (e.g. local divergence), report the error and continue without aborting the session.

### 2. Check for a blocked jadu-loop task

If `LOOP_TASK.md` exists in the project root, read its `STATUS` line and, if `STATUS: blocked`, the reason noted on the blocked subtask. This must be the first thing surfaced in step 5's report — a returning session should learn about a stuck autonomous task immediately, before anything else. If `LOOP_TASK.md` doesn't exist or `STATUS` isn't `blocked`, say nothing about it.

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

### 5. Report back

Print a short summary:

- If step 2 found a blocked jadu-loop task, lead with that — branch name and blocking reason.
- How many new subtasks were added and what area they cover.
- One-line suggestion for where to start.

Do not ask for confirmation at any step — just do it.

## Rules

- Treat this as planning/session setup only.
- Do not implement feature/code changes.
- Obey repository `AGENTS.md` and user approval rules before changing files.
