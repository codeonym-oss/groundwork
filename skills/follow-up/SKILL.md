---
name: follow-up
description: Save a reminder of work for later in the groundwork planning tree, at the level it belongs to (the project, an epic, a story or a ticket). Use when the person says to note, remember or come back to something, and when you notice a problem unrelated to the current task, such as a bug, a flaky test or a misleading comment - draft it and ask before saving.
---

# Save a follow-up

Read `<skill-dir>/../../references/structure.md` ("`follow-ups/`"). Without `groundwork.md`, offer `/groundwork:init`,
or save it in `follow-ups/` at the project root if the person prefers.

1. **What:** a title naming the problem, not the fix ("The products list re-sorts when a row is edited"), then what
   was seen and where (file:line, a page, a trace id), why it is left for later, and what fixing it would take, as far
   as known. Write enough that someone reading it in a month understands it without this conversation.
2. **Where:** propose the level: the ticket, story or epic it belongs to, found by searching the planning tree, or
   the planning root's `follow-ups/` when it belongs to none. Never the level of the work in progress just because
   that is where it was found.
3. **Header:** `status: open`; `from: person` when the person asked for it, `agent` when you noticed it;
   `found-while:` the key or slug of the work in progress; `resolved-by:` empty.
4. **Show the file** (path and content) and save it after a yes. A follow-up you drafted on your own is always
   shown first, even mid-task; then carry on with the task.

To close one, set `status: done` or `dropped` and fill `resolved-by`, after the person agrees. Never delete one.
