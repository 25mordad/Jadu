# Jadu (جادو)

A collection of AI-agent workflow skills for structured, productive project sessions. Fork the repo, copy the workflows you want, and use them with Claude Code or Codex.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[فارسی](README.fa.md)

---

## Workflows included

| Workflow | Claude Code | Codex | What it does |
|---|---|---|---|
| Bidar | `/jadu-bidar` | `jadu-bidar` skill | Session start — reads project state, expands planning subtasks, and sets or suggests a 30-minute focus reminder |
| Zad | `/jadu-zad` | `jadu-zad` skill | Project initialization wizard — asks setup questions once and writes project context files |
| Kar | `/jadu-kar` | `jadu-kar` skill | Conversational task manager — add, update, review, and complete tasks in `TASKS.md` |
| Payan | `/jadu-payan` | `jadu-payan` skill | Session end — inline close (no brief), updates docs/tasks, then commits and pushes automatically |
| Push | `/jadu-push` | `jadu-push` skill | Stage changes, write a concise commit, and push on demand any time outside of a session close |

`jadu-tamam` was renamed to `jadu-payan`.

---

## How to use

### Claude Code

Copy the commands you want into your project's `.claude/commands/` directory:

```bash
cp .claude/commands/jadu-bidar.md /your-project/.claude/commands/
```

Or install all Claude Code commands globally:

```bash
mkdir -p ~/.claude/commands
cp .claude/commands/jadu-*.md ~/.claude/commands/
```

The commands become available as slash commands such as `/jadu-bidar`.

### Codex

Copy the skill folders you want into your project or user-level Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R .codex/skills/jadu-* ~/.codex/skills/
```

Then start a new Codex session and invoke the workflow by name, for example: `jadu-bidar`.

### Shared project guide

For projects that use multiple agents, keep an `AGENTS.md` file in the project root. Jadu’s Codex workflows treat `AGENTS.md` as the primary source of instructions. Claude Code can keep a smaller `CLAUDE.md` that points to the shared guide.

---

## Typical session flow

1. `jadu-zad` — initialize or refresh project context files.
2. `jadu-bidar` — start a session, pull latest safely, read context, and choose a focus.
3. `jadu-kar` — add or update tasks as work becomes clearer.
4. `jadu-payan` — close the session inline, update docs/tasks, and commit + push automatically.
5. `jadu-push` or explicit `push` — commit and push on demand any time you're not closing the session.

---

## Customization

- **Rename the prefix** — the `jadu-` prefix is arbitrary. Rename the files to anything you like (`/start`, `/push`, `/done`) and Claude Code will pick up the new names.
- **Edit the workflows** — each command or skill is plain Markdown. Change the steps, tone, or structure to match your workflow.
- **Keep agents aligned** — when behavior changes, update both `.claude/commands/` and `.codex/skills/`.
- **Add your own** — create a new `.md` file in `.claude/commands/` for Claude Code, or a new `.codex/skills/<name>/SKILL.md` folder for Codex.

---

## Optional: 30-minute sound alert

`jadu-bidar` uses only a 30-minute focus reminder. Claude Code can schedule it when the reminder tool is available. Codex may not have a reminder tool; in that case the skill tells you to set an external 30-minute reminder instead of faking one.

Claude Code can optionally play a sound at each 30-minute reminder. It requires `ffplay` (part of `ffmpeg`) and `30.mp3` placed at `~/.claude/sounds/`.

This repo includes the default sound:

```bash
# Install ffmpeg (if not already installed)
# macOS:  brew install ffmpeg
# Ubuntu: sudo apt install ffmpeg

# Copy the sound file
mkdir -p ~/.claude/sounds
cp sounds/30.mp3 ~/.claude/sounds/
```

If the file or `ffplay` is not present, the workflow skips the sound silently.

---

## Contributing

PRs are welcome. Please keep Claude Code commands, Codex skills, and user documentation aligned when changing workflow behavior.
