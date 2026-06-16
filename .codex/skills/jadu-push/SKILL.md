---
name: jadu-push
description: Explicit push workflow for Jadu. Use only when the user invokes jadu-push or explicitly asks to push. Stages all changes, commits with a concise summary or user-provided message, and runs git push. Never push for ordinary session close or task updates.
---

# Jadu Push — Commit and Push

Commit and push only when the user explicitly asks.

## Workflow

1. Run `git status --short` and inspect relevant diffs to understand what changed.
2. Stage all changes with `git add -A`.
3. Commit with a short summary of the staged changes, unless the user supplied a commit message.
4. Run `git push`.
5. Report whether the commit and push succeeded.

## Rules

- Never run `git push` unless the user explicitly asks to push.
- If there is nothing to commit, skip the commit. Push only if there are already local commits to push and the user asked to push.
- If push fails because of auth, divergence, or network, report the error and stop.
- Do not add agent-specific co-author lines unless the user asks.
