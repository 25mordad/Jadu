# Jadu — Tasks

## Active

- [ ] P2 · Set up automatic Claude PR review via GitHub Actions
  - [ ] Create `.github/workflows/claude-pr-review.yml` triggered on `pull_request`
    - [ ] Research Anthropic's official `claude-code-action` GitHub Action (or equivalent)
    - [ ] Scaffold workflow: checkout, set up Node/Python if needed, run review, post comment
    - [ ] Scope the review prompt: check skill format, flag unsafe behavior, be constructive
  - [ ] Add `ANTHROPIC_API_KEY` secret to the GitHub repo settings
    - [ ] Go to Settings → Secrets & variables → Actions → New repository secret
  - [ ] Wire the workflow to run `/review` skill (or equivalent API call) and post comment
    - [ ] Decide: use `gh` CLI + Claude API call vs. official Action ← depends on research above
    - [ ] Ensure the comment is posted on the PR thread, not silently dropped
  - [ ] Test with a draft PR after push ← depends on push task
    - [ ] Open a small draft PR (e.g. minor README tweak)
    - [ ] Verify Claude posts a review comment automatically

## Backlog

- [ ] P3 · Add CONTRIBUTING.md with guidelines for public contributors
- [ ] P3 · Add a skills wishlist / ideas for future commands

## Done

- [x] P1 · Rename all skills to jadu-* Persian names and optimize for public use — 2026-06-04
  - [x] Read global versions and compare with project versions
  - [x] Choose Persian names: bidar (بیدار), tamam (تمام), zad (زاد), kar (کار), jadu-push
  - [x] Create optimized `jadu-bidar.md` (recurring timers, git pull, optional sound)
  - [x] Create optimized `jadu-tamam.md` (background agent approach, token-efficient)
  - [x] Create `jadu-zad.md` (adds `/compact` tip from global version)
  - [x] Create `jadu-push.md` (generalized Co-Authored-By for public use)
  - [x] Create `jadu-kar.md`
  - [x] Remove all `bobo-*.md` files
  - [x] Update `CLAUDE.md` skill list and naming convention
  - [x] Update `README.md` and `README.fa.md` skills tables

- [x] P1 · Write a README explaining what Jadu is and how to fork and use it — 2026-05-30
  - [x] Draft sections: title/tagline, what Jadu is, skill list with one-liners, fork & use instructions
  - [x] Add customization guide (how to rename prefix, add new skills)
  - [x] Add a "Skills included" table linking to each `.claude/commands/` file
  - [x] Add license badge and link
    - [x] Create `LICENSE` file (MIT)
    - [x] Add badge to `README.md`
    - [x] Add badge to `README.fa.md`

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
