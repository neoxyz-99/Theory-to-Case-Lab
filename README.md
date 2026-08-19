# Theory-to-Case Lab

[中文说明](README.zh-CN.md) · [MIT License](LICENSE) · [Contributing](CONTRIBUTING.md)

A bilingual Agent Skill for reconstructing theories, mapping scholarly reception, and explaining cases across the humanities and social sciences.

Theory-to-Case Lab turns a focal theoretical work into two linked Markdown notes by default:

1. a source-grounded **Reading Note**;
2. a verified **Scholarly Reception and Applications** note.

When a concrete research case is supplied, it adds an optional third **Theory-to-Case Lab** note that reconstructs the explanatory or interpretive pathway, identifies evidence, tests rival accounts, and states boundaries.

## Why this is different

Representative academic-agent projects often emphasize literature discovery, review writing, paper critique, or theory synthesis—for example [Literature Review Skills](https://github.com/xingtaxueshu/literature-review-skills), [LitReviewSkill](https://github.com/Zsun79/LitReviewSkill), and [Asta Theorizer](https://github.com/allenai/asta-theorizer). Theory-to-Case Lab overlaps with those projects at the general search, synthesis, and citation layers. Its distinctive contribution is the complete path from primary-text reconstruction to reception mapping, epistemically appropriate case explanation, and paper-ready analysis.

- **Low-noise evidence provenance:** the reading guide defines `[P]` focal text, `[S]` external scholarship, `[A]` analyst reconstruction, and the exceptional mixed forms `[P/A]` and `[S/A]`. The body labels only points of possible ambiguity instead of prefixing every paragraph.
- **Paired epistemic architecture:** what the work argues is not collapsed into how later scholars interpret, criticize, revise, or apply it.
- **Mechanism before labeling:** a case is not “explained” merely because concepts have been attached to it.
- **Plural explanatory forms:** causal, interpretive, critical, genealogical, and normative theories use different pathways.
- **Rivals and boundaries:** applications include counterfactuals or alternative readings, disconfirming evidence, and scope limits.
- **Analytical visuals:** diagrams explain structures, sequences, debates, or levels; every visual states its purpose, encoding, evidence class, and inferential limit first.
- **Bilingual research workflow:** English and Simplified Chinese templates preserve original-language concepts and support Obsidian wikilinks and verified Zotero URIs.

This comparison is a purposeful representative scan, not a claim that no related project exists.

## Output contract

| Situation | English files | Chinese files |
|---|---|---|
| Focal theory source | `Author_Short_Title_Reading_Note.md` + `Author_Short_Title_Scholarly_Reception_and_Applications.md` | `作者_短标题_文献解读.md` + `作者_短标题_学界评价与理论应用.md` |
| Concrete case supplied | Add `Author_Short_Title_Theory_to_Case_Lab.md` | Add `作者_短标题_理论解释案例实验室.md` |

The reception note always reports search date, databases or tools, query scope, inclusion logic, and access limits. If the evidence base is thin, the note records that limitation instead of manufacturing consensus or citations.

## Explanatory pathways

For causal or mechanism-oriented theories:

```text
outcome difference → theoretical position → resources and constraints
→ mechanism → changed choice set → outcome and distributional effects
```

For interpretive, critical, genealogical, or normative theories:

```text
text/practice → conceptual location → interpretive operation
→ meaning or power relation revealed → alternative reading → boundary
```

The skill does not force interpretive work into causal notation.

## Visual contract

Every diagram begins with a short purpose callout explaining:

- why prose or a table is insufficient;
- what nodes and arrows encode;
- whether the visual is grounded in `[P]`, `[S]`, or reconstructed as `[A]`;
- what the visual cannot establish.

The durable outputs use Markdown tables and Mermaid. Interactive visuals are created only when explicitly requested. Default maxima are two diagrams in each paired note and three in the Case Lab.

The opening reading guide defines all simple and mixed provenance labels. A slash means “source material plus analysis,” not a new source type; the preferred practice is to separate source claims from analysis and reserve mixed labels for short syntheses that cannot be split naturally. Semantic emphasis has stable meaning: **bold** for core claims or mechanisms, `<mark>highlight</mark>` for directly reusable research findings, <u>underline</u> for boundaries or recurrent misreadings, and *italics* for wording-sensitive terms. Styling never replaces evidence provenance.

## Install

### Codex

Install from this repository with the Skill Installer, or copy the skill directory into your Codex skills folder:

```bash
git clone https://github.com/neoxyz-99/Theory-to-Case-Lab.git
cp -R Theory-to-Case-Lab/skills/analyze-theory "$CODEX_HOME/skills/analyze-theory"
```

If `CODEX_HOME` is unset, Codex normally uses `~/.codex`.

### Other Agent Skills-compatible tools

Copy `skills/analyze-theory` into the tool's documented skills directory. The core instructions, Markdown assets, references, and validator are self-contained; availability of scholarly search, PDF extraction, OCR, or Zotero access depends on the host tool.

## Use

Example prompts:

```text
Use $analyze-theory to analyze this uploaded theoretical article in Chinese.
Create the paired reading and reception notes, and preserve the original concepts.
```

```text
Use $analyze-theory to apply this theory to my case.
Create the optional Theory-to-Case Lab and compare a serious rival explanation.
```

## Validate

Paired notes:

```bash
python skills/analyze-theory/scripts/validate_theory_dossier.py \
  --reading path/to/Reading_Note.md \
  --reception path/to/Scholarly_Reception_and_Applications.md
```

Three-file bundle:

```bash
python skills/analyze-theory/scripts/validate_theory_dossier.py \
  --reading path/to/Reading_Note.md \
  --reception path/to/Scholarly_Reception_and_Applications.md \
  --case-lab path/to/Theory_to_Case_Lab.md
```

Run the repository tests with:

```bash
python -m unittest discover -s tests -v
```

The validator checks structure and provenance signals; it cannot replace scholarly judgment or verification against original sources.

## Repository map

- `skills/analyze-theory/SKILL.md` — routing, output contract, and quality gate.
- `skills/analyze-theory/assets/` — English and Chinese templates.
- `skills/analyze-theory/references/` — close reading, reception, application, evidence, Case Lab, and visual protocols.
- `skills/analyze-theory/scripts/` — deterministic validation.
- `examples/` — synthetic bilingual demonstrations, never citable scholarship.
- `tests/` — regression and failure-mode tests.

## Privacy and copyright

This repository contains no uploaded books, articles, private research notes, Zotero libraries, or user documents. Do not commit source texts unless you have the right to redistribute them. Examples are explicitly synthetic and must not be cited as scholarship.

## Scope and limitations

- Scholarly reception defaults to a purposeful representative review, not a systematic review or bibliometric analysis.
- A Zotero link is emitted only when its URI is known; item keys are never guessed.
- Search rankings and citation counts are discovery signals, not proof of quality or consensus.
- Visual proximity and arrows are not evidence by themselves.

## Citation

See [CITATION.cff](CITATION.cff). For software citation, use `Theory-to-Case Lab, version 1.0.0, neoxyz-99, 2026`.
