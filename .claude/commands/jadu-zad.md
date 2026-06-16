# Zad — Project Initialization Wizard

Bootstraps a new or existing project by asking key questions and writing the appropriate context files for multi-agent work.

## What this command does

1. Ask all setup questions in one message — never one question at a time.
2. Based on the answers, determine which files to create or update.
3. Show the exact file plan and wait for approval.
4. Write each approved file and confirm what changed.

## Step 1 — Ask everything at once

Greet the user briefly, then ask all of the following in a single message. Group them visually but do not split across turns:

### Project Identity

- **Name:** What is this project called?
- **Type:** Is this a software/IT project, or something else such as file management, research, writing, or personal workflow?
- **Description:** One or two sentences — what does it do, what problem does it solve?
- **Status:** Starting fresh, picking up something in progress, or reorganizing something existing?
- **Audience:** Who uses it or benefits from it?

### Tools & Setup

- **Software tools / apps:** What tools, apps, languages, frameworks, databases, hosting, services, scripts, or file structures are central?
- **Automation / integrations:** Any automated steps, scripts, APIs, connected services, CI/CD, storage, or communication tools?
- **Other tools:** Anything else worth knowing?

### Team & Timeline

- **Team:** Who is involved? List names and roles if known.
- **Start date:** When did or will the project start?
- **Milestones:** Any phases, deadlines, or target outcomes?

### Conventions & Rules

- **Workflow:** Preferred working process, branching/review process, folder rules, naming conventions, or approval steps?
- **Standards:** Any style, quality, security, or process standards?
- **Agent rules:** Anything Codex, Claude, or other agents should always or never do in this project?

### Existing files

- Does the project already have `AGENTS.md`, `CLAUDE.md`, `PROJECT.md`, `README.md`, `TASKS.md`, or `WORKLOG.md`? The agent should also check automatically.

## Step 2 — Determine which files to create or update

After the user answers, inspect existing context files and apply these rules:

| Condition | File action |
|---|---|
| Always | Create or update `PROJECT.md` |
| User mentioned agent rules, workflow rules, stack details, commands, or “what agents should know” | Create or update `AGENTS.md` |
| User wants Claude Code compatibility, or `CLAUDE.md` already exists | Offer to create or update `CLAUDE.md` |
| User mentioned tasks, milestones, deadlines, backlog, or next steps | Create or update `TASKS.md` |
| User wants session history | Create `WORKLOG.md` with a minimal header if missing |

Before writing, tell the user: “Based on your answers, I’ll create/update: …” Include target paths, scope, and whether each file will be created, appended, or merged. Wait for explicit approval.

## Step 3 — Write `PROJECT.md`

Use this shape, omitting sections with no real content:

```markdown
# [Project Name]

> [One-sentence description]

## Overview
[2–4 sentences: what it does, who it is for, current status]

## Setup & Tools

| What | Details |
|---|---|
| ... | ... |

## Team

| Name | Role |
|---|---|
| ... | ... |

## Timeline

| Milestone | Target Date |
|---|---|
| ... | ... |

## Conventions
[Workflow rules, naming standards, approval steps, or other operating rules]

## Notes
[Key constraints, kickoff decisions, links]

---
_Initialized: YYYY-MM-DD_
```

## Step 4 — Write `AGENTS.md`

Use `AGENTS.md` as the shared guide for all agents:

```markdown
# [Project Name] — Agent Guide

## What this project is
[1–2 sentences]

## Tools & setup
[Key tools, apps, languages, or structure]

## Key commands / workflows
- `...` — ...

## Conventions agents should follow
- ...

## Things agents should never do in this project
- ...
```

Include the user’s approval workflow if they gave one. If they did not, keep any existing repository instructions intact and avoid inventing restrictive rules.

## Step 5 — Write `CLAUDE.md` only when needed

If Claude compatibility is requested, mirror the relevant parts of `AGENTS.md` but phrase rules for Claude Code. Do not create `CLAUDE.md` by default for an agent-neutral or Codex-only project.

## Step 6 — Write `TASKS.md`

Pre-populate tasks from milestones and next steps. Use checkboxes and realistic priorities:

- P1: due in the next 1–2 weeks or explicitly urgent
- P2: current phase/sprint work
- P3: backlog or someday items

## Step 7 — Report back

After writing, print a short summary:

- files created/updated
- one sentence per file describing its contents
- assumptions made for skipped answers

End with: `Tip: in long sessions, ask your agent to compact/summarize periodically to keep context cost low.`

## Rules

- Ask all setup questions in one message.
- If the user skips a question, make a reasonable assumption and state it.
- Never overwrite an existing file without asking first.
- Do not add placeholder `TBD` sections; omit empty sections.
- Do not execute project work; only create or update context/planning files.
- Obey repository `AGENTS.md` instructions, especially approval-before-code rules.
