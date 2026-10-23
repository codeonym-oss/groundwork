# groundwork: notes for coding agents

- Public Claude Code plugin `groundwork` (skills are `groundwork:<skill>`). Read `CONTRIBUTING.md` for how skills,
  references and tracker guides are added, and `references/structure.md` for the planning tree the skills manage.
- Issues live in GitHub Issues on this repo, on the org project "groundwork".
- `main` is protected: work on a branch named after the issue (`<n>-short-name`), open a pull request with a
  conventional-commit title and `Fixes #<n>`; never edit `VERSION` or the version in `plugin.json` by hand
  (release-please does).
- Tests: `make test`; manifest and skills: `claude plugin validate .`.
- Never add text from `multica-ai/andrej-karpathy-skills` to this repo: it has no licence (`init` fetches it instead).
