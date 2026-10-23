# No tracker

The planning tree is the tracker. Everything works, minus the issues.

## Levels

Folders only (`structure.md`). Folders keep their slug: there is no key to rename them to, and `key-prefix` is empty.

## Check access

Nothing to check.

## Create an issue

Nothing is created. Approval of a draft sets `status: tracked` directly, so the next step (the ticket pass) can start.

## Read an issue

Read the level's `meta.md` and `draft.md`.

## Set a status

Set `status` in `meta.md` (with a copy in `history/` first).

## Link the pull or merge request

Write its URL in `meta.md`'s `mr` field.

## Close

Set `status: done` in `meta.md`.
