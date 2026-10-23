---
name: create-epic
description: Plan an epic with groundwork - grill the person on its goal, shared design and split into stories, record every decision, draft the epic and its stories, and create the tracker issues after approval. Use when the person wants to plan a large piece of work made of several stories.
---

# Create an epic

1. Read `<skill-dir>/../../references/structure.md`, `grilling.md`, `approval.md`, `drafting.md`, and the tracker guide
   named in `groundwork.md` (`<skill-dir>/../../references/trackers/`). No `groundwork.md`: offer `/groundwork:init`.
2. Follow `drafting.md` with **kind `epic`**. The epic's children are **stories** (in `stories/`); a piece of work too
   small to be a story may be a ticket directly under the epic (`tickets/`).
3. The global pass settles what every story will share: the goal, why now, who it serves, the architecture and
   boundaries, what is explicitly not part of it, and the stories in the order they ship. Questions that only matter
   inside one story are left for that story's pass: note them in the story's `draft.md` as open questions.
4. Stop after the issues are created. The next step is `/groundwork:create-story` on the first story.
