---
name: analyze-theory
description: Analyze theories from books, articles, PDFs, notes, or a user-supplied corpus; reconstruct concepts, assumptions, mechanisms, propositions, logic, cases, strengths, limitations, genealogy, research status, scholarly applications, controversies, and research paths; then help apply the theory in a literature review, theoretical framework, research questions, propositions, hypotheses, operationalization, or analysis plan. Use for theory-focused close reading, intellectual history, research-landscape synthesis, critical comparison, or theory-to-paper design in the humanities and social sciences. Do not use for PDF formatting operations, generic summaries with no theoretical focus, or citation-style conversion alone.
---

# Analyze Theory

Produce source-grounded theory research that separates textual evidence, external scholarship, and the analyst's proposed use. Match the user's language and disciplinary conventions. Use analytical visuals only when they clarify relationships that prose or a table cannot show as efficiently.

## Select the mode

Choose the smallest mode that satisfies the request:

- `close-reading`: Interpret supplied primary texts, reconstruct the theory, and analyze cases and arguments.
- `research-landscape`: Trace genealogy, applications, debates, critiques, revisions, and current research.
- `paper-application`: Map a theory to the user's question, material, method, literature review, and theoretical framework.
- `full`: Run all three modes. Use this default when the user asks for a comprehensive theory report.

State the selected mode and corpus scope briefly. Do not block on missing preferences when a reasonable assumption is safe; list the assumption in the report.

When the user uploads or supplies a focal theory book, article, report, or chapter, the mode controls depth but not the output count: produce the paired Markdown notes defined under **Build the deliverable**. For theory questions with no focal source, answer in the smallest suitable form instead of creating empty files.

## Set the output language

Use the language explicitly requested by the user. Otherwise match the user's language. English is the canonical template language; Chinese is a supported localized output. Preserve original-language theoretical terms when translating them materially improves precision.

## Establish the evidence base

1. Inventory every supplied source before synthesizing it. Record title, author, date or edition, source type, accessibility, and role in the analysis.
2. Use the available PDF capability for PDFs. Detect image-only pages, missing text, unreadable notes, truncated files, and edition-dependent pagination. Apply OCR when available and disclose OCR uncertainty.
3. Distinguish:
   - `[P] Primary text`: what the theorist or focal source states.
   - `[S] Scholarship`: what an external scholar argues or finds.
   - `[A] Analysis`: the agent's reconstruction, evaluation, comparison, or application proposal.
   - `[P/A]` or `[S/A]`: a mixed claim combining a source-grounded statement with the agent's reconstruction or synthesis.
4. Never use `[A]` as evidence for `[P]` or `[S]`. Never invent quotations, page numbers, publication details, DOIs, or consensus.
5. For claims attributed to a source, cite the most precise available locator: page, chapter/section, figure/table, or stable URL. If pagination is unavailable, say so.
6. Keep provenance visible without turning the note into an audit log. Define all five labels in the opening reading guide, then use labels only at the smallest useful claim group, table row, or point of possible ambiguity. Do not prefix every paragraph or bullet. Prefer separating a source statement from the agent's interpretation over using `[P/A]` or `[S/A]`; reserve combined labels for genuinely inseparable short syntheses.

Read [references/evidence-and-citation.md](references/evidence-and-citation.md) whenever the task includes external research, quotations, contested attribution, or a formal paper deliverable.

## Coordinate supporting capabilities

This skill owns theory reconstruction, scholarly-reception synthesis, theory-to-case explanation, and theory-to-paper design. Treat other capabilities as supporting layers:

- PDF or document skills extract, OCR, render, or format source files;
- browsers, search, indexes, and scholarly apps discover or retrieve literature;
- Drive and document skills store or format the finished notes.

Do not substitute those access or artifact operations for the analytical workflow in this skill. Conversely, do not use this skill for generic document handling, undirected web research, citation-style conversion, or non-theoretical summarization.

## Run the workflow

### 1. Frame the theory

Identify the theory's target problem, level of analysis, explanatory or interpretive goal, historical context, disciplinary setting, and intended scope. Distinguish a theory from a concept, framework, method, school, metaphor, or normative position; explain any category ambiguity.

### 2. Reconstruct the primary text

Follow [references/close-reading-protocol.md](references/close-reading-protocol.md). Extract and connect:

- central question and intervention;
- key concepts and definitions;
- explicit and implicit assumptions;
- mechanisms, relations, or interpretive moves;
- principal claims, propositions, and conclusions;
- scope conditions, boundary conditions, and excluded cases;
- examples, cases, analogies, counterexamples, and their argumentative role;
- tensions, ambiguities, changes across chapters or editions, and missing steps.

Represent the logic as compact prose plus a Mermaid diagram when the diagram materially clarifies at least three relationships. Mark inferred links `[A]`. Read [references/visual-expression-protocol.md](references/visual-expression-protocol.md) before adding any diagram or semantic emphasis.

### 3. Evaluate the theory

Separate types of evaluation:

- explanatory or interpretive value;
- conceptual clarity and internal coherence;
- empirical support and falsifiability, when applicable;
- transferability and scope;
- methodological implications;
- normative, political, ethical, or positional assumptions;
- risks of reductionism, determinism, circularity, reification, or anachronism.

Do not collapse “controversial,” “unfalsifiable,” “normative,” and “false” into one judgment. Present the strongest charitable reading before criticism. Distinguish immanent criticism from external criticism and later revisions.

### 4. Map the research landscape

For current status, applications, disputes, or “how scholars use it,” browse and verify current sources. Follow [references/landscape-protocol.md](references/landscape-protocol.md).

Search in lanes: origin; canonical formulation; major interpretations; extensions and revisions; empirical or interpretive applications; critiques; competing theories; reviews or handbooks; and recent work. Prefer primary publications, peer-reviewed research, university-press material, and authoritative bibliographic records. Treat citation counts and search ranking as signals, not quality judgments.

Organize findings by intellectual position or research problem, not as an author-by-author list. Report meaningful agreement, disagreement, methods, application domains, gaps, and unresolved questions. Make any inference about “the field” explicit and proportionate to the searched corpus.

### 5. Translate the theory into the user's paper

Follow [references/paper-application-protocol.md](references/paper-application-protocol.md). Test fit before recommending use:

- What does the theory make visible in the user's object?
- What is the unit and level of analysis?
- Which concepts can be observed, interpreted, or operationalized?
- What mechanism or relationship connects them?
- Which evidence could challenge the proposed reading?
- What lies outside the theory's scope?
- Is the role descriptive, explanatory, interpretive, critical, normative, or generative?

Offer only applications supported by the user's question and material. When the user has not supplied a paper topic, provide adaptable options and clearly label placeholders. When the user supplies a concrete case or explicitly asks for a theory-to-case explanation, also read [references/theory-to-case-lab-protocol.md](references/theory-to-case-lab-protocol.md).

Produce, as relevant:

- a problem-driven literature-review architecture;
- a theory-selection rationale and comparison with alternatives;
- a theoretical-framework narrative and concept map;
- research questions, propositions, or hypotheses at the appropriate epistemic level;
- a construct/indicator or concept/evidence table;
- an analysis procedure or coding lens;
- limitations, rival explanations, and contribution paths;
- targeted follow-up searches and a prioritized reading list.

## Build the deliverable

For every supplied focal theory source, create two Markdown files in the selected output language while preserving original-language concepts and complete bibliographic data.

1. The reading note reconstructs what the source says, how its arguments and cases work, and how the theory could explain the user's case. It should primarily contain `[P]` and `[A]` claims.
2. The reception note maps verified scholarly interpretations, evaluations, disputes, revisions, operationalizations, and substantive applications. It should primarily contain `[S]` and `[A]` claims.

When the user supplies a concrete case or explicitly requests theory-to-case application, create a third, optional Theory-to-Case Lab note. It turns the selected theory into a traceable explanatory or interpretive pathway, tests rival accounts, specifies evidence and disconfirming observations, and states boundaries. Do not generate this third file for close reading alone.

Use these templates and filenames:

| Output language | Reading note | Reception note |
|---|---|---|
| English | [assets/theory-dossier-template.md](assets/theory-dossier-template.md) → `Author_Short_Title_Reading_Note.md` | [assets/scholarly-reception-application-template.md](assets/scholarly-reception-application-template.md) → `Author_Short_Title_Scholarly_Reception_and_Applications.md` |
| Chinese | [assets/theory-dossier-template.zh-CN.md](assets/theory-dossier-template.zh-CN.md) → `作者_短标题_文献解读.md` | [assets/scholarly-reception-application-template.zh-CN.md](assets/scholarly-reception-application-template.zh-CN.md) → `作者_短标题_学界评价与理论应用.md` |

For the optional third file use:

| Output language | Theory-to-Case Lab |
|---|---|
| English | [assets/theory-to-case-lab-template.md](assets/theory-to-case-lab-template.md) → `Author_Short_Title_Theory_to_Case_Lab.md` |
| Chinese | [assets/theory-to-case-lab-template.zh-CN.md](assets/theory-to-case-lab-template.zh-CN.md) → `作者_短标题_理论解释案例实验室.md` |

Cross-link every generated file with Obsidian wikilinks. Keep Author, Year, Title, and Type identical across them. If a Zotero URI is verified, render `[Open in Zotero](zotero://...)`; otherwise write `Zotero 链接待补`. Never infer a Zotero item key.

Before the first diagram or semantic emphasis, include a reading guide that defines `[P]`, `[S]`, `[A]`, `[P/A]`, and `[S/A]`, explains that the slash marks a mixed claim rather than a new source type, and states the low-noise labeling rule. Before every diagram, state its analytical purpose, encoding, evidence class, and inferential limit. Use the smallest suitable form: tables for exact repeated fields and Mermaid only for structures, sequences, branches, or levels. Default limits are two diagrams in each paired note and three in the Case Lab. Do not create an interactive artifact unless the user requests one.

The second file always requires external scholarly research. Record the search date, tools or databases, query families, inclusion logic, and access limits. Use a purposeful representative review unless the user requests a systematic review or bibliometric study. If little scholarship is accessible, still create the file, state the negative or limited search result precisely, separate verified references from leads, and do not invent reception, applications, consensus, or citations.

Use [assets/claim-evidence-matrix.md](assets/claim-evidence-matrix.md) for formal literature reviews, theoretical frameworks, or any request requiring traceability; it remains optional and is not a third default output file.

Keep these separations visible:

- author's formulation vs. later interpretation;
- theory's own examples vs. new illustrative examples;
- evidence-backed field description vs. search-limited inference;
- literature synthesis vs. language the user could adopt in a paper;
- theoretical proposition vs. empirical hypothesis;
- criticism of a theory vs. criticism of one application.

## Apply the quality gate

Before delivery, verify:

1. Every substantive attributed claim has a source and locator where available.
2. Direct quotations were checked against the source and are necessary.
3. Cases are tied to the claim they illustrate or test.
4. Strengths and criticisms name the criterion being used.
5. The landscape includes disagreements and negative or limiting evidence, not only supportive applications.
6. Current-status claims state search date, scope, and uncertainty.
7. Suggested paper use fits the user's unit of analysis, evidence, method, and research aim.
8. No reference is listed unless verified against a source or authoritative bibliographic record.
9. The report contains actionable next steps and verification flags for unresolved items.
10. Paired notes have consistent bibliographic metadata and reciprocal Obsidian links.
11. The reading note does not treat concept labeling as case explanation; it identifies the explanandum, mechanism or interpretive move, evidence, rival account, and boundary.
12. The reception note distinguishes substantive applications from background citations and reports the research scope.
13. Every diagram has a purpose callout, an evidence-class label, an inferential limit, and a short prose interpretation.
14. Bold, highlight, underline, and italics follow the semantic roles in the visual-expression protocol and do not replace `[P]`, `[S]`, or `[A]`.
15. When a Case Lab is present, all three notes agree bibliographically, link to one another, select an epistemically appropriate pathway, and include rival accounts, disconfirming evidence, and boundaries.
16. The body uses provenance labels sparingly: combined labels are exceptional, and repeated paragraph-level prefixes are removed when section context and precise citations already make provenance clear.

For a legacy single-file dossier, optionally run:

```bash
python scripts/validate_theory_dossier.py path/to/report.md
```

For paired notes, run:

```bash
python scripts/validate_theory_dossier.py \
  --reading path/to/Author_Short_Title_Reading_Note.md \
  --reception path/to/Author_Short_Title_Scholarly_Reception_and_Applications.md
```

For a three-file theory-to-case bundle, run:

```bash
python scripts/validate_theory_dossier.py \
  --reading path/to/Author_Short_Title_Reading_Note.md \
  --reception path/to/Author_Short_Title_Scholarly_Reception_and_Applications.md \
  --case-lab path/to/Author_Short_Title_Theory_to_Case_Lab.md
```

Treat the validator as a completeness check, not a substitute for scholarly judgment.
