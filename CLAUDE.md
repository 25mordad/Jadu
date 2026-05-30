# Jadu — Claude Guide

## What this project is

A public collection of Claude Code custom skills (slash commands). Users fork the repo and adapt the commands for their own workflows with Claude.

## Tech stack

- Claude Code skills (Markdown files in `.claude/commands/`)
- GitHub for hosting and collaboration

## Skills in this repo

- `bobo-init-project` — Project initialization wizard
- `bobo-wrap-it-up` — End-of-session wrap-up
- `bobo-study-project` — Session start / project orientation
- `bobo-push` — Stage, commit, and push changes
- `bobo-todo` — Conversational task manager

## Conventions Claude should follow

- Skill files use the `bobo-` prefix naming convention
- Each skill must be self-contained — it should work without relying on context from other skills or conversations
- When adding or editing a skill, preserve the existing file structure and tone

## PR review workflow

All public PRs are automatically reviewed by Claude. When reviewing:
- Check that the skill is well-structured and follows the existing format
- Flag anything that could cause unexpected or unsafe behavior
- Be welcoming and constructive — this is a public, contribution-friendly repo
