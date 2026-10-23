#!/usr/bin/env python3
"""List the follow-ups of a groundwork planning tree, oldest first.

Usage: list_follow_ups.py [--root DIR] [--all] [--level KEY] [--today YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

FILE_NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})_(\d{4})_(.+)\.md$")


@dataclass
class FollowUp:
    path: Path
    found_on: date
    time: str
    title: str
    status: str
    author: str
    level: str


def read_header(text: str) -> tuple[dict[str, str], str]:
    """The `key: value` fields between the leading `---` lines, and the text after them."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    fields: dict[str, str] = {}
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return fields, "\n".join(lines[index + 1 :])
        key, _, value = line.partition(":")
        fields[key.strip()] = value.split("#", 1)[0].strip()
    return {}, text


def title_of(body: str, slug: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return slug.replace("-", " ")


def level_of(follow_ups_dir: Path, root: Path) -> str:
    """The key of the level a follow-ups folder belongs to, or `root`."""
    level_dir = follow_ups_dir.parent
    if level_dir == root:
        return "root"
    meta = level_dir / "meta.md"
    if meta.is_file():
        fields, _ = read_header(meta.read_text(encoding="utf-8"))
        if fields.get("key"):
            return fields["key"]
    return level_dir.name


def find_root(start: Path) -> Path | None:
    """The planning root named by the nearest `groundwork.md` above `start`."""
    for folder in [start, *start.parents]:
        settings = folder / "groundwork.md"
        if settings.is_file():
            fields, _ = read_header(settings.read_text(encoding="utf-8"))
            return folder / fields.get("planning-root", "planning")
    return None


def collect(root: Path) -> list[FollowUp]:
    follow_ups = []
    for path in sorted(root.rglob("follow-ups/*.md")):
        match = FILE_NAME.match(path.name)
        if not match:
            continue
        found_on, time, slug = match.groups()
        fields, body = read_header(path.read_text(encoding="utf-8"))
        follow_ups.append(
            FollowUp(
                path=path,
                found_on=date.fromisoformat(found_on),
                time=time,
                title=title_of(body, slug),
                status=fields.get("status") or "open",
                author=fields.get("from") or "person",
                level=level_of(path.parent, root),
            )
        )
    return follow_ups


def in_level(follow_up: FollowUp, root: Path, key: str) -> bool:
    """True when the follow-up sits in the level named `key` or anywhere under it."""
    relative = follow_up.path.relative_to(root).parts
    return follow_up.level == key or any(part == key or part.startswith(f"{key}-") for part in relative)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, help="the planning root (default: from groundwork.md)")
    parser.add_argument("--all", action="store_true", help="include done and dropped follow-ups")
    parser.add_argument("--level", help="only this level (a key or folder name) and the levels under it")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today(), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    root = args.root or find_root(Path.cwd())
    if root is None or not root.is_dir():
        print("No planning root found: run /groundwork:init, or pass --root.", file=sys.stderr)
        return 1
    root = root.resolve()

    follow_ups = collect(root)
    if not args.all:
        follow_ups = [f for f in follow_ups if f.status == "open"]
    if args.level:
        follow_ups = [f for f in follow_ups if in_level(f, root, args.level)]
    follow_ups.sort(key=lambda f: (f.found_on, f.time, str(f.path)))

    if not follow_ups:
        print("No open follow-ups." if not args.all else "No follow-ups.")
        return 0

    level_width = max(len(f.level) for f in follow_ups)
    for f in follow_ups:
        waited = (args.today - f.found_on).days
        status = "" if f.status == "open" else f" [{f.status}]"
        print(f"{waited:>4}d  {f.level:<{level_width}}  {f.author:<6}  {f.title}{status}")
        print(f"       {f.path.relative_to(root)}")
    print(f"\n{len(follow_ups)} follow-up(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
