---
name: list-follow-ups
description: List the open follow-ups at every level of the groundwork planning tree - the project's own and every epic's, story's and ticket's, whoever wrote them - oldest first, with how long each has waited. Use when the person asks what follow-ups, reminders or loose ends are open.
---

# List follow-ups

```bash
python3 <skill-dir>/scripts/list_follow_ups.py            # open ones, oldest first
python3 <skill-dir>/scripts/list_follow_ups.py --all      # closed ones too
python3 <skill-dir>/scripts/list_follow_ups.py --level GH-12   # one level and everything under it
```

It finds the planning root from `groundwork.md` (searching up from the current directory); pass `--root <dir>` to
point it elsewhere. Files without a header count as open, from a person.

Show the output as it is, then offer what fits: open one, close one (`status: done` or `dropped` with
`resolved-by`, after a yes), or turn one into a ticket (`/groundwork:create-ticket`, linking the follow-up in the
draft).
