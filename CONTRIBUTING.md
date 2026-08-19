# Contributing

Contributions that improve theory reconstruction, humanities and social-science applicability, bilingual clarity, validation, or documentation are welcome.

## Before opening a pull request

1. Keep `SKILL.md` focused on routing, non-obvious constraints, and output contracts. Put conditional detail in `references/` and reusable output structures in `assets/`.
2. Preserve the distinction between `[P]`, `[S]`, and `[A]`; define `[P/A]` and `[S/A]` in the reading guide, use mixed labels only exceptionally, and avoid paragraph-by-paragraph provenance prefixes.
3. Do not add user documents, copyrighted source texts, private Zotero data, fabricated citations, or examples that could be mistaken for real scholarship.
4. Keep English and Simplified Chinese templates behaviorally aligned; wording need not be mechanically identical.
5. Explain the purpose and inferential limit before every new visual.
6. Add or update tests for observable behavior rather than matching incidental wording.

Run:

```bash
python -m unittest discover -s tests -v
python skills/analyze-theory/scripts/validate_theory_dossier.py \
  --reading examples/en/Demo_Relational_Gatekeeping_Reading_Note.md \
  --reception examples/en/Demo_Relational_Gatekeeping_Scholarly_Reception_and_Applications.md \
  --case-lab examples/en/Demo_Relational_Gatekeeping_Theory_to_Case_Lab.md
```

Describe what changed, why it improves scholarly use, and which checks were run. New source claims require verifiable citations.
