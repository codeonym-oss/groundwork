# Asking first

groundwork never writes outside the planning folder without the person's explicit yes. No setting, flag or
earlier answer turns this off.

## What needs a yes

- **The tracker:** creating, editing, closing or linking an issue, a board item or a project.
- **The forge and git:** creating a branch, committing, pushing, opening or editing a pull or merge request,
  creating a repository.
- **The machine:** installing a package, a CLI or a plugin; logging in; running a command that changes global
  state.
- **The person's files:** writing or editing any file outside the planning root, including `groundwork.md`,
  `AGENTS.md`, `CLAUDE.md`, `.gitignore` and source code.
- **Follow-ups an agent drafts** (they are the person's reminders, so the person decides whether they exist).

## What doesn't

Reading anything; running read-only commands (`git status`, `gh issue view`, listing a board); and writing the
planning files the person is working on with you right now: decisions they just agreed, drafts, `meta.md`,
`history/`, `impl.md`.

## How to ask

1. **Show exactly what will happen:** the commands to run, or the issue titles and the board, or the file and the
   lines that change. Never "I'll set things up".
2. **Ask one clear question** in the conversation and wait for the answer. Several actions may be asked together
   when they are listed one by one ("create these 11 issues and add them to project 5?").
3. **A yes covers what was shown, nothing more.** Something new, or different from what was shown, is asked again.
   A yes in an earlier session, or for an earlier ticket, does not carry over.
4. **A no is final for that action.** Say what was left undone and carry on with what doesn't need it.
5. **Report what happened:** links to what was created, and anything that failed, with its error.
