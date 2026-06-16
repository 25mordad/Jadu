# Jadu — Agent Guide

Jadu is a public collection of reusable AI-agent workflows for structured project sessions. It supports Claude Code through slash-command Markdown files and Codex through skill folders.

## Source of truth

- Use this `AGENTS.md` as the shared guide for all agents.
- Keep `CLAUDE.md` as Claude-specific compatibility notes only.
- Keep `README.md` and `README.fa.md` user-facing and installation-focused.
- Keep `.claude/commands/` and `.codex/skills/` behavior aligned whenever a Jadu workflow changes.

## Workflow names

| Workflow | Meaning | Claude Code | Codex |
|---|---|---|---|
| Bidar | Start/resume a session | `/jadu-bidar` | `jadu-bidar` skill |
| Zad | Initialize project context | `/jadu-zad` | `jadu-zad` skill |
| Kar | Manage tasks | `/jadu-kar` | `jadu-kar` skill |
| Payan | Close a session | `/jadu-payan` | `jadu-payan` skill |
| Push | Commit and push explicitly | `/jadu-push` | `jadu-push` skill or explicit `push` request |

`jadu-tamam` has been renamed to `jadu-payan`. Do not add new references to `jadu-tamam` except as historical migration notes.

## Agent compatibility rules

- Prefer agent-neutral wording: “agent”, “Codex”, or “Claude Code” only when the distinction matters.
- `AGENTS.md` is the default project guide created by Jadu workflows. Create or update `CLAUDE.md` only for Claude compatibility.
- Codex workflows live in `.codex/skills/<skill-name>/SKILL.md`.
- Claude Code workflows live in `.claude/commands/<command-name>.md`.
- If a tool exists in one agent surface but not another, document a safe fallback instead of assuming the tool exists.
- Do not create OS-level cron jobs unless the user explicitly asks.

## Focus reminder policy

- Jadu keeps only the 30-minute focus reminder.
- Do not add 60-minute reminder schedules or `60.mp3` instructions.
- If a timer/reminder tool is unavailable, tell the user to set an external 30-minute reminder.
- Optional sound setup should reference only `sounds/30.mp3`.

## Repository rules

- First define the task with the user.
- Then refine the task and subtasks together.
- Then confirm the exact intended path, scope, and implementation plan.
- Start coding or changing implementation files only after the user explicitly gives permission.
- Documentation and task-file updates requested by the user are allowed, but feature/code changes require explicit approval first.
- Never run `git push` unless the user explicitly asks to push.
- When the user says `push`, run `git add -A`, commit with a short summary of the staged changes unless the user supplied a message, then `git push`.

## Maintenance checklist

When changing a workflow:

1. Update the matching Claude command and Codex skill.
2. Update `README.md` and `README.fa.md` if users need to know.
3. Update this `AGENTS.md` if agent behavior or conventions changed.
4. Update `CLAUDE.md` only for Claude-specific notes.
5. Check for stale names with `grep -R "jadu-tamam\|60.mp3\|60-minute" .`.
