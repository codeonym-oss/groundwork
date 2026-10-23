# Security policy

## Supported versions

The latest minor release (`0.x`) gets fixes. Older versions: upgrade the plugin.

## Reporting a vulnerability

Please **don't open a public issue**. Report it privately through GitHub:
**Security → Report a vulnerability** on https://github.com/codeonym-oss/groundwork/security/advisories/new

Include what you found, how to reproduce it, and the impact. You'll get an acknowledgement within 7 days and a fix or
mitigation plan within 30.

## Scope

- A skill that writes outside the planning folder, runs a command, or changes the tracker **without asking first**.
- Commands in the skills or tracker guides that could be turned into command injection through a title, a slug, a
  branch name or a file name.
- `scripts/`: unsafe file handling.
- Out of scope: the forge and tracker CLIs and services themselves (report those to their vendors).
