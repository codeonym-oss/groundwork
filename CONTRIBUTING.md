# Contributing

Issues and pull requests are welcome. The bar: **a skill does exactly what its `SKILL.md` says, the same way every
time, and never writes outside the planning folder without asking.**

## Setup

Python 3.10+ for the tests and the scripts. Then:

```bash
make test                     # repo consistency + script tests
claude plugin validate .      # the manifest and the skills
```

Try a change on a real project by loading the plugin from your checkout:

```bash
claude --plugin-dir /path/to/groundwork
```

## How the repo is laid out

- `.claude-plugin/plugin.json` (Claude Code) and `plugin.json` (the portable manifest Codex reads, with its
  `extensions.com.openai` display fields): keep their shared fields identical (a test checks it). Claude Code
  lists the skills; Codex finds them in `skills/`.
- `skills/<skill>/SKILL.md`: one per skill, short. Each reads the shared files it needs from `references/`.
- `references/`: the rules every skill shares. `structure.md` (the planning tree), `grilling.md` (how questions are
  asked), `approval.md` (what needs a yes), `drafting.md` (the create flow), `trackers/` (one guide per tracker).
- `skills/<skill>/scripts/`: deterministic helpers (Python, standard library only), each with tests in `tests/`.

A rule belongs in one place. If two skills need it, it goes in `references/` and both point to it.

## Rules for changes

- **Every new outside write asks first.** If a skill gains a step that touches the tracker, git, the machine or the
  person's files, it follows `references/approval.md`. A pull request that adds a write without a question is not
  merged.
- **Nothing project-specific.** Story points, languages, labels and custom fields are a project's rules in
  `groundwork.md`, never built into a skill.
- **No bundled third-party text without a licence that allows it.** The Karpathy guidelines are fetched by `init`,
  never copied here (a test checks it).
- **Adding a tracker:** copy `references/trackers/none.md`'s headings into `references/trackers/<name>.md`, fill each
  operation with the exact commands (checked against the real CLI or API), and add it to the README's table. The
  tests check every guide has every operation.

## Pull requests

`main` is protected: work on a branch named after the issue (`<n>-short-name`) and open a pull request whose title is
a conventional commit (`feat(shape): …`, `fix(init): …`) with `Fixes #<n>` in the body. release-please builds the
version and the changelog from those titles; don't edit `VERSION` or either manifest's version by hand.
