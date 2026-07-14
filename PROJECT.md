# Jadu

> A curated collection of AI-agent workflow skills for Claude Code and Codex — open for public use, contribution, and remixing.

## Overview

Jadu (جادو — "magic") is a public template repository of reusable agent workflows that streamline common project sessions: starting work, initializing context, managing tasks, closing sessions (which commits and pushes automatically), and pushing changes on demand outside a session close. It is designed to be cloned, forked, or used as inspiration for building your own command or skill set across Claude Code and Codex.

## Tech Stack

| Layer | Choice |
|---|---|
| Claude Code | Markdown slash commands in `.claude/commands/` |
| Codex | Skill folders in `.codex/skills/` |
| Shared agent docs | `AGENTS.md` |
| Hosting | GitHub (public) |
| CI/CD | Planned agent-assisted PR review |

## Team

| Name | Role |
|---|---|
| Bahman | Solo author |

## Timeline

| Milestone | Target Date |
|---|---|
| Initial release | 2026-05-30 |
| Multi-agent documentation and Codex skills | 2026-06-16 |

## Conventions

- **Branching:** No formal strategy — direct commits and PRs welcome
- **Naming:** Use the `jadu-` prefix for all workflows
- **Agent docs:** Keep `AGENTS.md` as the shared source of truth; keep `CLAUDE.md` for Claude-specific compatibility
- **Skill parity:** Keep `.claude/commands/` and `.codex/skills/` aligned when workflow behavior changes
- **Review:** Public contributions are welcome; agent-assisted PR review is planned

## Notes

- Skills follow the `jadu-` prefix naming convention
- `jadu-tamam` was renamed to `jadu-payan`
- Focus reminders use only the 30-minute reminder
- The repo serves as both a working toolkit and a public template others can fork and adapt

---
_Initialized: 2026-05-30_
