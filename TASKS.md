# Jadu — Tasks

## Active

- [ ] P1 · Write a README explaining what Jadu is and how to fork and use it
  - [x] Draft sections: title/tagline, what Jadu is, skill list with one-liners, fork & use instructions
  - [x] Add customization guide (how to rename `bobo-` prefix, add new skills)
  - [x] Add a "Skills included" table linking to each `.claude/commands/` file
  - [ ] Add license badge and link

- [ ] P2 · Set up automatic Claude PR review via GitHub Actions
  - [ ] Create `.github/workflows/claude-pr-review.yml` triggered on `pull_request`
  - [ ] Add `ANTHROPIC_API_KEY` secret to the GitHub repo settings
  - [ ] Wire the workflow to run `/review` skill (or equivalent API call) and post comment
  - [ ] Test with a draft PR after push ← depends on push task

## Backlog

- [ ] P3 · Add CONTRIBUTING.md with guidelines for public contributors
- [ ] P3 · Add a skills wishlist / ideas for future commands

## Done

- [x] P1 · Initialize git repo and push to GitHub as a public repo — 2026-05-30
  - [x] Create `.claude/commands/` directory and copy skill files into the repo
  - [x] Create a `.gitignore` (exclude OS junk, editor files)
  - [x] Create public GitHub repo named `Jadu` under account `25mordad`
  - [x] Stage all files and make the initial commit
  - [x] Add GitHub remote and push

- [x] P1 · Add Farsi translation of README — 2026-05-30
  - [x] Create `README.fa.md` with full Farsi translation
  - [x] Translate title, tagline, and overview
  - [x] Translate skills table with one-liners
  - [x] Translate install instructions (both options)
  - [x] Translate customization section
  - [x] Translate contributing note
  - [x] Link `README.fa.md` from the main `README.md`
