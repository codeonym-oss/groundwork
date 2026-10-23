---
name: create-ticket
description: Plan a ticket with groundwork - for a new ticket, grill and draft it and create its tracker issue after approval; for a drafted ticket, run the ticket pass that reads the code as it is today, settles the ticket's own decisions and writes impl.md. Use when the person wants to plan one piece of work, or to prepare a drafted ticket for implementation.
---

# Create a ticket

Read `<skill-dir>/../../references/structure.md`, `grilling.md`, `approval.md`, `drafting.md`, and the tracker guide
named in `groundwork.md` (`<skill-dir>/../../references/trackers/`). No `groundwork.md`: offer `/groundwork:init`.

Find the ticket: one the person names (by key, slug or path), or a new one.

## A new ticket

Follow `drafting.md` with **kind `ticket`**: grill what it must do and why, draft `meta.md` and `draft.md`, create the
issue after approval. Then go straight on to the ticket pass below, in the same session.

## The ticket pass

For a ticket whose `status` is `drafted` or `tracked`. It is the last step before building: run it when the ticket is
next, not earlier, because it plans against the code as it is now.

1. **Read what is settled:** every ancestor's decisions, the ticket's own decisions, its `draft.md`, and the
   follow-ups it takes up.
2. **Read the code:** find the files, functions, tests and docs the change touches. Run the existing tests that
   cover them, so the plan starts from a known state. Say what you found in a few lines.
3. **Grill the ticket's own questions** (`grilling.md`): what the code reveals that the draft didn't settle, such as
   where a seam goes, how an edge case behaves, what a test should prove. Decisions go in the ticket's
   `decisions/`. If the code shows the ticket is really two, propose splitting it: each part gets its own folder,
   `meta.md` and `draft.md`, and its own issue after approval.
4. **Write `impl.md`** (`structure.md`, "`impl.md`"): the files to read, numbered steps each with `→ check:`, the
   tests, the risks. Keep it to what the ticket needs: no speculative features, no abstractions for one use, no
   unrelated clean-ups (note those as follow-ups instead).
5. If `draft.md` no longer matches what was decided, update it (copy to `history/` first) and offer to update the
   tracker issue's description.
6. Set `status: planned`, add a line to `history/CHANGES.md`, and show `impl.md`. The next step is
   `/groundwork:implement`.
