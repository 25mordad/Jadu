# Payan — Session End

Close a work session by producing a compact session brief, updating project documentation from that brief, and reporting what changed. The brief is the source of truth; do not infer unmentioned work from git history.

## Step 1 — Write the session brief first

Synthesize the session from the conversation only. Do not read files for this step. Keep the brief under 35 lines and omit empty sections.

Use this exact format:

```text
SESSION BRIEF
Date: YYYY-MM-DD
Title: <short session title>

BUILT:
- <feature or change> | files: <key files touched>

DECISIONS:
- <title>: why=<reason> | how=<approach>

CHALLENGES:
- <challenge> → <solution>

PENDING:
- [ ] <item>

AGENTS_MD_CHANGES: yes|no — <what changed structurally, or omit if no>
CLAUDE_MD_CHANGES: yes|no — <what changed structurally, or omit if no>
README_CHANGES: yes|no — <what changed for new users/devs, or omit if no>
MEMORY_CHANGES: yes|no — <new durable preference/pattern to save, or omit if no>
```

Output the brief visibly in a code block so the user can review it.

## Step 2 — Update `WORKLOG.md`

Read or create `WORKLOG.md` as needed. Append a dated entry, omitting empty sections:

```markdown
## YYYY-MM-DD — <title from brief>

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

Focus on why decisions were made, not just what changed.

## Step 3 — Update `TASKS.md`

If `TASKS.md` exists:

- Mark completed tasks `[x]` only when completion is clear from the session brief.
- Move fully done blocks to `## Done` with a one-line summary and date.
- Add new pending subtasks under relevant parent tasks.
- Do not remove or re-prioritize open items.

If `TASKS.md` is missing and the brief has pending items, propose or create a minimal task list depending on repository approval rules.

## Step 4 — Update project guides only when flagged

- Update `AGENTS.md` only if `AGENTS_MD_CHANGES=yes` and the change is structural: new commands, architecture patterns, workflows, setup rules, or changed conventions.
- Update `CLAUDE.md` only if `CLAUDE_MD_CHANGES=yes` and Claude compatibility notes changed.
- Update `README.md` only if `README_CHANGES=yes`, such as new installation steps, commands, workflow names, env vars, or feature flags.

## Step 5 — Save memory only when flagged

If `MEMORY_CHANGES=yes`, write durable preferences/patterns to the project memory system if one exists. If no memory convention exists, ask before creating a new memory directory.

## Step 6 — Git behavior

Inspect status and report dirty files when useful. Do not run `git push` unless the user explicitly asked to push in this turn.

If the user explicitly says “push”, follow the repository push behavior:

1. `git add -A`
2. `git commit -m "<short auto-generated summary>"` unless the user provided a commit message
3. `git push`

For normal `jadu-payan` without explicit push:

- Do not push.
- Do not auto-commit unless the user explicitly requested a commit.
- It is OK to stage/commit only when explicitly requested; otherwise just report what changed.

## Step 7 — Archive `WORKLOG.md` if needed

Archive when `WORKLOG.md` exceeds 250 lines or contains more than 8 session entries matching `## 20` headings.

1. Create `WORKLOG_ARCHIVE.md` if it does not exist with header `# Worklog Archive`.
2. Move all entries except the 3 most recent into the top of `WORKLOG_ARCHIVE.md`.
3. Keep the `WORKLOG.md` header intact; only session entries move.
4. Add at the bottom of `WORKLOG.md`: `> Older entries archived in WORKLOG_ARCHIVE.md` if not already present.

## Step 8 — Report back

End with a concise report:

- what was updated
- what was skipped and why
- whether archiving ran
- whether git commit/push was skipped or run

Then print: `Session closed. If staying in this tab for another session, consider clearing/compacting context before starting again with jadu-bidar.`

## Rules

- Use the session brief as the source of truth.
- Obey `AGENTS.md` approval rules before editing docs when required.
- Prefer documentation/task updates only; do not change implementation files as part of session close.
- Never run `git push` unless the user explicitly asks to push.
