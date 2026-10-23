---
name: create-story
description: Plan a story with groundwork - grill the person on its design and how it splits into tickets, record every decision, draft the story and its tickets, and create the tracker issues after approval. Use when the person wants to plan a feature made of several tickets, alone or inside an epic.
---

# Create a story

1. Read `<skill-dir>/../../references/structure.md`, `grilling.md`, `approval.md`, `drafting.md`, and the tracker guide
   named in `groundwork.md` (`<skill-dir>/../../references/trackers/`). No `groundwork.md`: offer `/groundwork:init`.
2. Follow `drafting.md` with **kind `story`**. Its children are **tickets** (in `tickets/`).
3. Inside an epic, the story is either already drafted (use its folder) or new (create it under the epic's
   `stories/`). Read the epic's decisions first and never ask them again.
4. The global pass settles what every ticket will share: the design, the data and interfaces between the tickets, the
   rules each keeps, and the tickets in the order they ship, each a thin slice that can be built and checked on its
   own. Questions that only matter inside one ticket are left for its ticket pass: note them in the ticket's
   `draft.md`.
5. Stop after the issues are created. The next step is `/groundwork:create-ticket` on the first ticket.
