---
name: jadu-kar
description: Conversational task manager for Jadu. Use when the user invokes jadu-kar, asks to add, update, complete, list, review, reprioritize, or reorganize tasks in TASKS.md without executing the task work.
---

# Jadu Kar — Task Manager

Manage `TASKS.md` in the project root through conversation. Never ask the user to edit the file directly.

## Modes

Detect which mode applies from the user’s natural-language request.

### Mode A — Add a new task

1. Ask in one message for missing details: goal, priority, due date, subtasks, and blockers.
2. Once clear, write the task to `TASKS.md`. If the file does not exist, create it with a header.
3. Confirm with a clean summary of the task and where it landed.

### Mode B — Update or complete a task/subtask

1. Read `TASKS.md` and fuzzy-match the task/subtask.
2. If a subtask is complete, mark `- [x]`.
3. If the whole task is complete, move the block to `## Done` with a completed date.
4. Ask: “Anything to add or unblock next?” then stop.

### Mode C — List or review tasks

1. Read `TASKS.md`.
2. Print open tasks sorted by priority then due date.
3. Show subtask completion ratio when possible.
4. Highlight overdue tasks when due date is before today.
5. Suggest the single best next action.

### Mode D — Reprioritize or change due dates

1. Ask for confirmation if ambiguous.
2. Update `TASKS.md` in place.
3. Re-sort tasks P1 → P2 → P3, then by due date within each group when the file format supports it.

## Rules

- Do not execute task work; only plan and update `TASKS.md`.
- Ask clarifying questions in one message, not one at a time.
- If the request is vague, make a reasonable assumption and state it.
- Keep subtasks concrete and actionable.
- Flag dependencies inline with `← depends on [subtask name]`.
- Obey repository `AGENTS.md` approval rules before editing.
