---
name: jadu-payan
description: Session-end workflow for Jadu. Use when the user invokes jadu-payan, says the session is ending, asks to wrap up, update WORKLOG/TASKS/AGENTS/CLAUDE/README from the conversation, archive long worklogs, or close out with a commit and push. Inline, no session brief.
---

# Jadu Payan — Session End

Inline session close. No agents, no briefs. Just do it.

## Workflow

### 1. Resolve working directory

Run `pwd`. Stay in this directory for all steps.

### 2. Update `WORKLOG.md`

Read the last 80 lines first. Append a new dated entry covering what was built, key decisions (with why), challenges & solutions, and pending/TODO items. Focus on WHY decisions were made, not just what. Omit empty sections.

### 3. Update `TASKS.md`

- Mark completed tasks `[x]`.
- Add new subtasks under relevant parent tasks.
- Do not remove or re-prioritize open items.

### 4. Update `AGENTS.md` / `CLAUDE.md`

Only if something structural changed: new scripts, new architecture patterns, changed commands, changed conventions. Update `AGENTS.md` for shared/agent-neutral changes and `CLAUDE.md` only for Claude-specific compatibility notes. Skip otherwise.

### 5. Update `README.md`

Only if new CLI commands, setup steps, or env vars were added. Skip otherwise.

### 6. Save memory

If a persistent memory system is available for this agent surface, write any new feedback/preferences/project facts there and update its index. Skip if nothing new or no memory system exists.

### 7. Archive

**`WORKLOG.md`** — if it exceeds 120 lines OR has more than 4 session entries (count `## 20` headings):
1. Create `WORKLOG_ARCHIVE.md` if it doesn't exist.
2. Move all entries except the 2 most recent to the top of `WORKLOG_ARCHIVE.md`.
3. Keep the `WORKLOG.md` header intact.
4. Ensure `WORKLOG.md` ends with: `> Older entries archived in WORKLOG_ARCHIVE.md`.

**`TASKS.md`** — if it exceeds 200 lines:
1. Create `TASKS_ARCHIVE.md` if it doesn't exist.
2. Move any top-level task block where all subtasks are `[x]` to the top of `TASKS_ARCHIVE.md`, with a `### Done YYYY-MM-DD` header.
3. Keep all open/partial blocks in `TASKS.md`.

### 8. Commit and push

```bash
git add -A
git status --short
git diff --cached --quiet && echo "nothing_to_commit" || git commit -m "chore: session close — <title>"
git push
```

If no remote exists, skip silently.

### 9. Report back

Report what was updated, what was skipped, whether archiving ran, and whether git pushed. Then print: "Session closed."

## Rules

- Do not ask for confirmation at any step — just do it.
- Stay in the resolved working directory for the whole workflow.
- Closing a session is treated as the user's explicit request to push; always commit and push in step 8.
- Prefer documentation/task updates only; do not change implementation files as part of session close.
