# Tracker guides

One file per tracker groundwork supports. A skill reads the one named by `tracker:` in `groundwork.md` and uses only
the operations it describes; it never improvises a write to a shared board. Every write here needs a yes first
(`../approval.md`).

Each guide covers the same operations:

| operation | used by |
|---|---|
| **check access** (one read) | `init` |
| **create an issue** at a level, with its parent | `create-*` |
| **read an issue** | every skill that resumes work |
| **set a status** | `implement` |
| **link the pull or merge request** | `implement` |
| **close** | `implement`, when the work merges |

To add a tracker, copy `none.md`'s headings, fill each operation with the exact commands, and say how epic, story
and ticket map onto it.
