---
name: init
description: Set up groundwork in a project - check the tools, detect the forge, choose the tracker, write groundwork.md with the project's own rules, add the Karpathy coding guidelines to AGENTS.md and CLAUDE.md, and install the skills groundwork builds with. Run once per project, or again to change a setting.
disable-model-invocation: true
---

# groundwork init

Read `<skill-dir>/../../references/approval.md` first: **every step below that writes anything is shown and asked
before it runs.** Declining a step skips it and moves on; declining everything leaves the project untouched.

If `groundwork.md` already exists at the project root, show its settings, ask which ones to change, and run only
those steps.

## 1. Tools

Check, and report in one short table:

- `git`, and that this is a git repository (`git rev-parse --show-toplevel`). Without one, groundwork still plans,
  but `forge: none`.
- `python3` (used by `list-follow-ups`).
- **The forge**, from `git remote get-url origin`: `github.com` → `gh`; a GitLab host → `glab`; anything else or no
  remote → `none`. Check the CLI is installed (`gh --version`, `glab --version`) and logged in (`gh auth status`,
  `glab auth status`). When it isn't, give the install link or command for the person's OS and the login command,
  and offer to run them (`gh auth login` and `glab auth login` are interactive: suggest the person runs them).
- The **default branch**: `git symbolic-ref refs/remotes/origin/HEAD`, else ask.

## 2. Tracker

Ask which tracker the project uses: GitHub Issues, GitLab issues, Jira, Linear, or none. Recommend the forge's own
when the person has no preference. Then read the matching guide in `<skill-dir>/../../references/trackers/` and:

- ask for `tracker-project` (the repo, project key or team) and an optional `tracker-board`;
- ask how epics, stories and tickets map onto it, offering the guide's default; look the project's issue types or
  board columns up rather than guessing;
- run the guide's **check access** read and show the result. If it fails, show the error and fix access before going
  on, or record `tracker: none` for now.

`key-prefix` follows from the tracker: `GH-` for GitHub, the project key and a hyphen for Jira (`SHOP-`), the team
key for Linear (`ENG-`), a prefix the person picks for GitLab (`GL-` by default), empty for none.

## 3. Planning root and project rules

- **Planning root:** propose `planning/` at the project root. Ask whether it is committed (the team shares the
  plans) or gitignored (personal notes).
- **Project rules:** ask for the project's own conventions, as sentences, e.g. what a story point means, the language
  of issue titles, labels or fields every issue needs, branch naming. groundwork has none built in; say so, and
  that "none" is a fine answer.

## 4. Write `groundwork.md`

Write it at the project root in the format of `<skill-dir>/../../references/structure.md` ("`groundwork.md`"). Show
the full file and ask before writing it. Then ask, each separately:

- commit `groundwork.md`, or add it to `.gitignore`;
- add the planning root to `.gitignore` when it was chosen as personal;
- add one line to `AGENTS.md` (create the file if needed): `Planning follows groundwork: read groundwork.md before
  planning or building anything.`

Create the planning root with an empty `follow-ups/` folder.

## 5. The Karpathy guidelines

Offer to add Andrej Karpathy's coding guidelines (think before coding, simplicity first, surgical changes,
goal-driven execution). The text has no licence, so groundwork never bundles it: download it from its source when the
person agrees.

```bash
curl -fsSL https://raw.githubusercontent.com/multica-ai/andrej-karpathy-skills/main/CLAUDE.md
```

- If the download fails, say so, link https://github.com/multica-ai/andrej-karpathy-skills, and skip this step.
  Never write the guidelines from memory.
- **`AGENTS.md`:** append them under `## Coding guidelines`, with a line naming the source URL, dropping the file's
  own `# CLAUDE.md` heading. If they are already there, say so and change nothing.
- **`CLAUDE.md`:** Claude Code reads `CLAUDE.md`, not `AGENTS.md`. If `CLAUDE.md` doesn't exist, create it holding
  `@AGENTS.md`; if it exists without that line, offer to add it at the top.
- **Other agents**, only when their files already exist: `GEMINI.md` (add `@AGENTS.md`), `.cursor/rules/` (a
  `karpathy-guidelines.mdc` rule with `alwaysApply: true` and the same text),
  `.github/copilot-instructions.md` (append the text). Codex reads `AGENTS.md` itself.

Show each file's change before writing it.

## 6. Skills groundwork builds with

`/groundwork:implement` and prototypes use Matt Pocock's `tdd`, `code-review` and `prototype` skills. Check
`claude plugin list` for `mattpocock-skills`; if it's missing, offer:

```bash
claude plugin marketplace add mattpocock/skills
claude plugin install mattpocock-skills@mattpocock
```

Outside Claude Code, point to https://github.com/mattpocock/skills instead.

## 7. Report

One short summary: what was set, what was skipped, and what to run next (`/groundwork:shape` for an idea that isn't
defined yet, `/groundwork:create-ticket`, `create-story` or `create-epic` when the level is known).
