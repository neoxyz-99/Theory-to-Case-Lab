from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "skills/analyze-theory/scripts/validate_theory_dossier.py"
SPEC = importlib.util.spec_from_file_location("theory_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidatorTests(unittest.TestCase):
    def bundle(self, language: str):
        if language == "en":
            base = ROOT / "examples/en"
            return (
                base / "Demo_Relational_Gatekeeping_Reading_Note.md",
                base / "Demo_Relational_Gatekeeping_Scholarly_Reception_and_Applications.md",
                base / "Demo_Relational_Gatekeeping_Theory_to_Case_Lab.md",
            )
        base = ROOT / "examples/zh-CN"
        return (
            base / "示例_关系守门_文献解读.md",
            base / "示例_关系守门_学界评价与理论应用.md",
            base / "示例_关系守门_理论解释案例实验室.md",
        )

    def changed_copy(self, source: Path, old: str, new: str) -> Path:
        tmp = Path(tempfile.mkdtemp()) / source.name
        original = source.read_text(encoding="utf-8")
        self.assertIn(old, original)
        tmp.write_text(original.replace(old, new, 1), encoding="utf-8")
        return tmp

    def test_english_three_file_bundle_passes(self):
        result = VALIDATOR.validate_bundle(*self.bundle("en"))
        self.assertTrue(result["passed_structural_check"], result)
        self.assertEqual(result["mode"], "three-file")

    def test_chinese_three_file_bundle_passes(self):
        result = VALIDATOR.validate_bundle(*self.bundle("zh-CN"))
        self.assertTrue(result["passed_structural_check"], result)

    def test_pair_mode_remains_compatible(self):
        reading, reception, _ = self.bundle("en")
        result = VALIDATOR.validate_bundle(reading, reception)
        self.assertTrue(result["passed_structural_check"], result)
        self.assertEqual(result["mode"], "paired")

    def test_legacy_mode_remains_compatible(self):
        text = """# Legacy Theory Dossier
## Corpus and Method
## Theory at a Glance
## Concepts
## Logical Architecture
## Cases
## Strengths and Limitations
## Research Landscape
## Controversies
## Paper Application
## References
[P] Demonstration content.
"""
        path = Path(tempfile.mkdtemp()) / "legacy.md"
        path.write_text(text, encoding="utf-8")
        self.assertTrue(VALIDATOR.validate(path)["passed_structural_check"])

    def test_missing_search_date_fails(self):
        reading, reception, case_lab = self.bundle("en")
        broken = self.changed_copy(reception, "- Search date: 2026-08-19", "- Search date:")
        self.assertFalse(VALIDATOR.validate_bundle(reading, broken, case_lab)["passed_structural_check"])

    def test_metadata_mismatch_fails(self):
        reading, reception, case_lab = self.bundle("en")
        broken = self.changed_copy(reception, "- Year: 2026", "- Year: 2025")
        result = VALIDATOR.validate_bundle(reading, broken, case_lab)
        self.assertFalse(result["passed_structural_check"])
        self.assertIn("Year", result["metadata_mismatches"])

    def test_broken_reciprocal_link_fails(self):
        reading, reception, case_lab = self.bundle("en")
        text = reading.read_text(encoding="utf-8").replace(
            "Demo_Relational_Gatekeeping_Theory_to_Case_Lab", "Wrong_Case_Lab"
        )
        broken = Path(tempfile.mkdtemp()) / reading.name
        broken.write_text(text, encoding="utf-8")
        result = VALIDATOR.validate_bundle(broken, reception, case_lab)
        self.assertFalse(result["passed_structural_check"])
        self.assertIn("reading", result["link_failures"])

    def test_visual_without_purpose_callout_fails(self):
        _reading, _reception, case_lab = self.bundle("en")
        broken = self.changed_copy(case_lab, "> [!info] Purpose of this visual", "> [!note] Diagram")
        result = VALIDATOR.validate(broken, "case-lab")
        self.assertFalse(result["passed_structural_check"])
        self.assertTrue(any("purpose callout" in item for item in result["warnings"]))

    def test_visual_without_evidence_class_in_callout_fails(self):
        _reading, _reception, case_lab = self.bundle("en")
        broken = self.changed_copy(
            case_lab,
            "Evidence class: `[A]`, grounded in synthetic `[P]` and `[S]` claims.",
            "The pathway is a demonstration reconstruction.",
        )
        result = VALIDATOR.validate(broken, "case-lab")
        self.assertFalse(result["passed_structural_check"])
        self.assertTrue(any("evidence-class" in item for item in result["warnings"]))

    def test_semantic_emphasis_without_reading_guide_fails(self):
        reading, _reception, _case_lab = self.bundle("en")
        text = reading.read_text(encoding="utf-8")
        start = text.index("> [!tip] Reading guide")
        end = text.index("\n\n", start)
        tmp = Path(tempfile.mkdtemp()) / reading.name
        tmp.write_text(text[:start] + text[end + 2 :], encoding="utf-8")
        result = VALIDATOR.validate(tmp, "reading")
        self.assertFalse(result["passed_structural_check"])
        self.assertTrue(any("Reading guide" in item for item in result["warnings"]))

    def test_unresolved_placeholder_fails(self):
        reading, _reception, _case_lab = self.bundle("en")
        broken = self.changed_copy(reading, "- Title: Relational Gatekeeping", "- Title: {{title}}")
        self.assertFalse(VALIDATOR.validate(broken, "reading")["passed_structural_check"])

    def test_unresolved_case_path_fails(self):
        _reading, _reception, case_lab = self.bundle("en")
        broken = self.changed_copy(case_lab, "- Selected path: causal", "- Selected path: causal / interpretive")
        self.assertFalse(VALIDATOR.validate(broken, "case-lab")["passed_structural_check"])


if __name__ == "__main__":
    unittest.main()
