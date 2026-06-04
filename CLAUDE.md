# Jadu — Claude Guide

## What this project is

A public collection of Claude Code custom skills (slash commands). Users fork the repo and adapt the commands for their own workflows with Claude.

## Tech stack

- Claude Code skills (Markdown files in `.claude/commands/`)
- GitHub for hosting and collaboration

## Skills in this repo

- `jadu-bidar` — Session start / project orientation
- `jadu-tamam` — End-of-session wrap-up
- `jadu-zad` — Project initialization wizard
- `jadu-push` — Stage, commit, and push changes
- `jadu-kar` — Conversational task manager

## Conventions Claude should follow

- Skill files use the `jadu-` prefix naming convention
- Each skill must be self-contained — it should work without relying on context from other skills or conversations
- When adding or editing a skill, preserve the existing file structure and tone

## PR review workflow

All public PRs are automatically reviewed by Claude. When reviewing:
- Check that the skill is well-structured and follows the existing format
- Flag anything that could cause unexpected or unsafe behavior
- Be welcoming and constructive — this is a public, contribution-friendly repo
