"""Repo consistency: the manifest, the skills and the references agree."""
import json
import re
import unittest
from pathlib import Path

REPO = Path(__file__).parent.parent
TRACKER_HEADINGS = [
    "## Levels",
    "## Check access",
    "## Create an issue",
    "## Read an issue",
    "## Set a status",
    "## Close",
]


def frontmatter(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "---", f"{path} has no frontmatter"
    end = lines.index("---", 1)
    return dict(line.split(": ", 1) for line in lines[1:end])


class RepoTest(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((REPO / ".claude-plugin/plugin.json").read_text())
        self.portable = json.loads((REPO / "plugin.json").read_text())

    def test_every_listed_skill_has_a_named_skill_md(self):
        for entry in self.manifest["skills"]:
            skill_md = REPO / entry / "SKILL.md"
            self.assertTrue(skill_md.is_file(), skill_md)
            fields = frontmatter(skill_md)
            self.assertEqual(fields["name"], Path(entry).name)
            self.assertGreater(len(fields["description"]), 40)

    def test_every_skill_folder_is_listed(self):
        listed = {Path(entry).name for entry in self.manifest["skills"]}
        on_disk = {p.parent.name for p in (REPO / "skills").glob("*/SKILL.md")}
        self.assertEqual(listed, on_disk)

    def test_versions_agree(self):
        version = (REPO / "VERSION").read_text().strip()
        self.assertEqual(self.manifest["version"], version)
        self.assertEqual(self.portable["version"], version)
        manifest = json.loads((REPO / ".release-please-manifest.json").read_text())
        self.assertEqual(manifest["."], version)

    def test_portable_manifest_matches_the_claude_one(self):
        # Codex reads the portable plugin.json and finds the skills in skills/ itself.
        allowed = {"$schema", "name", "version", "description", "author", "homepage", "repository", "license",
                   "keywords", "extensions"}
        self.assertLessEqual(set(self.portable), allowed)
        for field in allowed - {"$schema", "extensions"}:
            self.assertEqual(self.portable[field], self.manifest[field], field)
        openai = self.portable["extensions"]["com.openai"]
        self.assertTrue((REPO / openai["onboardingSkill"]).is_file())
        for key in ("composerIcon", "logo"):
            self.assertTrue((REPO / openai["interface"][key]).is_file(), key)

    def test_referenced_files_exist(self):
        pattern = re.compile(r"<skill-dir>/(\.\./\.\./references/[\w./-]+?\.md|scripts/[\w.-]+)")
        for skill_md in (REPO / "skills").glob("*/SKILL.md"):
            for target in pattern.findall(skill_md.read_text(encoding="utf-8")):
                self.assertTrue((skill_md.parent / target).resolve().exists(), f"{skill_md}: {target}")

    def test_reference_names_used_bare_exist(self):
        names = {"structure.md", "grilling.md", "approval.md", "drafting.md"}
        for name in names:
            self.assertTrue((REPO / "references" / name).is_file(), name)

    def test_tracker_guides_cover_every_operation(self):
        guides = [p for p in (REPO / "references/trackers").glob("*.md") if p.name != "README.md"]
        self.assertEqual({p.stem for p in guides}, {"github", "gitlab", "jira", "linear", "none"})
        for guide in guides:
            text = guide.read_text(encoding="utf-8")
            for heading in TRACKER_HEADINGS:
                self.assertIn(heading, text, f"{guide.name} lacks {heading}")
            self.assertRegex(text, r"## Link the (pull|merge|pull or merge) request")

    def test_no_bundled_karpathy_text(self):
        # The guidelines have no licence: groundwork fetches them, never ships them (decision 022).
        marker = "Don't assume. Don't hide confusion. Surface tradeoffs."
        for path in REPO.rglob("*.md"):
            if ".git" in path.parts:
                continue
            self.assertNotIn(marker, path.read_text(encoding="utf-8"), path)


if __name__ == "__main__":
    unittest.main()
