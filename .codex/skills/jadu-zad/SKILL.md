---
name: jadu-zad
description: Project initialization wizard for Jadu. Use when the user invokes jadu-zad, asks to initialize/bootstrap a new or existing project, or wants Codex to create project context files such as PROJECT.md, AGENTS.md, optional CLAUDE.md, TASKS.md, or WORKLOG.md from a structured questionnaire.
---

# Jadu Zad — Project Initialization Wizard

Bootstrap a new or existing project by gathering setup context, deciding which context files are needed, and writing only those files after the user approves the exact file plan.

## Workflow

### 1. Ask all setup questions at once

Greet the user briefly, then ask all relevant questions in one message. Do not drip one question per turn.

Group the questions like this:

**Project Identity**
- Name: What is this project called?
- Type: Is this a software/IT project, or something else such as file management, research, writing, or personal workflow?
- Description: In one or two sentences, what does it do and what problem does it solve?
- Status: Starting fresh, picking up something in progress, or reorganizing something existing?
- Audience: Who uses it or benefits from it?

**Tools & Setup**
- Software tools / apps: What tools, apps, languages, frameworks, databases, hosting, services, scripts, or file structures are central?
- Automation / integrations: Any automated steps, scripts, APIs, connected services, CI/CD, storage, or communication tools?
- Other tools: Anything else worth knowing?

**Team & Timeline**
- Team: Who is involved? List names and roles if known.
- Start date: When did or will the project start?
- Milestones: Any phases, deadlines, or target outcomes?

**Conventions & Rules**
- Workflow: Preferred working process, branching/review process, folder rules, naming conventions, or approval steps?
- Standards: Any style, quality, security, or process standards?
- Agent rules: Anything Codex, Claude, or other agents should always or never do in this project?

**Existing files**
- Does the project already have `AGENTS.md`, `CLAUDE.md`, `PROJECT.md`, `README.md`, `TASKS.md`, or `WORKLOG.md`? Say that Codex will check automatically, but the user can add context.

### 2. Inspect existing context files

After the user answers, check for existing files before proposing changes:

- `PROJECT.md`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `TASKS.md`
- `WORKLOG.md`

Never overwrite an existing file without explicit user approval. Prefer appending or merging when a file already exists.

### 3. Decide what to create or update

Apply these rules:

| Condition | File action |
|---|---|
| Always | Create or update `PROJECT.md` |
| User mentioned agent rules, workflow rules, stack details, commands, or “what agents should know” | Create or update `AGENTS.md` |
| User explicitly wants Claude Code compatibility, or `CLAUDE.md` already exists and should stay in sync | Offer to create or update `CLAUDE.md` |
| User mentioned tasks, milestones, deadlines, backlog, or next steps | Create or update `TASKS.md` with initial tasks |
| User wants a session history | Create `WORKLOG.md` with a minimal header if missing |

Before writing, tell the user exactly: “Based on your answers, I’ll create/update: …” Include the target path, scope, and whether each file is created, appended, or merged. Give the user a chance to adjust. Start writing only after the user explicitly approves the file plan.

### 4. Write `PROJECT.md`

Use a concise project overview with real details only. Omit empty sections and do not add placeholders.

### 5. Write `AGENTS.md`

Use `AGENTS.md` as the shared guide for all agents. Include:

- What the project is
- Tools and setup
- Key commands/workflows
- Conventions agents should follow
- Things agents should never do

Include the user’s approval workflow if they gave one. If they did not, keep any existing repository instructions intact and avoid inventing restrictive rules.

### 6. Write `CLAUDE.md` only when needed

If Claude compatibility is requested, mirror the relevant parts of `AGENTS.md` but phrase rules for Claude Code. Do not create `CLAUDE.md` by default for a Codex-only project.

### 7. Write `TASKS.md`

Pre-populate tasks from milestones and next steps. Use checkboxes and realistic priorities:

- P1: due in the next 1–2 weeks or explicitly urgent
- P2: current phase/sprint work
- P3: backlog or someday items

### 8. Report back

After writing, print a short summary:

- files created/updated
- one sentence per file describing its contents
- assumptions made for skipped answers

End with: `Tip: in long sessions, ask Codex to compact/summarize periodically to keep context cost low.`

## Rules

- Ask all setup questions in one message.
- If the user skips a question, make a reasonable assumption and state it.
- Never overwrite an existing file without asking first.
- Do not add placeholder `TBD` sections; omit empty sections.
- Do not execute project work; only create or update context/planning files.
- Obey repository `AGENTS.md` instructions, especially approval-before-code rules.
