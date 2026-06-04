# Tamam — Session End

Full end-of-session close via a background agent — keeps the main context cheap.

## How it works

1. **Inline (you):** Synthesize a compact session brief from the conversation. No file reads. Just text.
2. **Agent (background):** Spawned with only that brief. It reads files and writes all updates with a tiny context.

The agent never sees the conversation. It only sees the brief you write. That's what makes it cheap.

---

## Step 1 — Write the brief

Synthesize the session into this exact format (keep it under 35 lines, omit empty sections):

```
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

CLAUDE_MD_CHANGES: yes|no — <what changed structurally, or omit if no>
README_CHANGES: yes|no — <what changed for new devs, or omit if no>
MEMORY_CHANGES: yes|no — <new preference/pattern to save, or omit if no>
```

Output the brief as a code block in your response so the user can see it.

---

## Step 2 — Spawn the agent

Call the Agent tool with:
- `description`: "Tamam session close"
- `run_in_background`: false

The `prompt` must be self-contained. Use this template, filling in the SESSION BRIEF you wrote above:

---

**[AGENT PROMPT TEMPLATE — fill in the brief, include everything below verbatim]**

Working directory: $PWD

You are doing an end-of-session project close. A SESSION BRIEF is below. Use it as your only source of truth about what happened — do not try to read git history or infer from code. Just update the files as instructed.

<SESSION BRIEF>
[paste the brief here]
</SESSION BRIEF>

### 1. Update WORKLOG.md

Append a new dated entry. Structure (omit empty sections):

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

Focus on WHY decisions were made, not just what.

### 2. Update TASKS.md

- Mark completed tasks `[x]`
- Move fully-done blocks (all items checked) to `## Done` with a one-line summary and date
- Add new subtasks under relevant parent tasks
- Do NOT remove or re-prioritize open items

### 3. Update CLAUDE.md — only if CLAUDE_MD_CHANGES=yes

Update only for structural changes: new routes, new lang files, new architecture patterns, changed commands.

### 4. Update README.md — only if README_CHANGES=yes

Update only if new CLI commands, setup steps, test docs, env vars, or feature flags were added.

### 5. Save memory — only if MEMORY_CHANGES=yes

Write new feedback/preferences to the project memory directory and update the MEMORY.md index. Follow the memory format (frontmatter + body with Why/How to apply lines).

### 6. Push to remote — only if git remote is configured

Run `git remote get-url origin 2>/dev/null`. If a URL is returned:
1. Stage all modified tracked files: `git add -u`
2. Check if anything is staged: `git diff --cached --quiet && echo "nothing" || echo "staged"`
3. If there are staged changes, commit: `git commit -m "chore: session close — <title from SESSION BRIEF>"`
4. Push: `git push`

If no remote URL is returned, skip this step silently.

### 7. Archive WORKLOG.md — only if needed

Archive when WORKLOG.md exceeds 250 lines OR contains more than 8 session entries (count `## 20` headings).

1. Create `WORKLOG_ARCHIVE.md` if it doesn't exist (header: `# Worklog Archive`)
2. Move all entries except the 3 most recent into the top of `WORKLOG_ARCHIVE.md`
3. Keep WORKLOG.md header intact — only session entries move
4. Add at the bottom of WORKLOG.md: `> Older entries archived in WORKLOG_ARCHIVE.md`

### Rules

- Do NOT ask for confirmation — just do it
- Report at the end: what was updated, what was skipped, whether archiving ran, whether git push ran

---

## Rules (for you, not the agent)

- Do NOT ask for confirmation — write the brief and spawn the agent immediately
- The brief is the only context the agent gets — make it complete enough to act on
- Output the brief visibly so the user can review it while the agent runs
- After the agent finishes, print: "Session closed. If staying in this tab for another session, run `/clear` then `/jadu-bidar`."
