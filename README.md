# Jadu (جادو)

A collection of Claude Code custom skills for structured, productive coding sessions. Fork the repo, drop the files into your project, and the commands are immediately available in Claude Code.

[فارسی](README.fa.md)

---

## Skills included

| Command | What it does |
|---|---|
| `/bobo-study-project` | Session start — reads project state, expands the task list with subtasks, sets 30- and 60-minute focus reminders |
| `/bobo-init-project` | Project initialization wizard — asks setup questions once and writes `CLAUDE.md`, `TASKS.md`, `WORKLOG.md` |
| `/bobo-wrap-it-up` | End-of-session close — updates the worklog, commits pending notes, leaves the project ready to resume |
| `/bobo-todo` | Conversational task manager — add, update, and complete tasks in `TASKS.md` through conversation |
| `/bobo-push` | Stage tracked changes, write a commit message, and push to the current branch in one step |

---

## How to use

### Option 1 — Per-project (recommended)

Copy the skill files you want into your project's `.claude/commands/` directory:

```bash
cp .claude/commands/bobo-study-project.md /your-project/.claude/commands/
```

The command is then available inside that project.

### Option 2 — Global (all projects)

Copy into your user-level commands directory:

```bash
cp .claude/commands/bobo-*.md ~/.claude/commands/
```

The commands become available in every Claude Code session.

---

## Customization

- **Rename the prefix** — the `bobo-` prefix is arbitrary. Rename the files to anything you like (`/start`, `/push`, `/done`) and Claude Code will pick up the new names.
- **Edit the skill** — each file is plain Markdown. Change the steps, tone, or structure to match your workflow.
- **Add your own** — create a new `.md` file in `.claude/commands/` and it becomes a slash command immediately.

---

## Contributing

PRs are welcome. All submissions are automatically reviewed by Claude before merge.
