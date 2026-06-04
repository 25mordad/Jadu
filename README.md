# Jadu (جادو)

A collection of Claude Code custom skills for structured, productive coding sessions. Fork the repo, drop the files into your project, and the commands are immediately available in Claude Code.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[فارسی](README.fa.md)

---

## Skills included

| Command | What it does |
|---|---|
| `/jadu-bidar` | Session start — reads project state, expands the task list with subtasks, sets 30- and 60-minute focus reminders |
| `/jadu-zad` | Project initialization wizard — asks setup questions once and writes `PROJECT.md`, `CLAUDE.md`, and `TASKS.md` |
| `/jadu-tamam` | Session end — writes a compact brief and delegates all doc updates to a background agent, keeping your context cheap |
| `/jadu-kar` | Conversational task manager — add, update, and complete tasks in `TASKS.md` through conversation |
| `/jadu-push` | Stage tracked changes, write a commit message, and push to the current branch in one step |

---

## How to use

### Option 1 — Per-project (recommended)

Copy the skill files you want into your project's `.claude/commands/` directory:

```bash
cp .claude/commands/jadu-bidar.md /your-project/.claude/commands/
```

The command is then available inside that project.

### Option 2 — Global (all projects)

Copy into your user-level commands directory:

```bash
cp .claude/commands/jadu-*.md ~/.claude/commands/
```

The commands become available in every Claude Code session.

---

## Customization

- **Rename the prefix** — the `jadu-` prefix is arbitrary. Rename the files to anything you like (`/start`, `/push`, `/done`) and Claude Code will pick up the new names.
- **Edit the skill** — each file is plain Markdown. Change the steps, tone, or structure to match your workflow.
- **Add your own** — create a new `.md` file in `.claude/commands/` and it becomes a slash command immediately.

---

## Optional: sound alerts

`/jadu-bidar` can play a sound at each focus reminder. It requires `ffplay` (part of `ffmpeg`) and two audio files placed at `~/.claude/sounds/`.

This repo includes the sounds used in the default setup:

```bash
# Install ffmpeg (if not already installed)
# macOS:  brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg

# Copy the sound files
mkdir -p ~/.claude/sounds
cp sounds/30.mp3 ~/.claude/sounds/
cp sounds/60.mp3 ~/.claude/sounds/
```

If the files or `ffplay` are not present, the skill skips the sound silently — only the push notification fires.

---

## Contributing

PRs are welcome. All submissions are automatically reviewed by Claude before merge.
