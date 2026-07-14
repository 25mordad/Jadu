# Payan — Session End

Inline session close. No agents, no briefs. Just do it.

---

## Step 1 — Resolve working directory

Run `pwd`. Stay in this directory for all steps.

---

## Step 2 — Update WORKLOG.md

Read the last 80 lines first. Append a new dated entry:

```markdown
## YYYY-MM-DD — <short session title>

### What we built

| Feature | Files |
|---|---|
| ... | ... |

### Decisions

#### 1. <title>
**Why:** ...
**How:** ...

### Challenges & Solutions

| Challenge | Solution |
|---|---|
| ... | ... |

### Pending / TODO

- [ ] ...

---
```

Focus on WHY decisions were made, not just what. Omit empty sections.

---

## Step 3 — Update TASKS.md

- Mark completed tasks `[x]`
- Add new subtasks under relevant parent tasks
- Do NOT remove or re-prioritize open items

---

## Step 4 — Update AGENTS.md / CLAUDE.md

Only if something structural changed: new scripts, new architecture patterns, changed commands, changed conventions. Update `AGENTS.md` for shared/agent-neutral changes and `CLAUDE.md` only for Claude-specific compatibility notes. Skip otherwise.

---

## Step 5 — Update README.md

Only if new CLI commands, setup steps, or env vars were added. Skip otherwise.

---

## Step 6 — Save memory

Write any new feedback/preferences/project facts to `~/.claude/projects/<project-slug>/memory/` and update `MEMORY.md` index. Follow the memory format (frontmatter + body with Why/How to apply lines). Skip if nothing new.

---

## Step 7 — Archive

**WORKLOG.md** — if it exceeds 120 lines OR has more than 4 session entries (count `## 20` headings):
1. Create `WORKLOG_ARCHIVE.md` if it doesn't exist
2. Move all entries except the 2 most recent to the TOP of `WORKLOG_ARCHIVE.md`
3. Keep WORKLOG.md header intact
4. Ensure WORKLOG.md ends with: `> Older entries archived in WORKLOG_ARCHIVE.md`

**TASKS.md** — if it exceeds 200 lines:
1. Create `TASKS_ARCHIVE.md` if it doesn't exist
2. Move any top-level task block where ALL subtasks are `[x]` to the TOP of `TASKS_ARCHIVE.md`, with a `### Done YYYY-MM-DD` header
3. Keep all open/partial blocks in TASKS.md

---

## Step 8 — Commit and push

```
git add -A
git status --short
git diff --cached --quiet && echo "nothing_to_commit" || git commit -m "chore: session close — <title>"
git push
```

If no remote exists, skip silently.

---

## Rules

- Do NOT ask for confirmation at any step — just do it
- Do not add agent-specific co-author lines unless the user asks
- cd into the working directory first
- Report at the end: what was updated, what was skipped, whether archiving ran, whether git pushed
- After finishing, print: "Session closed. Run `/clear` then `/jadu-bidar` to start fresh."
