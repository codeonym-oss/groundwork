# Linear

Prefer the **Linear connector (MCP)** when the session has one; otherwise Linear's **GraphQL API** with a personal API
key in `LINEAR_API_KEY` (Settings → Security & access). `tracker-project` is the team key (e.g. `ENG`); the key is
Linear's identifier (`ENG-123`), so `key-prefix` is `ENG-`.

## Levels

- **Epic:** a Linear **project**.
- **Story:** an issue in that project.
- **Ticket:** a **sub-issue** of its story (`parentId`), or an issue in the project when the story is a project
  itself. Record the mapping at init.

## Check access

With the connector: list the teams and find the team key. With the API:

```bash
curl -s https://api.linear.app/graphql -H "Authorization: $LINEAR_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":"{ teams { nodes { id key name } } }"}'
```

## Create an issue

With the connector: its create (or save) issue operation, with the team, title, description, and `parentId` or
project. With the API:

```bash
jq -n --arg team "TEAM_ID" --arg title "TITLE" --rawfile body path/to/draft.md --arg parent "PARENT_ID" \
  '{query: "mutation($i: IssueCreateInput!) { issueCreate(input: $i) { issue { identifier url } } }",
    variables: {i: {teamId: $team, title: $title, description: $body, parentId: $parent}}}' |
curl -s https://api.linear.app/graphql -H "Authorization: $LINEAR_API_KEY" -H "Content-Type: application/json" -d @-
```

Drop `parentId` for a top-level issue; use `projectId` to place a story in an epic's project. An epic is created
with `projectCreate(input: {name, description, teamIds})`.

## Read an issue

```bash
curl -s https://api.linear.app/graphql -H "Authorization: $LINEAR_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":"{ issue(id: \"ENG-123\") { identifier title state { name } url parent { identifier } } }"}'
```

## Set a status

Find the team's workflow state id by name (`{ workflowStates(filter: {team: {key: {eq: "ENG"}}}) { nodes { id name } } }`),
then `issueUpdate(id: "ENG-123", input: {stateId: "…"})`.

## Link the pull or merge request

Put the identifier in the branch name or the request title (`ENG-123`); Linear's GitHub and GitLab integrations link
it and move the issue on merge.

## Close

Move it to the team's completed state (`issueUpdate` with that `stateId`), or let the integration do it on merge.
