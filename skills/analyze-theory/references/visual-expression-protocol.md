# Analytical Visual and Emphasis Protocol

## Purpose

Use visual structure to reduce interpretive load, not to decorate the note. Prefer prose for a single claim and a table for exact repeated fields. Use Mermaid only when at least three labeled relationships, a branch, a sequence, or multiple analytical levels must be seen together.

## Required visual preface

Immediately before every diagram, add a callout in the output language:

```markdown
> [!info] Purpose of this visual
> This visual shows **[relationship]** because prose alone obscures **[structure]**. Nodes represent **[meaning]** and arrows represent **[meaning]**. Evidence class: `[P]`, `[S]`, or `[A]`. It should not be interpreted as **[inferential limit]**.
```

Chinese output uses:

```markdown
> [!info] 图示用途
> 这张图用于展示**[关系]**，因为单靠文字不易看清**[结构]**。节点表示**[含义]**，箭头表示**[含义]**。证据类别：`[P]`、`[S]` 或 `[A]`。它不表示**[推论边界]**。
```

After the diagram, add `**Interpretation:**` or `**图后说明：**` and explain the main relationship in prose. The visual never replaces the argument.

## Choose the smallest useful form

| Analytical task | Preferred form |
|---|---|
| Concept hierarchy or dependency | Mermaid concept map |
| Assumption–mechanism–outcome sequence | Mermaid flowchart |
| Claim and supporting material | Argument–evidence graph |
| Genealogy, response, or revision | Mermaid timeline |
| Three or more scholarly positions | Debate map |
| Exact cross-source comparison | Markdown table |
| Theory-to-case pathway | Flowchart or layered diagram |
| Individual, organizational, institutional, or discursive levels | Layered diagram |

Default maxima are two diagrams in the reading note, two in the reception note, and three in the Case Lab. Exceed them only when the user asks for additional visual analysis.

## Evidence discipline

- Never draw a relationship as the theorist's own model unless the source supports it.
- Mark analyst-reconstructed nodes or links `[A]` in the callout and, where ambiguity remains, in the node label.
- Use solid arrows only for supported directional or sequential relations. Use dotted arrows for association, analogy, uncertainty, or a relation awaiting verification, and define that encoding.
- Link positions in a reception map to verified representative sources in the accompanying prose or table.
- Make case nodes traceable to the evidence matrix or a precise locator.
- Retain an explicitly labeled unresolved relation rather than completing a graph speculatively.

## Semantic emphasis

Before the first use of semantic emphasis, include a short `Reading guide` or `阅读提示`:

- `**bold**`: core concept, central proposition, mechanism, or conclusion;
- `<mark>highlight</mark>`: finding directly useful to the user's research or writing;
- `<u>underline</u>`: boundary condition, negation, or recurrent misreading;
- `*italics*`: original-language term, title, or term whose wording matters;
- block quotation: verified source wording with a locator;
- `[P]`, `[S]`, `[A]`: evidence provenance, never replaced by styling.

Do not emphasize whole paragraphs. As a default, use no more than two emphasized spans per paragraph. Underlining must not be used as generic emphasis because readers may mistake it for a link.

## Interactive visuals

Do not create HTML or an interactive artifact by default. Use one only when the user explicitly asks to explore adjustable conditions, competing pathways, or scenarios. Keep the Markdown note as the durable scholarly record.
