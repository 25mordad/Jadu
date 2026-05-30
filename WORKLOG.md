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
