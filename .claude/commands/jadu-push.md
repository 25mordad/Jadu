Stage all modified tracked files, create a commit with a concise message summarising the changes, then push to the current remote branch.

Steps:
1. Run `git status` and `git diff` to understand what changed.
2. Stage every modified/deleted tracked file (`git add` by name — no `-A`).
3. Write a commit message: one subject line (≤72 chars) + blank line + bullet list of changes. Always append `Co-Authored-By: Claude <noreply@anthropic.com>`.
4. Run `git push origin <current-branch>`.
5. Confirm the push succeeded and print the remote URL line from git output.
