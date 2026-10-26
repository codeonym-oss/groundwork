# groundwork

**Plan work before building it.** groundwork is a plugin for Claude Code and Codex that turns an idea into epics, stories and
tickets through short grilling sessions, keeps every decision in a folder tree next to your code, drafts the tracker
issues, plans each ticket against the code as it is that day, and builds it. It asks before every write outside the
planning folder.

**New here?** Read the [usage guide](docs/usage.md): install, setup, and a walk from idea to merged pull request.

```
/groundwork:shape          "the checkout feels slow and nobody knows why"  → a story, split in three tickets
/groundwork:create-story   grill the design → decisions/ → draft the story and its tickets → create the issues
/groundwork:create-ticket  read the code → settle the ticket's own questions → impl.md
/groundwork:implement      branch → test-first build → review → ask to commit, push, open the PR
```

## Why

Coding agents are fast at building and bad at knowing what to build. The questions that decide whether a feature is
right (what it's for, what it must not break, where it stops) are answered in passing, forgotten by the next
session, and asked again by the next ticket. groundwork makes them explicit:

- **One question at a time, each with a recommendation.** You decide; the agent looks up the facts.
- **Every answer is a file.** `decisions/004-issues-only-after-approval.md` records the question, the choice, why,
  and what was rejected.
- **Decisions are inherited.** A ticket reads its story's and epic's decisions and never asks them again.
- **Plans are made late.** A ticket's implementation plan is written right before it is built, against the code as
  it is then, not weeks earlier.
- **You approve every outside write.** Issues, branches, commits, pushes, pull requests, installs, edits to your
  files: each is shown and waits for a yes. Nothing turns this off.

## Install

groundwork is published in the [codeonym-oss marketplace](https://github.com/codeonym-oss/claude-plugins).

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

Then start a new Codex session. If you added the marketplace before it supported Codex, refresh it first with
`codex plugin marketplace upgrade codeonym-oss`.

Then, in your project:

```
/groundwork:init
```

In Codex, which has no `/groundwork:…` commands, find the skills with `/skills` or ask for one by name ("use
groundwork's init skill"). See [Using groundwork in Codex](docs/usage.md#using-groundwork-in-codex).

`init` checks your tools, detects the forge (`gh` or `glab`), asks which tracker you use and your project's own
rules (what a story point means, the language of issue titles…), writes them to `groundwork.md`, offers to add
[Andrej Karpathy's coding guidelines](https://github.com/multica-ai/andrej-karpathy-skills) to `AGENTS.md` and
`CLAUDE.md`, and offers to install [Matt Pocock's skills](https://github.com/mattpocock/skills) that
`implement` builds with. Every step asks first. The [usage guide](docs/usage.md#set-up-a-project) goes through each step.

## Skills

| skill | what it does |
|---|---|
| `/groundwork:init` | sets the project up: tools, forge, tracker, project rules, coding guidelines |
| `/groundwork:shape` | for work that isn't defined yet: grills the problem, proposes the level (ticket, story, epic), a split, and what to run next |
| `/groundwork:create-epic` | grills an epic's goal and shared design, drafts its stories, creates the issues after approval |
| `/groundwork:create-story` | grills a story's design, drafts its tickets, creates the issues after approval |
| `/groundwork:create-ticket` | drafts a new ticket, or runs the **ticket pass** on a drafted one: reads the code, settles its own questions, writes `impl.md` |
| `/groundwork:implement` | builds a planned ticket test-first, reviews it, then asks before committing, pushing and opening the PR |
| `/groundwork:follow-up` | saves a reminder for later at the level it belongs to; agents draft them for unrelated bugs and ask before saving |
| `/groundwork:list-follow-ups` | every open follow-up at every level, oldest first, with how long it has waited |

## The planning tree

```
planning/                          the planning root (set at init)
  follow-ups/                      reminders that belong to no epic, story or ticket
  GH-1-checkout-speed/             a story: <key>-<slug> once its issue exists, <slug> before
    meta.md                        kind, key, parent, status, branch, pull request
    draft.md                       the issue text
    decisions/                     001-where-the-time-goes.md, 002-…
    follow-ups/  history/  prototypes/
    tickets/
      GH-2-cache-the-price-list/
        meta.md  draft.md
        impl.md                    the plan, written by the ticket pass
        decisions/                 this ticket's own decisions
```

A level moves through `shaping` → `drafted` → `tracked` → `planned` → `building` → `in-review` → `done`, each step
set by the skill that does it. Before a skill rewrites `draft.md`, `impl.md` or `meta.md`, it keeps a copy in
`history/` with a line saying why. The full format is in [`references/structure.md`](references/structure.md).

## Trackers and forges

| tracker | through |
|---|---|
| GitHub Issues (with or without a GitHub Project) | `gh` |
| GitLab issues (epics on paid tiers) | `glab` |
| Jira | the Atlassian connector, or `acli` |
| Linear | the Linear connector, or its API |
| none | the planning folders alone |

Each has a short guide in [`references/trackers/`](references/trackers/) describing exactly how issues are created,
linked, moved and closed, so a write to your shared board is never improvised. Adding a tracker is one file.

## Works with any coding agent

groundwork installs as a plugin in **Claude Code** and **Codex** (see [Install](#install)). Its skills are plain
`SKILL.md` files and its planning tree is plain Markdown, so other agents can follow the same workflow too:

- **Agents that load skills** (Cursor, Gemini CLI and others): point them at this repo's `skills/` folder; each
  skill reads the shared `references/` through relative paths.
- **Any agent at all:** the planning tree is just files. An agent that reads `groundwork.md`,
  `references/structure.md` and a level's `decisions/` can plan and build within the same rules.
- `init` writes the coding guidelines into `AGENTS.md`, which Codex, Cursor and Gemini CLI read, and points
  `CLAUDE.md` at it.

groundwork is built and tested in Claude Code. Its Codex install has been checked; reports on how the workflow
behaves in Codex and other agents are welcome.

## How it differs from Matt Pocock's skills

groundwork stands on [mattpocock/skills](https://github.com/mattpocock/skills): its grilling builds on his
`grilling`, and `implement` uses his `tdd` and `code-review`. His `to-tickets`, `triage` and `wayfinder` also plan
work; groundwork differs in that it:

- keeps **a decision file per answer, inherited down the tree**, rather than a plan or a set of tickets alone;
- plans each ticket **in its own late pass** against the current code (`impl.md`);
- **never writes outside the planning folder without a yes**, including commits;
- keeps **follow-ups** at every level, with a listing across the tree.

Use whichever fits; they install side by side.

## Credits

- [Matt Pocock's skills](https://github.com/mattpocock/skills) (MIT): the grilling method in
  [`references/grilling.md`](references/grilling.md) builds on his `grilling` skill.
- [Andrej Karpathy's coding guidelines](https://github.com/multica-ai/andrej-karpathy-skills): `init` downloads them
  from their repository when you agree. groundwork doesn't include their text.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Run the tests with `make test`.

## License

[MIT](LICENSE)
