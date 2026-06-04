# Bidar — Session Start

Called at the beginning of a work session. Studies the project state, expands the task list with new subtasks, and sets focus timers.

The timers serve two purposes: keeping you focused, and keeping sessions short. Shorter sessions mean smaller context windows, which saves tokens and keeps Claude's responses sharp.

## Steps

### 1. Get current time

Run `date '+%M %H %d %m'` to get current minute, hour, day-of-month, and month. You'll need this for the reminder schedule.

### 2. Pull latest from remote (if applicable)

Run `git remote get-url origin 2>/dev/null`. If a remote URL is returned, run `git pull --ff-only`. Report what changed (e.g., "pulled 3 commits") or "already up to date". If the pull fails (e.g. local divergence), report the error and continue without aborting the session.

### 3. Read project context

Read the following in parallel:
- `TASKS.md` — the primary task list; focus on P1 and P2 open items and their subtasks
- `WORKLOG.md` (last 80 lines) — focus on the most recent session's **Pending / TODO** for additional context
- `git log --oneline -20` — understand what was last worked on
- `CLAUDE.md` — refresh on architecture, flags, conventions

Skim (do NOT deep-read) 2–3 recently modified files from the git log to understand the current shape of the code.

### 4. Expand the task list

Add new subtasks to open tasks in `TASKS.md`. Rules:
- Do NOT execute anything — only plan
- Add subtasks that logically follow from what's already done or partially started
- Break vague items into concrete, actionable steps (e.g. "finish checkout" → "Add validation to BookingController::checkout()", "Write test for RevolutService capture")
- Flag dependencies between subtasks inline with `← depends on [name]`
- Keep each new item one line, prefixed with `- [ ]`
- Add new subtasks under the relevant existing task block — do NOT create new top-level tasks
- Do NOT remove, check off, or re-prioritize any existing items

### 5. Schedule 30-minute recurring reminder

Call `CronCreate` with:
- `cron`: `"*/30 * * * *"` (every 30 minutes)
- `recurring`: true
- `prompt`: `"Run this Bash command (ignore any errors): command -v ffplay >/dev/null 2>&1 && [ -f ~/.claude/sounds/30.mp3 ] && ffplay -nodisp -autoexit ~/.claude/sounds/30.mp3 >/dev/null 2>&1 & Then send a PushNotification with message: '⏱ 30 min — check your focus, review progress on current task'"`

### 6. Schedule 1-hour recurring reminder

Call `CronCreate` with:
- `cron`: `"0 * * * *"` (every hour at :00)
- `recurring`: true
- `prompt`: `"Run this Bash command (ignore any errors): command -v ffplay >/dev/null 2>&1 && [ -f ~/.claude/sounds/60.mp3 ] && ffplay -nodisp -autoexit ~/.claude/sounds/60.mp3 >/dev/null 2>&1 & Then send a PushNotification with message: '🏁 1 hour done — wrap up, update worklog, take a break'"`

### 7. Report back

Print a short summary:
- How many new subtasks were added and what area they cover
- Confirmation that both recurring timers are set (every 30 min and every hour)
- One-line suggestion for where to start

Do NOT ask for confirmation at any step — just do it.
