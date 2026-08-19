from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/analyze-theory"


class SkillStructureTests(unittest.TestCase):
    def test_required_skill_files_exist(self):
        required = [
            "SKILL.md",
            "agents/openai.yaml",
            "assets/theory-dossier-template.md",
            "assets/theory-dossier-template.zh-CN.md",
            "assets/scholarly-reception-application-template.md",
            "assets/scholarly-reception-application-template.zh-CN.md",
            "assets/theory-to-case-lab-template.md",
            "assets/theory-to-case-lab-template.zh-CN.md",
            "references/visual-expression-protocol.md",
            "references/theory-to-case-lab-protocol.md",
            "scripts/validate_theory_dossier.py",
        ]
        for relative in required:
            self.assertTrue((SKILL / relative).is_file(), relative)

    def test_skill_frontmatter_is_discoverable(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        self.assertRegex(text, r"(?m)^name:\s*analyze-theory\s*$")
        self.assertRegex(text, r"(?m)^description:\s*\S.+$")
        self.assertIn("Do not use for PDF formatting", text)

    def test_ui_prompt_names_the_skill(self):
        text = (SKILL / "agents/openai.yaml").read_text(encoding="utf-8")
        self.assertIn("$analyze-theory", text)
        short = re.search(r'short_description:\s*"([^"]+)"', text)
        self.assertIsNotNone(short)
        self.assertGreaterEqual(len(short.group(1)), 25)
        self.assertLessEqual(len(short.group(1)), 64)

    def test_case_templates_are_behaviorally_aligned(self):
        english = (SKILL / "assets/theory-to-case-lab-template.md").read_text(encoding="utf-8")
        chinese = (SKILL / "assets/theory-to-case-lab-template.zh-CN.md").read_text(encoding="utf-8")
        for token in ("[P]", "[S]", "[A]", "[P/A]", "[S/A]", "```mermaid", "<mark>", "<u>"):
            self.assertIn(token, english)
            self.assertIn(token, chinese)
        self.assertIn("Rival Explanations", english)
        self.assertIn("对手解释", chinese)

    def test_python_cache_is_ignored(self):
        text = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("__pycache__/", text)


if __name__ == "__main__":
    unittest.main()
