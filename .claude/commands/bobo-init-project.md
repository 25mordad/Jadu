# Init Project — Project Initialization Wizard

Bootstraps a new or existing project by asking key questions and writing the appropriate context files.

---

## What this command does

1. Ask all setup questions in **one message** — never one question at a time.
2. Based on the answers, determine which files to create (see Decision rules below).
3. Write each file and confirm what was created.

---

## Step 1 — Ask everything at once

Greet the user briefly, then ask **all of the following** in a single message. Group them visually but don't split across turns:

### Project Identity
- **Name**: What is this project called?
- **Type**: Is this a software/IT project, or something else (e.g. file management, research, writing, personal workflow)?
- **Description**: One or two sentences — what does it do, what problem does it solve?
- **Status**: Starting fresh, picking up something in-progress, or reorganising something existing?
- **Audience**: Who uses it or benefits from it?

### Tools & Setup
_Answer what's relevant — skip anything that doesn't apply._
- **Software tools / apps**: What tools, apps, or software are central to this project? (For IT projects: languages, frameworks, databases, hosting. For others: apps, scripts, file structures, services.)
- **Automation / integrations**: Any automated steps, scripts, or connected services?
- **Other tools**: Anything else worth knowing (CI/CD, communication tools, storage, etc.)?

### Team & Timeline
- **Team**: Who's involved? List names/roles if known (e.g. "25mordad — solo", "25mordad (content) + Sara (design)").
- **Start date**: When did / will the project start?
- **Milestones**: Are there any phases, deadlines, or a target to hit?

### Conventions & Rules
- **Workflow**: How do you prefer to work on this? (For code: branching strategy, review process. For others: folder structure rules, naming conventions, approval steps.)
- **Standards**: Any enforced style, quality, or process standards?
- **Anything Claude should always or never do** in this project?

### Existing files
- Does the project already have a `CLAUDE.md`, `README.md`, or `TASKS.md`? (Claude will check automatically — this is for any context the user wants to add.)

---

## Step 2 — Determine which files to create

After the user answers, apply these rules:

| Condition | File to create |
|---|---|
| Always | `PROJECT.md` |
| User mentioned Claude-specific rules, stack details, or "what Claude should know" | `CLAUDE.md` |
| User mentioned tasks, milestones, or a backlog | `TASKS.md` with initial tasks pre-populated |
| `CLAUDE.md` already exists | Offer to update it instead of overwriting |
| `TASKS.md` already exists | Offer to append initial tasks instead of overwriting |

Before writing, tell the user: "Based on your answers, I'll create: [list of files]." Give them a chance to adjust.

---

## Step 3 — Write the files

### PROJECT.md format

```markdown
# [Project Name]

> [One-sentence description]

## Overview
[2–4 sentences: what it does, who it's for, current status]

## Setup & Tools
<!-- For software projects: languages, frameworks, databases, hosting.
     For other projects: key apps, file structures, services, scripts. -->

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
[Workflow rules, naming standards, approval steps — whatever governs how work gets done]

## Notes
[Anything else worth capturing — key constraints, decisions made at kickoff, links]

---
_Initialized: YYYY-MM-DD_
```

### CLAUDE.md format

```markdown
# [Project Name] — Claude Guide

## What this project is
[1–2 sentences]

## Tools & setup
[Key tools, apps, languages, or structure — whatever is central to how this project works]

## Key commands / workflows
<!-- Fill in as the project matures -->
- `...` — ...

## Conventions Claude should follow
- ...

## Things Claude should never do in this project
- ...
```

### TASKS.md format

Use the same format as the `todo` command. Pre-populate with tasks derived from the user's milestones and any "next steps" they mentioned. Assign realistic priorities:
- P1: anything due in the next 1–2 weeks or explicitly called urgent
- P2: milestone work within the current sprint/phase
- P3: backlog or "someday" items

---

## Rules

- Ask all questions in **one message** — never drip one question per turn.
- If the user skips a question, make a reasonable assumption and state it.
- Never overwrite an existing file without asking first.
- Don't add placeholder sections with "TBD" — omit sections that have no content yet.
- After writing, print a short summary: which files were created/updated and one sentence per file on what it contains.
- Do NOT execute any project work — only write the context files.
