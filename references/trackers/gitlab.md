# GitLab issues

Through `glab` (logged in). `tracker-project` is `GROUP/PROJECT` (or `GROUP/SUBGROUP/PROJECT`).

## Levels

- **Epics** exist on GitLab Premium and Ultimate only. With them, an epic is a group epic and its stories join it with
  `--epic`. Without them, an epic is an issue like the others.
- **Stories and tickets** are issues. A child is **linked** to its parent (`--linked-issues`) and its description
  starts with `Parent: #PARENT_IID`, so the relation shows on both sides on every tier.

Ask at init which applies; record it in `epic-as` / `story-as` / `ticket-as`.

## Check access

```bash
glab repo view GROUP/PROJECT
glab issue list -R GROUP/PROJECT --per-page 1
```

## Create an issue

```bash
glab issue create -R GROUP/PROJECT --title "TITLE" --description-file path/to/draft.md \
  --linked-issues PARENT_IID --link-type relates_to --yes
```

The command prints the issue URL; the IID is its last segment. Add `--epic EPIC_ID` when the parent is an epic on a
paid tier. The key is `<key-prefix><iid>`.

**An epic on a paid tier:**

```bash
glab api --method POST "groups/GROUP_ID/epics" -f title="TITLE" -f description="$(cat path/to/draft.md)"
```

## Read an issue

```bash
glab issue view IID -R GROUP/PROJECT --output json
glab api "projects/:id/issues/IID/links"
```

## Set a status

GitLab statuses are labels or the board's lists (e.g. `workflow::in progress`) when the project uses them; use the
project's own, recorded as a project rule. Without them, open is in progress and closed is done.

```bash
glab issue update IID -R GROUP/PROJECT --label "workflow::in progress" --unlabel "workflow::todo"
```

## Link the merge request

Put `Closes #IID` in the merge request description; GitLab links it and closes the issue on merge.

```bash
glab mr create --source-branch BRANCH --target-branch DEFAULT_BRANCH --title "TITLE" --description-file mr.md --yes
```

## Close

`Closes #IID` closes it on merge. Otherwise: `glab issue close IID -R GROUP/PROJECT`.
