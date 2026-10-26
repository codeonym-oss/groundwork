# Using groundwork

A walk through groundwork from install to merged pull request. The [README](../README.md) says what groundwork is;
this guide says how to work with it day to day. The exact rules the skills follow are in
[`references/`](../references/).

- [Install](#install)
- [Set up a project](#set-up-a-project)
- [The workflow at a glance](#the-workflow-at-a-glance)
- [1. Shape an idea](#1-shape-an-idea)
- [2. Plan an epic, a story or a ticket](#2-plan-an-epic-a-story-or-a-ticket)
- [3. The ticket pass](#3-the-ticket-pass)
- [4. Implement](#4-implement)
- [Follow-ups](#follow-ups)
- [What groundwork asks before doing](#what-groundwork-asks-before-doing)
- [Picking up where you left off](#picking-up-where-you-left-off)
- [Changing your mind](#changing-your-mind)
- [Using groundwork in Codex](#using-groundwork-in-codex)
- [Troubleshooting](#troubleshooting)

## Install

groundwork is published in the [codeonym-oss marketplace](https://github.com/codeonym-oss/claude-plugins), which
serves both Claude Code and Codex.

**Claude Code:**

```
/plugin marketplace add codeonym-oss/claude-plugins
/plugin install groundwork@codeonym-oss
```

**Codex** (a Codex CLI that supports `codex plugin`), in your terminal:

```bash
codex plugin marketplace add codeonym-oss/claude-plugins
codex plugin add groundwork@codeonym-oss
```

Start a new Codex session afterwards. If you added the marketplace before it supported Codex, refresh it with
`codex plugin marketplace upgrade codeonym-oss`. See [Using groundwork in Codex](#using-groundwork-in-codex) for how
calling the skills differs.

**From a checkout** (to try a change, or to pin a version):

```bash
git clone https://github.com/codeonym-oss/groundwork
claude --plugin-dir /path/to/groundwork
```

## Set up a project

Run once, at the root of the project:

```
/groundwork:init
```

`init` goes through seven short steps and asks before each one that writes anything. Declining a step skips it.

1. **Tools.** Checks `git`, `python3` and the forge CLI (`gh` for GitHub, `glab` for GitLab), and whether you are
   logged in. When a login is missing it gives you the command to run yourself.
2. **Tracker.** Asks which tracker you use (GitHub Issues, GitLab issues, Jira, Linear or none), which repo, project
   or team the issues go to, and how epics, stories and tickets map onto it. Then runs a read-only access check.
3. **Planning root and rules.** Proposes `planning/` at the project root, asks whether it is shared (committed) or
   personal (gitignored), and asks for your project's own conventions.
4. **`groundwork.md`.** Shows the settings file and writes it at the project root after a yes.
5. **Coding guidelines.** Offers to download Andrej Karpathy's coding guidelines into `AGENTS.md`, and to point
   `CLAUDE.md` at `AGENTS.md`.
6. **Skills groundwork builds with.** Offers to install Matt Pocock's skills (`tdd`, `code-review`, `prototype`).
   groundwork works without them; `implement` then reviews on its own.
7. **Report.** What was set, what was skipped, what to run next.

The result is a `groundwork.md` like this one:

```markdown
---
planning-root: planning
forge: github
default-branch: main
tracker: github
tracker-project: acme/shop
tracker-board: "3"
key-prefix: GH-
epic-as: issue with sub-issues
story-as: issue with sub-issues
ticket-as: issue
---

# Project rules

- A story point is one hour of work.
- Write issue titles in French.
```

The project rules are plain sentences, and every skill follows them as written. groundwork has no built-in story
points, labels, languages or branch names: if your team has a convention, write it here. Run `/groundwork:init`
again at any time to change a setting; it only reruns the steps you pick.

## The workflow at a glance

```
idea ──► shape ──► create-epic ──► create-story ──► create-ticket ──► ticket pass ──► implement ──► merged
         (when      (several        (several          (one pull         (impl.md,       (branch, tests,
          unsure)    stories)        tickets)          request)          right before    review, PR)
                                                                         building)
```

You can enter at any point. A bug fix you already understand starts at `create-ticket`; a vague complaint starts at
`shape`. Each level is a folder in the planning tree, and each step sets the level's `status` in its `meta.md`:

`shaping` → `drafted` → `tracked` → `planned` → `building` → `in-review` → `done`

## 1. Shape an idea

Use `shape` when you don't yet know what to build, or how big it is.

```
/groundwork:shape the checkout feels slow and nobody knows why
```

`shape` first searches the planning tree and the code for anything related (an open story it belongs to, a
follow-up describing it, a decision ruling something out) and tells you what it found. Then it grills you on the
**problem**, not the solution: what hurts and for whom, what done looks like, what must not change, how many
separate deliverables it holds.

It ends with a proposal:

- **the level:** a ticket, a story or an epic, or "this belongs in an existing story";
- **a first split:** the children in the order they would ship;
- **the command to run next.**

`shape` creates nothing but its notes in `planning/shaping/<slug>/`. The `create-*` skill you run next takes over
its decisions, so nothing is asked twice.

## 2. Plan an epic, a story or a ticket

```
/groundwork:create-epic     several stories toward one goal
/groundwork:create-story    several tickets toward one goal
/groundwork:create-ticket   one deliverable, one pull request
```

All three follow the same flow.

**Grilling.** One question at a time, each with two to four options, what each costs, and a recommendation. Answer
with a number, or in your own words. Facts the agent can look up (in the code, the docs, the tracker) it looks up;
only decisions come to you. A typical question:

> Where should the price list be cached?
>
> 1. In memory per process: no new dependency, but each instance warms up separately.
> 2. In Redis: shared across instances, but adds a dependency to the checkout path.
> 3. Not at all; precompute it at deploy: fastest reads, but prices change only on deploy.
>
> I recommend **1**: decision 002 says checkout runs on a single instance for now.

**Every answer becomes a file** in the level's `decisions/`, written the moment it is agreed:

```
planning/checkout-speed/decisions/003-cache-the-price-list-in-memory.md
```

Each holds the question, the decision, why, what was rejected, and your answer quoted. Decisions are inherited:
a ticket reads its story's and its epic's decisions and never asks them again.

**Drafting.** When the agent has no more questions, it lists the decisions of the session and asks whether you
share the same understanding. After your yes it writes `draft.md` (the issue text) and, for an epic or story, a
folder with a short draft for each child. You review the drafts and ask for changes.

**Creating the issues.** After you approve the drafts, it lists exactly what it will create (titles, levels,
parents, board) and asks once more. Then it creates the issues and renames each folder from `<slug>` to
`<key>-<slug>`, for example `GH-12-checkout-speed`. With `tracker: none`, approval is the last step.

A story ends up like this:

```
planning/
  GH-1-checkout-speed/
    meta.md  draft.md
    decisions/  001-where-the-time-goes.md  002-…
    history/
    tickets/
      GH-2-cache-the-price-list/      meta.md  draft.md
      GH-3-lazy-load-the-recommendations/
      GH-4-measure-checkout-in-ci/
```

The children are drafted, not planned: each gets its own grilling later, in its ticket pass.

## 3. The ticket pass

The ticket pass turns a drafted ticket into a plan. Run it when the ticket is **next**, not when the story is
planned, because it plans against the code as it is that day.

```
/groundwork:create-ticket GH-2
```

It reads the inherited decisions and the ticket's draft, reads the code the change touches, runs the existing tests
that cover it, and tells you what it found. Then it grills you on what the code revealed that the draft didn't
settle (where a seam goes, how an edge case behaves, what a test should prove). If the ticket turns out to be two,
it proposes the split.

It ends by writing `impl.md`:

- **Read first:** the files and functions involved, with paths;
- **Steps:** numbered, each with a `→ check:` saying how it is verified;
- **Tests:** what is tested, and where;
- **Risks:** what could break elsewhere, and how it is checked.

The ticket is now `planned`.

## 4. Implement

```
/groundwork:implement GH-2
```

`implement` refuses a ticket that isn't `planned` and tells you what is missing. For a planned ticket:

1. **Branch.** Proposes `GH-2-cache-the-price-list` (or your project's branch rule), cut from the latest default
   branch, and asks. Uncommitted changes are shown to you, never stashed or discarded.
2. **Build.** Works through `impl.md` test-first: writes the test a step's `→ check:` describes, sees it fail, makes
   it pass. If the code disagrees with the plan, it stops and asks rather than improvising. Unrelated problems it
   finds become follow-ups, not fixes.
3. **Review.** Reviews the whole diff against `impl.md` and the decisions, and fixes what it finds.
4. **Stop and ask.** Shows the changed files and the test output, then asks, one at a time: commit (with the
   proposed message), then push and open the pull request (with its title and body, including `Fixes #2`).

When the pull request is merged, tell it so (or it checks with `gh pr view` / `glab mr view`): it marks the ticket
`done`, closes the issue if the tracker didn't, and offers to close the follow-ups the ticket took up. When the last
ticket of a story is done, it offers to mark the story done too.

## Follow-ups

A follow-up is a reminder of work for later: a bug spotted on the way, a test that flakes, a misleading comment.

```
/groundwork:follow-up the products list re-sorts when a row is edited
/groundwork:list-follow-ups
```

- It is saved at the level it **belongs** to (an epic, a story, a ticket, or the planning root), not where it was
  found.
- Agents draft follow-ups on their own when they notice something unrelated to the task, then show it and save it
  only after your yes.
- `list-follow-ups` lists every open one across the tree, oldest first, with how long each has waited.
- Follow-ups are closed (`status: done` or `dropped`), never deleted. A ticket that takes one up links it, and
  `implement` offers to close it after the merge.

## What groundwork asks before doing

groundwork never writes outside the planning folder without your explicit yes. No setting turns this off.

| asks first | doesn't ask |
|---|---|
| creating, editing, closing or linking tracker issues | reading anything |
| creating a branch, committing, pushing, opening a pull request | read-only commands (`git status`, `gh issue view`) |
| installing a package, CLI or plugin; logging in | decisions you just agreed, drafts, `meta.md`, `impl.md`, `history/` |
| editing any file outside the planning root, source code included | |
| saving a follow-up an agent drafted | |

Each question shows exactly what will happen (the commands, the issue titles, the lines that change). A yes covers
what was shown and nothing more; a yes from an earlier session doesn't carry over. A no is final for that action, and
the agent carries on with the rest.

## Picking up where you left off

Everything lives in files, so a new session (or a different agent, or a teammate) starts from the tree:

- `meta.md` says where a level stands (`status`, `branch`, `mr`).
- `decisions/` says what is settled.
- `history/CHANGES.md` says what changed and when.
- the parent's `draft.md` gives the order the children ship in.

To continue, name the level: `/groundwork:create-ticket GH-3` runs the next ticket's pass, `/groundwork:implement
GH-3` builds it once planned. Commit the planning root if your team should see the plans; keep it gitignored if
they are personal notes.

## Changing your mind

- **A decision is never edited.** To change one, say so during a grilling session: a new decision is written that
  says `Supersedes 004`, and the old one gets a `Superseded by 011` line.
- **A draft or plan that changes** is copied to `history/` first, with a line in `history/CHANGES.md` saying why.
  If the issue text no longer matches, the agent offers to update the tracker issue.
- **Dropping work:** say so, and the level is set to `dropped` with the reason in `history/CHANGES.md`. Nothing is
  deleted.

## Using groundwork in Codex

groundwork's skills install in Codex from the same marketplace (see [Install](#install)). The workflow, the planning
tree and the approval rules are the same; the differences are in how you call things:

- **No `/groundwork:…` commands.** That syntax is specific to Claude Code. In Codex, use `/skills` to see the
  installed skills, or ask for one by name: "use groundwork's init skill", "run groundwork's create-ticket on GH-2".
- **`init` and `implement` only run when you ask.** Claude Code never starts them on its own; in Codex, ask for
  them by name too.
- **Coding guidelines:** Codex reads `AGENTS.md` itself, so the guidelines `init` adds there apply directly.
- **Matt Pocock's skills:** `init` installs them with `claude plugin`, which Codex doesn't have. Install them from
  [mattpocock/skills](https://github.com/mattpocock/skills) yourself, or go without: `implement` then writes the
  tests and reviews the diff on its own.

Codex installation has been checked; reports on how the full workflow behaves in Codex are welcome in
[the issues](https://github.com/codeonym-oss/groundwork/issues).

## Troubleshooting

**"groundwork.md is missing."** The project hasn't been set up: run `/groundwork:init`. `shape` and `follow-up` work
without it, keeping notes in the conversation or in `follow-ups/` at the project root.

**`implement` stops at once.** The ticket isn't `planned`: run its ticket pass with `/groundwork:create-ticket
<key>` first.

**The access check in `init` fails.** Log the forge CLI in yourself (`gh auth login`, `glab auth login`; they are
interactive), check that the repo or project name is right, and run `/groundwork:init` again. You can pick
`tracker: none` meanwhile and switch later.

**Creating issues failed halfway.** The agent stops, reports which issues exist, and doesn't retry without asking.
The folders of the created ones are already renamed; the others keep their slug and `status: drafted`.

**A link broke after a folder was renamed.** Folders are renamed once, when the issue is created, and relative links
into them are fixed then. Ask the agent to search the planning root for the old path.
