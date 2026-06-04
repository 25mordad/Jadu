# Kar — Task Manager

Manages `TASKS.md` in the project root through conversation. Never asks the user to edit the file directly.

## File format

`TASKS.md` uses this structure:

```markdown
# TASKS

## [P1] Task title — due: YYYY-MM-DD
**Goal:** one sentence on what done looks like
**Blocked by:** (optional — another task title or external dependency)
- [ ] Subtask A
- [ ] Subtask B ← depends on A
- [x] Completed subtask

## [P2] Another task — due: YYYY-MM-DD
...
```

Priority levels: `P1` (this week / urgent), `P2` (this sprint / important), `P3` (backlog / someday).
Completed tasks stay in the file but are moved to a `## Done` section at the bottom.

---

## Behavior by invocation

The command is called with an optional natural-language arg describing intent. Detect which mode applies:

### Mode A — Adding a new task
Triggered when the user describes something new to do.

1. **Ask in one message** (combine all missing info into a single reply — never ask one question at a time across multiple turns):
   - What is the goal / what does "done" look like?
   - Priority: P1 (this week), P2 (this sprint), or P3 (backlog)?
   - Due date — or is there no deadline?
   - Any subtasks already obvious, or should we figure them out together?
   - Anything this is blocked by?

2. Once the user answers, ask follow-up only if a subtask needs breaking down further. Stop asking when the task is clear enough to act on.

3. Write the task to `TASKS.md`. If the file doesn't exist, create it with the header `# TASKS\n\n---\n`.

4. Confirm: show the task as it was written, one-line summary of where it landed in priority order.

### Mode B — Updating / completing a subtask
Triggered when the user says something like "done with X", "finished Y", "mark Z complete".

1. Read `TASKS.md`, find the matching task/subtask (fuzzy match on title).
2. If a subtask: mark `- [x]`. If the whole task is done: move the entire block to the `## Done` section with a `**Completed:** YYYY-MM-DD` line.
3. Ask: "Anything to add or unblock next?" — then stop.

### Mode C — Listing / reviewing tasks
Triggered when the user asks "what's next", "show tasks", "what are my priorities", etc.

1. Read `TASKS.md`.
2. Print open tasks sorted by priority then due date. Show subtask completion ratio (e.g. `2/5 done`).
3. Highlight any task that is overdue (due date < today) with `⚠ overdue`.
4. Suggest the single best next action to take right now.

### Mode D — Reprioritizing or changing due dates
Triggered when the user says "move X to P2", "push the deadline on Y", "this is more urgent now".

1. Ask for confirmation of what's changing if ambiguous.
2. Update `TASKS.md` in place.
3. Re-sort the file so tasks appear P1 → P2 → P3, then by due date within each group.

---

## Rules for all modes

- NEVER ask the user to edit `TASKS.md` themselves.
- NEVER dump the raw file contents — always present tasks in a clean, readable summary.
- Ask all clarifying questions in one message, not one at a time.
- If the user's description is vague, make a reasonable assumption and state it — don't block on perfection.
- Keep subtasks concrete and actionable (verb + object, e.g. "Add validation to BookingController::checkout()").
- When writing subtasks, flag dependencies inline with `← depends on [subtask name]`.
- Do NOT execute any task — only plan and write to `TASKS.md`.
