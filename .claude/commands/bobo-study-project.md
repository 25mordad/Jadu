# Study Project — Session Start

Called at the beginning of a work session. Studies the project's current state, expands the pending task list with new subtasks, and sets focus timers.

The timers serve two purposes: keeping you focused, and keeping sessions short. Shorter sessions mean smaller context windows, which saves tokens and keeps Claude's responses sharp.

## Steps

### 1. Get current time

Run `date '+%M %H %d %m'` to get current minute, hour, day-of-month, and month. You'll need these to schedule the reminders.

### 2. Read project context

Read the following in parallel:
- `TASKS.md` — the primary task list; focus on P1 and P2 open items and their subtasks
- `WORKLOG.md` (last 80 lines) — focus on the most recent session's **Pending / TODO** for additional context
- `git log --oneline -20` — understand what was last worked on
- `CLAUDE.md` — refresh on architecture, flags, conventions

Skim (do NOT deep-read) 2–3 recently modified files from the git log to understand the current shape of the code.

### 3. Expand the task list

Add new subtasks to open tasks in `TASKS.md`. Rules:
- Do NOT execute anything — only plan
- Add subtasks that logically follow from what's already done or partially started
- Break vague items into concrete, actionable steps (e.g. "finish checkout" → "Add validation to BookingController::checkout()", "Write test for RevolutService capture")
- Flag dependencies between subtasks inline with `← depends on [name]`
- Keep each new item one line, prefixed with `- [ ]`
- Add new subtasks under the relevant existing task block — do NOT create new top-level tasks
- Do NOT remove, check off, or re-prioritize any existing items

### 4. Schedule 30-minute reminder

Compute target time = now + 30 minutes (carry over hour/day/month if needed).
Call `CronCreate` with:
- `cron`: `"<minute> <hour> <dom> <month> *"` (pinned, one-shot)
- `recurring`: false
- `prompt`: `"Send a PushNotification with message: '⏱ 30 min in — check your focus, review progress on current task'"`

### 5. Schedule 1-hour reminder

Compute target time = now + 60 minutes.
Call `CronCreate` with:
- `cron`: `"<minute> <hour> <dom> <month> *"` (pinned, one-shot)
- `recurring`: false
- `prompt`: `"Send a PushNotification with message: '🏁 1 hour done — wrap up, update worklog, take a break'"`

### 6. Report back

Print a short summary:
- How many new subtasks were added and what area they cover
- Confirmation that both timers are set (show the fire times in HH:MM format)
- One-line suggestion for where to start

Do NOT ask for confirmation at any step — just do it.
