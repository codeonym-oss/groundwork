---
name: implement
description: Build a planned groundwork ticket - create its branch, follow impl.md and the inherited decisions with test-driven development, review the result, then stop and ask before committing, pushing and opening the pull or merge request. Use when a ticket's ticket pass is done (status planned) and the person says to start it.
disable-model-invocation: true
---

# Implement a ticket

Read `<skill-dir>/../../references/structure.md`, `approval.md`, and the tracker guide named in `groundwork.md`. Find
the ticket the person names. Its `status` must be `planned`; if it isn't, say what is missing (usually the ticket pass:
`/groundwork:create-ticket`) and stop.

## 1. Branch

Propose the branch: the project rule for branch names if there is one, else `<key>-<slug>` from the folder name
(`GH-12-products-editor`), cut from the latest `default-branch` of the remote:

```bash
git fetch origin
git switch -c BRANCH origin/DEFAULT_BRANCH
```

Ask first. If the working tree has uncommitted changes, show them and ask what to do; never stash or discard them on
your own. After the branch exists, set `branch:` and `status: building` in `meta.md` (copy to `history/` first), and
move the tracker issue to its in-progress status when the guide has one (ask).

## 2. Build

- Read `impl.md`, the ticket's decisions and every ancestor's, and follow the coding guidelines in `AGENTS.md` or
  `CLAUDE.md` when they are there. In short: state assumptions, write the minimum code the step needs, change only
  what the ticket asks, and prove each step.
- Work through `impl.md` step by step. For each step, write the test that its `→ check:` describes, see it fail, make
  it pass. Use the `tdd` skill (Matt Pocock's) when it is installed. Run the type checker and the touched test files
  as you go, and the full test suite at the end.
- If the code disagrees with `impl.md` (a function moved, a step won't work), stop and say so. A small correction is
  noted in `impl.md` (copy to `history/` first); a change of design is a question for the person.
- A problem unrelated to the ticket becomes a follow-up (`structure.md`, "`follow-ups/`"), shown and saved only after
  a yes. Don't fix it in this branch.

## 3. Review

Review the whole diff against `impl.md` and the decisions: use the `code-review` skill (Matt Pocock's) when it is
installed, otherwise review it yourself for correctness, needless code and changes outside the ticket. Fix what it
finds.

## 4. Stop and ask

Show: the files changed (`git diff --stat`), the test results with their command and output, and anything from
`impl.md` that was changed or left undone. Then ask, one at a time:

1. **Commit?** Propose the message (the project's convention, else a conventional commit naming the key). After a
   yes, commit.
2. **Push and open the pull or merge request?** Show its title and body: what changed and why, how it was tested, and
   the closing reference from the tracker guide (`Fixes #12`, `Closes #12`, or the Jira key). After a yes, push with
   `git push -u origin BRANCH` and open it with the forge CLI. Set `mr:` and `status: in-review` in `meta.md`.

## 5. After the merge

When the person says it merged (or `gh pr view` / `glab mr view` shows it), set `status: done`, close the issue if
the tracker didn't, and offer to close the follow-ups the ticket took up (`status: done`, `resolved-by:` the key).
When every child of a story or epic is done, say so and offer to mark the parent done too.
