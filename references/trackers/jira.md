# Jira

Prefer the **Atlassian connector (MCP)** when the session has one; otherwise the **Atlassian CLI** (`acli`, logged in
with `acli jira auth login`). `tracker-project` is the project key (e.g. `SHOP`).

## Levels

Jira has its own issue types. Map each level to a type the project has (ask at init; look them up rather than
guess): usually **Epic**, **Story**, and **Task** (or **Sub-task** under a story when the project works that way). A
child names its parent with `--parent` (the parent's key). The key is Jira's own (`SHOP-123`), so `key-prefix` is
`SHOP-`.

## Check access

```bash
acli jira project view --key SHOP
```

With the connector: get the accessible sites, then read the project (or search one issue with JQL
`project = SHOP ORDER BY created DESC`).

## Create an issue

```bash
acli jira workitem create --project SHOP --type Story --summary "TITLE" \
  --description-file path/to/draft.md --parent SHOP-10 --json
```

With the connector: its create-issue operation, with the project key, the issue type, the summary, the description
and the parent key. If the operation's name isn't known, discover it from the connector rather than guessing.

Story points, components, sprints and other custom fields are set only when a project rule asks for them.

## Read an issue

```bash
acli jira workitem view SHOP-123 --fields summary,status,parent,description --json
```

## Set a status

Jira moves an issue through transitions; use the project's own status names.

```bash
acli jira workitem transition --key SHOP-123 --status "In Progress"
```

## Link the pull or merge request

Put the key in the branch name and the pull/merge request title (`SHOP-123 …`); Jira's development panel links them
when the forge integration is installed. Without it, add the request's URL as a comment.

## Close

```bash
acli jira workitem transition --key SHOP-123 --status "Done"
```
