# Loop Task: fix-footer-copyright-year

STATUS: idle
BRANCH: fix/footer-copyright-year

## Briefing

`resources/footer.html` hardcodes `© 2024` instead of computing the current
year, so the site footer has been visibly stale since January. This is a
one-line fix, already fully decided — there's no design judgment left to
make. Framework-agnostic worked example: replace every `<your test command>`
/ `<your lint command>` placeholder below with your project's actual
commands before using this as a starting point.

## Subtasks

- [ ] 1
  TYPE: branch
  ACTION: `git checkout main && git pull --ff-only && git checkout -b fix/footer-copyright-year`
  VERIFY: `git branch --show-current` prints exactly `fix/footer-copyright-year`

- [ ] 2
  TYPE: code
  ACTION: In `resources/footer.html`, change the line `<span>&copy; 2024 Acme Inc.</span>` to `<span>&copy; <script>document.write(new Date().getFullYear())</script> Acme Inc.</span>`. Change nothing else in the file. Commit with message `fix(footer): compute copyright year instead of hardcoding it`.
  VERIFY: `grep -c "&copy; 2024" resources/footer.html` outputs `0`

- [ ] 3
  TYPE: test
  ACTION: `<your test command>` (e.g. `npm test`) `&& <your lint command> resources/footer.html` (e.g. `npx eslint resources/footer.html`)
  VERIFY: exit code `0`, no failing tests, no lint violations reported on `resources/footer.html`

- [ ] 4
  TYPE: finalize
  ACTION: `git push -u origin fix/footer-copyright-year`, then `gh pr create --base main --title "fix: footer copyright year was hardcoded to 2024" --body "resources/footer.html hardcoded the copyright year instead of computing it, so the footer showed a stale year. Built via jadu-loop to validate the mechanism on this project. Do not merge until reviewed."`. Never merge.
  VERIFY: `gh pr view fix/footer-copyright-year --json state -q .state` outputs `OPEN`
