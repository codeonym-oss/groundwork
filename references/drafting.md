# Creating a level

The flow `create-epic`, `create-story` and `create-ticket` share. Read `structure.md`, `grilling.md` and
`approval.md` first, and the tracker guide named in `groundwork.md`.

## 1. Find where it goes

- **A new level:** ask for (or propose) a slug. Its parent is the level the person names, or the level whose folder
  the conversation is in; with none, it sits at the top of the planning root. Create the folder and its `meta.md`
  (`status: shaping`).
- **From a shaping session:** move `shaping/<slug>/decisions/` into the new folder, keeping the numbers, and delete
  the shaping folder.
- **An existing drafted level** (e.g. a ticket a story drafted): use its folder; it already has `meta.md` and
  `draft.md`.

Read every ancestor's decisions (`structure.md`, "Finding a level and what it inherits").

## 2. Grill

Run a grilling session (`grilling.md`) on this level's questions, writing each decision into its `decisions/`.

- **Epic or story (the global pass):** the goal, who it serves, the design and architecture choices its children
  will share, what is out of scope, and how it splits into children (stories for an epic, tickets for a story) and
  in what order. Slice children as thin, end-to-end pieces that each ship and can be checked on their own.
- **Ticket:** see `create-ticket`.

Explore the code, docs and tracker for facts as you go.

## 3. Draft

When the person confirms a shared understanding:

1. Write the level's `draft.md` (`structure.md`, "`draft.md`") and set `status: drafted`.
2. For an epic or a story, create each child's folder under `stories/` or `tickets/` with its `meta.md`
   (`status: drafted`, `parent:` empty until the parent has a key) and a short `draft.md`: the problem, the change,
   and **Done when**. The children get their own grilling later, in their own pass.
3. Add a line to `history/CHANGES.md`.

Show the drafts (the level's in full; each child's title and one-line summary) and ask for approval. Changes the
person asks for are made in place, with a copy in `history/` first.

## 4. Create the tracker issues

After the person approves the drafts, list exactly what will be created (each issue's title, its type or level, its
parent, the board) and ask. Then, following the tracker guide:

1. Create the parent first, then each child with the parent set, in the order of the parent's `draft.md`.
2. For each one, copy `meta.md` to `history/`, then fill `key`, `tracker-url`, `parent` and `status: tracked`.
3. Rename each folder to `<key-prefix><number>-<slug>`, children first, then the parent, and fix relative links.
4. Add a line to each level's `history/CHANGES.md`.

Report the created issues with their links. If one fails, stop, report what exists so far, and don't retry without
asking.

With `tracker: none`, approval sets `status: tracked` directly.

## 5. What next

Say what comes next: for an epic, `create-story` on its first story; for a story, `create-ticket` on its first
ticket (the ticket pass); for a ticket, the ticket pass if it hasn't run, then `implement`.
