# Wrap It Up

Full end-of-session close. Updates all project docs to reflect what was done this session.

## Steps

### 1. Update WORKLOG.md

Review the conversation and append a new dated entry using today's date. Use this structure (omit empty sections):

```markdown
## YYYY-MM-DD — <short session title>

### What we built

| Feature | Files |
|---|---|
| ... | ... |

### Decisions

#### 1. <Decision title>
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

Focus on **why** decisions were made, not just what. Keep it factual and concise.

---

### 2. Update TASKS.md

- Mark any completed tasks as `[x]`
- Move fully-completed task blocks (all items checked) to the `## Done` section with a one-line summary and date
- Add any new subtasks discovered during the session under their relevant parent task
- Do NOT remove or re-prioritize open items

---

### 3. Update CLAUDE.md (if needed)

Update only if something structurally new was introduced this session:
- New routes → add to the static pages table
- New lang files → add to the lang file table
- New architecture patterns or conventions → add a note
- Changed commands or flags → update the Commands section

Skip if nothing structural changed.

---

### 4. Update README.md (if needed)

Update only if:
- New CLI commands or setup steps were added
- Testing docs changed (new test files, new run commands)
- New environment variables or feature flags were introduced

Skip if nothing changed for a new developer reading it.

---

### 5. Save memory (if needed)

If the session revealed a new preference, correction, or non-obvious pattern worth carrying into future sessions, write it to the project memory files. Skip if nothing new emerged.

---

---

### 6. Archive WORKLOG.md (if needed)

After appending the new entry, check if archiving is warranted. Archive when **either** condition is true:
- WORKLOG.md exceeds **250 lines**, OR
- It contains more than **8 session entries** (count `## 20` headings)

**How to archive:**
1. Create `WORKLOG_ARCHIVE.md` if it doesn't exist (with a simple `# Worklog Archive` header)
2. Move all entries **except the 3 most recent** from `WORKLOG.md` into the top of `WORKLOG_ARCHIVE.md` (newest-first order)
3. Keep the WORKLOG.md header/ritual block intact — only session entries move
4. Add a one-line note at the bottom of `WORKLOG.md`: `> Older entries archived in WORKLOG_ARCHIVE.md`

Skip archiving if neither condition is met.

---

## Rules

- Do NOT ask for confirmation at any step — just do it
- Run all 5 steps (+ archive check), skipping only those with nothing new to add
- Report a short summary at the end: what was updated, what was skipped, and whether archiving ran
