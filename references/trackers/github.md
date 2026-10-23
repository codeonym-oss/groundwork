# GitHub Issues

Through `gh` (logged in with the `repo` scope, plus `project` when a board is used). `tracker-project` is
`OWNER/REPO`; `tracker-board` is an optional GitHub Project number owned by the same owner.

## Levels

GitHub has no epic or story types. Every level is an issue; a child is a **sub-issue** of its parent. Projects that
want the level visible add a label as a project rule (groundwork adds none by default).

## Check access

```bash
gh repo view OWNER/REPO --json name,hasIssuesEnabled
gh project view BOARD --owner OWNER --format json   # only with a board
```

## Create an issue

```bash
url=$(gh issue create -R OWNER/REPO --title "TITLE" --body-file path/to/draft.md)
number=${url##*/}
```

**Parent:** sub-issues take the child's id, not its number.

```bash
child_id=$(gh api repos/OWNER/REPO/issues/$number --jq .id)
gh api -X POST repos/OWNER/REPO/issues/PARENT_NUMBER/sub_issues -F sub_issue_id=$child_id
```

**Board:** add the issue, then set its status (look the field and option ids up once per session).

```bash
item=$(gh project item-add BOARD --owner OWNER --url "$url" --format json --jq .id)
project_id=$(gh project view BOARD --owner OWNER --format json --jq .id)
gh project field-list BOARD --owner OWNER --format json \
  --jq '.fields[] | select(.name=="Status") | {id, options}'
gh project item-edit --id "$item" --project-id "$project_id" --field-id FIELD_ID --single-select-option-id OPTION_ID
```

The key is `<key-prefix><number>` (e.g. `GH-12`).

## Read an issue

```bash
gh issue view NUMBER -R OWNER/REPO --json number,title,state,body,url
gh api repos/OWNER/REPO/issues/NUMBER/sub_issues --jq '[.[].number]'
```

## Set a status

On a board, `gh project item-edit` as above with the matching option (Todo, In Progress, Done, or the board's own).
Without a board, an open issue is in progress and a closed one is done: there is nothing to set.

## Link the pull request

Put `Fixes #NUMBER` in the pull request body; GitHub links it and closes the issue on merge.

```bash
gh pr create --base DEFAULT_BRANCH --head BRANCH --title "TITLE" --body-file pr.md
```

## Close

`Fixes #NUMBER` closes it on merge. Otherwise: `gh issue close NUMBER -R OWNER/REPO --reason completed` (or
`--reason "not planned"` for a dropped level).
