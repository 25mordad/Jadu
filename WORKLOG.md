# Jadu — Worklog

---

## 2026-05-30 — Project Kickoff

### What we built

| Feature | Files |
|---|---|
| Project identity & conventions | `PROJECT.md` |
| Claude-specific guide & PR review rules | `CLAUDE.md` |
| Launch task list | `TASKS.md` |

### Decisions

#### 1. Name: Jadu (جادو)
**Why:** Wanted a Persian-style name that felt cool and approachable. Candidates were Farman (command), Sorush (herald), Jadu (magic), Simorgh (mythical bird). Jadu won for being short, memorable, and capturing the "it just works" feel of a good command kit.
**How:** Used as the repo name and title across all project docs.

#### 2. Public repo as a skills template
**Why:** The `bobo-` prefixed Claude Code skills (init-project, wrap-it-up, study-project, push, todo) are useful enough to share. Making it public lets others fork and adapt them.
**How:** Repo will be published on GitHub with auto Claude review on all PRs.

#### 3. Accept all public PRs, reviewed by Claude
**Why:** Low friction for contributors, Claude review provides a quality gate without requiring manual attention on every PR.
**How:** To be wired up via GitHub Actions (pending task).

### Pending / TODO

- [ ] Write README
- [ ] Initialize git and push to GitHub
- [ ] Set up GitHub Actions for automatic Claude PR review

---

## 2026-05-30 — Launch Session

### What we built

| Feature | Files |
|---|---|
| Skill collection in repo | `.claude/commands/bobo-*.md` (5 files) |
| English README | `README.md` |
| Farsi README | `README.fa.md` |
| Gitignore | `.gitignore` |
| Initial commit + push to GitHub | `github.com/25mordad/Jadu` |

### Decisions

#### 1. bobo-init-project generalised for non-IT projects
**Why:** The skill was software-centric (languages, frameworks, databases). Users may want to initialise non-code projects — file management, writing, personal workflows — without irrelevant questions.
**How:** Replaced "Tech Stack" section with "Tools & Setup" (answer what's relevant, skip the rest). Updated PROJECT.md and CLAUDE.md templates to match. Example names changed to "25mordad".

#### 2. Token-saving rationale added to bobo-study-project
**Why:** The 30/60 min timers aren't just focus tools — bounded sessions keep context windows short, which directly saves tokens. Worth stating explicitly so users understand the full benefit.
**How:** Added one paragraph to the skill's description.

#### 3. settings.local.json and scheduled_tasks.* added to .gitignore
**Why:** Local Claude session artifacts — durable cron jobs and local permission overrides — should never be shared with contributors.
**How:** Added three entries to `.gitignore`.

#### 4. Farsi README as a separate file
**Why:** A full translation alongside English in one file would make both harder to read. A separate file keeps each clean and lets GitHub render it properly.
**How:** Created `README.fa.md`, linked from top of `README.md`.

### Pending / TODO

- [ ] Add license badge and link to README
- [ ] Set up GitHub Actions for automatic Claude PR review (P2)

---
