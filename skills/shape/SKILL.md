---
name: shape
description: Shape work that isn't defined yet - grill the person on a vague need or problem, find what is already decided, and propose what to build next - a ticket, a story or an epic, how it splits, and which groundwork create skill to run. Use when the person doesn't know where to start, or whether something is a task, a story or an epic.
---

# Shape the work

Read `<skill-dir>/../../references/structure.md`, `grilling.md` and `approval.md`. `groundwork.md` is needed only to
find the planning root; without it, keep the notes in the conversation and suggest `/groundwork:init` at the end.

`shape` creates nothing outside its notes: no tracker issue, no branch, no level folder.

1. **Take the need as given,** in the person's words. Create `shaping/<slug>/` under the planning root with
   `notes.md` holding that statement.
2. **Look around first:** search the planning tree for levels and decisions that touch the same area (an open story
   it may belong to, a follow-up that describes it, a decision that rules something out), and the code for what
   exists. Say what you found.
3. **Grill the problem, not the solution** (`grilling.md`), one question at a time, each with your recommendation:
   - what hurts today, for whom, and how they get by now;
   - what done looks like, and how anyone will know;
   - what must not change;
   - the size: how many separate deliverables it holds, and whether each could ship alone.
   Write each agreed decision in `shaping/<slug>/decisions/`, and keep `notes.md` up to date.
4. **Propose the shape:**
   - **the level:** a ticket (one deliverable, one pull request), a story (several tickets serving one goal), or an
     epic (several stories); or "this belongs in <existing level>";
   - **a first split:** the children, each in one line, in the order they would ship;
   - **the command to run next:** `/groundwork:create-ticket`, `create-story` or `create-epic`, which takes over the
     shaping folder's decisions (`drafting.md`, step 1).
5. Ask whether that shape is right. If the person picks another level, say what changes, and update `notes.md`.
