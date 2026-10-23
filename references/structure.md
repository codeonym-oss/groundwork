# The planning tree

Every groundwork skill reads this file first. It says where things live and what each file holds.

## `groundwork.md`, the project's settings

At the project root, written by `/groundwork:init`. Read it before anything else; if it is missing, say so and
offer to run `/groundwork:init`.

```markdown
---
planning-root: planning            # where the tree lives, relative to the project root
forge: github                      # github | gitlab | none
default-branch: main
tracker: github                    # github | gitlab | jira | linear | none
tracker-project: acme/shop         # the repo, project key or team the issues go to
tracker-board: "3"                 # optional: a GitHub project number, a Jira board, …
key-prefix: GH-                    # how a key is written in folder names: GH-12, SHOP-12, …
epic-as: issue with sub-issues     # how each level maps onto the tracker (see the tracker guide)
story-as: issue with sub-issues
ticket-as: issue
---

# Project rules

- A story point is one hour of work.
- Write issue titles in French.
```

The fields are what the skills need to act. The project rules are plain sentences: follow them as written. groundwork
itself has no built-in story points, languages, labels or custom fields; anything like that is a project rule.

## The tree

```
<planning-root>/
  follow-ups/                      reminders that belong to no epic, story or ticket
  shaping/<slug>/                  notes of a /groundwork:shape session, until a level is chosen
  <KEY>-<slug>/                    an epic, story or ticket at the top (no parent)
    meta.md                        what it is and where it stands
    draft.md                       the text that goes to the tracker
    impl.md                        tickets only, written by the ticket pass
    decisions/                     NNN-<slug>.md, the decisions taken at this level
    follow-ups/                    reminders for this level
    history/                       earlier copies of meta.md, draft.md, impl.md, and CHANGES.md
    prototypes/<slug>/             only when a prototype was built
    stories/<KEY>-<slug>/          an epic's stories, same shape
      tickets/<KEY>-<slug>/        a story's tickets, same shape
    tickets/<KEY>-<slug>/          an epic's or a story's tickets
```

- **Nesting:** an epic holds `stories/` (and may hold `tickets/` directly), a story holds `tickets/`. A story or a
  ticket without a parent sits at the top of the planning root.
- **Folder names:** `<slug>` while the level has no tracker issue (`products-editor`), renamed once to
  `<key-prefix><number>-<slug>` when the issue is created (`GH-12-products-editor`). A slug is lowercase words joined
  by hyphens, three to five words, naming what the work delivers. With `tracker: none`, folders keep their slug.
- **After a rename,** fix the relative links that point into the renamed folder (search the planning root for the old
  path).
- **Order:** the order children ship in is written in the parent's `draft.md`, never in folder names.

## Finding a level and what it inherits

A level's folder is the one holding its `meta.md`. Its **ancestors** are the folders above it that hold a `meta.md`,
up to the planning root.

**Inherited decisions:** before grilling or planning at a level, read the `decisions/` of every ancestor, top first.
Those questions are settled: never ask them again, and say which ones you relied on. A level may still raise a
problem with an inherited decision; then it is a new question at this level, and the new decision says which one it
changes.

## `meta.md`

```markdown
---
kind: ticket                       # epic | story | ticket
title: Keep every edit when an agent edits one file several times in one step
key:                               # empty until the tracker issue exists
parent: GH-1                       # the parent's key, or empty
status: drafted
branch:                            # set when the work starts
tracker-url:
mr:                                # the pull or merge request, once open
created: 2026-10-23
updated: 2026-10-23
---
```

| status | meaning | set by |
|---|---|---|
| `shaping` | grilling in progress | `create-*` |
| `drafted` | `draft.md` written, waiting for approval | `create-*` |
| `tracked` | the tracker issue exists | `create-*`, after a yes |
| `planned` | the ticket pass is done, `impl.md` written (tickets only) | `create-ticket` |
| `building` | branch created, implementation running | `implement` |
| `in-review` | the pull or merge request is open | `implement` |
| `done` | merged | `implement` |
| `dropped` | abandoned; the reason is in `history/CHANGES.md` | any skill, when the person says so |

Epics and stories skip `planned` and `building`. They are `done` when every child is.

## `draft.md`

The text of the tracker issue, written for the people who will read the issue. Start with a `# ` title (the same as
`meta.md`'s), then:

- **ticket:** the problem, the fix (what changes, not how in detail), what is out of scope, and **Done when**: the
  checks that prove it works;
- **story:** the goal, what it delivers, the rules every ticket keeps, and the tickets in the order they ship;
- **epic:** the goal, why now, the stories in order, and what is explicitly not part of it.

Link the decisions it rests on by number (`decision 004`), so a reader can find the reasoning.

## `impl.md` (tickets only)

Written by the ticket pass, against the code as it is that day:

- **Read first:** the files and functions the change touches, with paths.
- **Steps:** numbered, each small enough to check on its own, each with `→ check:` saying how it is verified
  (a test to write and see pass, a command, a page to open).
- **Tests:** what is tested, at which seam.
- **Risks:** what could break elsewhere, and how it is checked.

## `decisions/`

One file per decision, numbered in the order taken at that level: `001-<slug>.md`, `002-…`. Numbers restart at 001 in
each level's folder.

```markdown
# 004: The skill creates tracker issues, only after approval

**Date:** 2026-10-23 (grilling, Q4; agreed: "ok 2, but always ask first")

**Question:** does the skill create the tracker issues and the branches?

**Decision:** **it creates the issues, and never without an explicit yes.** …

- **Why:** …
- **Not chosen:** … and why not.
```

Quote the person's answer in the date line, briefly, in their words. A decision is never edited after it is written.
When it changes, write a new decision that says **Supersedes 004**, and add one line under the old title:
`**Superseded by 011.**`

## `history/`

Before rewriting `meta.md`, `draft.md` or `impl.md`, copy the current file to
`history/<YYYY-MM-DD>_<HHMM>_<file>` (local time), then add one line to `history/CHANGES.md`:

```markdown
- 2026-10-23: split the products editor into three tickets after the ticket pass.
```

Decisions are never copied: they are never edited (see above).

## `follow-ups/`

A reminder of work for later, found while doing something else. File name `<YYYY-MM-DD>_<HHMM>_<slug>.md`, in the
`follow-ups/` of the level it belongs to (the planning root's when it belongs to none).

```markdown
---
status: open                       # open | done | dropped
from: person                       # person | agent
found-while: GH-12                 # the work in progress when it was found, or empty
resolved-by:                       # a key, a pull/merge request, or why it was dropped
---

# The products list re-sorts when a row is edited

What was seen, where (file:line, a page, a trace), why it was left for later, and what fixing it would take.
```

- **Closed, never deleted:** set `status: done` or `dropped` and fill `resolved-by`.
- **A ticket that takes one up** links it in its `draft.md`; once that ticket is merged, offer to close it.
- **Files without a header** (written before groundwork) count as `status: open`, `from: person`.

**Agents register follow-ups too.** When you notice a problem unrelated to the task at hand (a bug, a flaky test, a
misleading comment), don't fix it and don't drop it: draft a follow-up with `from: agent`, show it, and save it only
after a yes. Then carry on with the task.

## `prototypes/`

When a question is better shown than argued, a prototype answers it. Build it only after a yes, in
`prototypes/<slug>/` at the level that asked: the code or screenshots, plus `findings.md` saying what it showed. The
decision that follows links to it. Prototypes are throwaway: never ship their code as is.

## `shaping/`

`/groundwork:shape` keeps its notes in `shaping/<slug>/`: `notes.md` (the problem as understood) and `decisions/`.
When the person picks a level, the chosen `create-*` skill moves those decisions into the new level's folder and
deletes the shaping folder.
