"""list_follow_ups.py: finding, filtering and ordering follow-ups across the tree."""
import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "skills/list-follow-ups/scripts/list_follow_ups.py"
spec = importlib.util.spec_from_file_location("list_follow_ups", SCRIPT)
list_follow_ups = importlib.util.module_from_spec(spec)
sys.modules["list_follow_ups"] = list_follow_ups
spec.loader.exec_module(list_follow_ups)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ListFollowUpsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.project = Path(self.tmp.name)
        self.root = self.project / "planning"
        write(self.project / "groundwork.md", "---\nplanning-root: planning\ntracker: github\n---\n")
        write(self.root / "follow-ups/2026-10-01_0900_old-note.md", "# An old note without a header\n")
        story = self.root / "GH-1-shop"
        write(story / "meta.md", "---\nkind: story\nkey: GH-1\n---\n")
        write(
            story / "follow-ups/2026-10-05_1000_slow-list.md",
            "---\nstatus: open\nfrom: agent    # noticed mid-task\nfound-while: GH-2\nresolved-by:\n---\n\n# The list is slow\n",
        )
        ticket = story / "tickets/GH-2-cart"
        write(ticket / "meta.md", "---\nkind: ticket\nkey: GH-2\n---\n")
        write(
            ticket / "follow-ups/2026-10-03_1200_done-thing.md",
            "---\nstatus: done\nfrom: person\nresolved-by: GH-3\n---\n\n# A done thing\n",
        )
        write(ticket / "follow-ups/2026-10-02_0800_cart-rounding.md", "---\nstatus: open\nfrom: person\n---\n\n# Cart rounds\n")

    def tearDown(self):
        self.tmp.cleanup()

    def run_script(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = list_follow_ups.main(["--root", str(self.root), "--today", "2026-10-11", *args])
        return code, out.getvalue()

    def titles(self, output):
        return [line.split("  ")[-1].strip() for line in output.splitlines() if line.strip()[:1].isdigit() and "d  " in line]

    def test_open_ones_oldest_first_at_every_level(self):
        code, output = self.run_script()
        self.assertEqual(code, 0)
        self.assertEqual(self.titles(output), ["An old note without a header", "Cart rounds", "The list is slow"])

    def test_a_header_less_file_is_open_from_a_person_at_the_root(self):
        _, output = self.run_script()
        first = output.splitlines()[0]
        self.assertIn("10d", first)
        self.assertIn("root", first)
        self.assertIn("person", first)

    def test_level_and_author_come_from_meta_and_header(self):
        _, output = self.run_script()
        line = next(l for l in output.splitlines() if "The list is slow" in l)
        self.assertIn("GH-1", line)
        self.assertIn("agent", line)

    def test_all_includes_closed_ones_marked(self):
        _, output = self.run_script("--all")
        self.assertIn("A done thing [done]", output)

    def test_level_keeps_that_level_and_below(self):
        _, output = self.run_script("--level", "GH-2")
        self.assertEqual(self.titles(output), ["Cart rounds"])
        _, output = self.run_script("--level", "GH-1")
        self.assertEqual(self.titles(output), ["Cart rounds", "The list is slow"])

    def test_root_found_from_groundwork_md(self):
        self.assertEqual(list_follow_ups.find_root(self.root / "GH-1-shop"), self.root)


if __name__ == "__main__":
    unittest.main()
