#!/usr/bin/env python3
"""Validate legacy, paired, or three-file Theory-to-Case Lab Markdown notes."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


LEGACY_SECTION_GROUPS = {
    "scope": ("corpus", "语料", "资料范围", "method", "方法"),
    "theory_core": ("theory at a glance", "理论概览", "核心观点", "主要观点"),
    "concepts": ("concept", "概念"),
    "logic": ("argument", "logical architecture", "逻辑", "论证"),
    "cases": ("case", "example", "案例", "例证"),
    "evaluation": ("strength", "limitation", "优点", "局限", "批评"),
    "landscape": ("research landscape", "研究现状", "研究图景", "学术应用"),
    "controversy": ("controvers", "debate", "争议", "分歧"),
    "application": ("user's paper", "paper application", "论文应用", "理论框架"),
    "references": ("references", "bibliography", "参考文献"),
}

READING_SECTION_GROUPS = {
    "basic_info": ("基本信息", "basic information"),
    "summary": ("一句话概括", "one-sentence summary"),
    "question": ("核心问题", "central question"),
    "claims": ("核心论点", "core arguments"),
    "concepts": ("关键概念", "key concepts"),
    "method": ("方法 / 材料", "方法/材料", "method / materials", "method/materials"),
    "case_explanation": ("理论如何解释案例", "how the theory explains cases"),
    "source_cases": ("原著案例在论证中的作用", "the role of cases in the source's argument"),
    "user_case": ("用理论解释我的案例", "applying the theory to my case"),
    "usefulness": ("对我有用的部分", "how this helps my research"),
    "paper": ("可以放进哪篇论文", "projects or papers where it fits"),
    "citation_use": ("我可能如何引用它", "how i might cite or use it"),
    "evaluation": ("我的评价", "my assessment"),
    "excerpts": ("摘录 / 页码", "摘录/页码", "quotations / page numbers", "quotations/page numbers"),
    "links": ("相关链接", "related links"),
}

RECEPTION_SECTION_GROUPS = {
    "basic_info": ("基本信息", "basic information"),
    "summary": ("一句话概括", "one-sentence summary"),
    "positioning": ("学界如何定位这篇文献", "how scholarship positions this work"),
    "agreement": ("相对稳定的共识", "relatively stable points of agreement"),
    "evaluation": ("主要解释与评价", "major interpretations and evaluations"),
    "controversy": ("主要争议、回应与修正", "major debates, responses, and revisions"),
    "applications": ("理论应用", "theoretical applications"),
    "extensions": ("概念的继承、修改与扩展", "conceptual inheritance, modification, and extension"),
    "operationalization": ("操作化与方法实践", "operationalization and methodological practice"),
    "usefulness": ("对我有用的部分", "how this helps my research"),
    "paper": ("可以放进哪篇论文", "projects or papers where it fits"),
    "citation_use": ("我可能如何引用学界讨论", "how i might cite the scholarly discussion"),
    "assessment": ("我的综合评价", "my overall assessment"),
    "excerpts": ("摘录 / 页码", "摘录/页码", "quotations / page numbers", "quotations/page numbers"),
    "links": ("相关链接", "related links"),
    "references": ("已核实参考文献", "verified references"),
    "leads": ("待核线索", "leads requiring verification"),
}

CASE_LAB_SECTION_GROUPS = {
    "basic_info": ("基本信息", "basic information"),
    "explanandum": ("案例与待解释对象", "case and explanandum"),
    "fit": ("理论—案例匹配度", "理论-案例匹配度", "theory–case fit", "theory-case fit"),
    "path": ("选定的解释路径", "selected explanatory or interpretive path"),
    "positions": ("概念、位置、资源与约束", "concepts, positions, resources, and constraints"),
    "steps": ("逐步解释", "step-by-step explanation"),
    "visual": ("理论—案例解释图", "理论-案例解释图", "theory-to-case visual"),
    "rivals": ("对手解释或替代阅读", "rival explanations or alternative readings"),
    "counterfactual": ("反事实、负案例或替代阅读", "counterfactual, negative case, or alternative reading"),
    "evidence": ("证据计划", "evidence plan"),
    "boundaries": ("适用范围与边界", "scope and boundaries"),
    "paper_ready": ("可直接写入论文的分析段", "paper-ready analytical paragraph"),
    "links": ("相关链接", "related links"),
}

SECTION_GROUPS = {
    "legacy": LEGACY_SECTION_GROUPS,
    "reading": READING_SECTION_GROUPS,
    "reception": RECEPTION_SECTION_GROUPS,
    "case-lab": CASE_LAB_SECTION_GROUPS,
}

PLACEHOLDER_PATTERNS = (
    r"\[Theory Name\]",
    r"\[date(?: or not applicable)?\]",
    r"\[sources, editions, languages, date range\]",
    r"\[Include verified sources only\.\]",
    r"\[verify\]",
    r"\{\{[^{}]+\}\}",
)
NONLEGACY_PLACEHOLDERS = (r"\[\[\s*\]\]",)
METADATA_KEYS = ("Author", "Year", "Title", "Type")
VISUAL_LIMITS = {"reading": 2, "reception": 2, "case-lab": 3}


def headings(markdown: str) -> list[str]:
    return [m.group(1).strip().lower() for m in re.finditer(r"^#{1,6}\s+(.+)$", markdown, re.M)]


def extract_metadata(markdown: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for key in METADATA_KEYS:
        match = re.search(rf"^-\s*{re.escape(key)}:\s*(.+?)\s*$", markdown, re.M | re.I)
        if match:
            metadata[key] = re.sub(r"\s+", " ", match.group(1).strip())
    return metadata


def extract_wikilinks(markdown: str) -> set[str]:
    links: set[str] = set()
    for raw in re.findall(r"\[\[([^\]]+)\]\]", markdown):
        target = raw.split("|", 1)[0].strip()
        if target.endswith(".md"):
            target = target[:-3]
        if target:
            links.add(Path(target).name)
    return links


def mermaid_blocks(markdown: str) -> list[re.Match[str]]:
    return list(re.finditer(r"```mermaid\s*\n(.*?)```", markdown, re.S | re.I))


def validate_visuals(markdown: str, kind: str) -> dict[str, Any]:
    blocks = mermaid_blocks(markdown)
    errors: list[str] = []
    warnings: list[str] = []

    for index, block in enumerate(blocks, start=1):
        before = markdown[max(0, block.start() - 1200):block.start()]
        after = markdown[block.end():block.end() + 700]
        recent_lines = "\n".join(before.splitlines()[-12:])
        callout_match = re.search(
            r">\s*\[!info\]\s*(?:Purpose of this visual|图示用途)", recent_lines, re.I
        )
        callout = recent_lines[callout_match.start():] if callout_match else ""

        if not callout_match:
            errors.append(f"Visual {index} has no immediately preceding purpose callout.")
        if not re.search(r"\[(?:P|S|A)\]", callout):
            errors.append(f"Visual {index} purpose callout has no evidence-class label.")
        if not re.search(
            r"(?:should not be interpreted|does not (?:show|mean|establish|prove)|cannot (?:show|mean|establish|prove)|不表示|不能证明|不等于)",
            callout,
            re.I,
        ):
            errors.append(f"Visual {index} purpose callout has no inferential limit.")
        if not re.search(r"\*\*(?:Interpretation|图后说明)[：:]\*\*", after, re.I):
            errors.append(f"Visual {index} has no prose interpretation immediately afterward.")

        body = block.group(1)
        edge_count = len(re.findall(r"(?:-->|---|-.->|==>)", body))
        node_count = len(set(re.findall(r"\b([A-Za-z][A-Za-z0-9_]*)\s*(?=\[|\()", body)))
        if edge_count < 2 or node_count < 3:
            warnings.append(f"Visual {index} may not meet the three-relationship threshold.")

    limit = VISUAL_LIMITS.get(kind)
    if limit is not None and len(blocks) > limit:
        warnings.append(f"Contains {len(blocks)} diagrams; default limit for {kind} is {limit}.")

    uses_semantic_emphasis = bool(re.search(r"<mark>|<u>|\*\*[^*]+\*\*", markdown, re.I))
    has_reading_guide = bool(re.search(r"\[!tip\]\s*(?:Reading guide|阅读提示)", markdown, re.I))
    if uses_semantic_emphasis and kind != "legacy" and not has_reading_guide:
        errors.append("Semantic emphasis is used without a Reading guide / 阅读提示 callout.")

    for line_number, line in enumerate(markdown.splitlines(), start=1):
        if len(line) > 180 and re.fullmatch(r"\s*(?:<mark>.*</mark>|<u>.*</u>|\*\*.*\*\*)\s*", line):
            warnings.append(f"Line {line_number} appears to emphasize a full paragraph.")

    return {
        "diagram_count": len(blocks),
        "errors": errors,
        "warnings": warnings,
        "has_reading_guide": has_reading_guide,
    }


def validate(path: Path, kind: str = "legacy") -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    found_headings = headings(text)
    expected_groups = SECTION_GROUPS[kind]
    missing = [
        name
        for name, aliases in expected_groups.items()
        if not any(alias.lower() in heading for alias in aliases for heading in found_headings)
    ]
    patterns = PLACEHOLDER_PATTERNS + (NONLEGACY_PLACEHOLDERS if kind != "legacy" else ())
    placeholders = [pattern for pattern in patterns if re.search(pattern, text, re.I)]
    labels = {label: len(re.findall(rf"\[{label}\]", text)) for label in ("P", "S", "A")}
    locator_signals = len(
        re.findall(
            r"(?:\bp{1,2}\.\s*\d+|第\s*\d+\s*页|chapter\s+\d+|第[一二三四五六七八九十百\d]+章|§\s*\d+)",
            text,
            re.I,
        )
    )
    verification_flags = len(re.findall(r"(?:\[verify\]|verification needed|待核|需核)", text, re.I))
    metadata = extract_metadata(text) if kind != "legacy" else {}
    missing_metadata = [key for key in METADATA_KEYS if not metadata.get(key)] if kind != "legacy" else []
    missing_search_date = kind == "reception" and not re.search(
        r"^-\s*(?:检索日期|search date):[ \t]*\S+", text, re.M | re.I
    )
    visual = validate_visuals(text, kind)

    case_path_error = False
    if kind == "case-lab":
        path_match = re.search(r"^-\s*(?:Selected path|选定路径):\s*(.+?)\s*$", text, re.M | re.I)
        case_path_error = not path_match or bool(re.search(r"\s/\s", path_match.group(1)))

    evidence_errors: list[str] = []
    if kind == "reading" and labels["P"] == 0:
        evidence_errors.append("Reading note has no [P] primary-text labels.")
    if kind == "reception" and labels["S"] == 0:
        evidence_errors.append("Reception note has no [S] scholarship labels.")
    if kind == "case-lab" and (labels["P"] == 0 or labels["A"] == 0):
        evidence_errors.append("Case Lab requires both [P] and [A] evidence labels.")

    warnings: list[str] = []
    if missing:
        warnings.append("Missing expected section groups: " + ", ".join(missing))
    if placeholders:
        warnings.append(f"Unresolved template placeholders: {len(placeholders)}")
    if missing_metadata:
        warnings.append("Missing bibliographic metadata: " + ", ".join(missing_metadata))
    if missing_search_date:
        warnings.append("Reception note has no completed search date.")
    if sum(labels.values()) == 0:
        warnings.append("No [P]/[S]/[A] evidence-class labels found.")
    warnings.extend(evidence_errors)
    if locator_signals == 0:
        warnings.append("No page, chapter, or section locator signals found.")
    if kind == "case-lab" and labels["S"] == 0:
        warnings.append("Case Lab has no [S] scholarship label; explain if reception research was unavailable.")
    if case_path_error:
        warnings.append("Case Lab has no single completed Selected path / 选定路径 value.")
    if kind == "legacy" and ("current" in text.lower() or "研究现状" in text):
        if not re.search(r"(?:search date|检索日期|检索时间|search current to)", text, re.I):
            warnings.append("Current-research discussion has no explicit search date.")
    warnings.extend(visual["errors"])
    warnings.extend(visual["warnings"])

    structural_failure = bool(
        missing
        or placeholders
        or missing_metadata
        or missing_search_date
        or evidence_errors
        or visual["errors"]
        or case_path_error
    )
    return {
        "file": str(path),
        "kind": kind,
        "passed_structural_check": not structural_failure,
        "heading_count": len(found_headings),
        "missing_section_groups": missing,
        "unresolved_placeholder_patterns": placeholders,
        "metadata": metadata,
        "missing_metadata": missing_metadata,
        "evidence_labels": labels,
        "locator_signals": locator_signals,
        "verification_flags": verification_flags,
        "wikilinks": sorted(extract_wikilinks(text)),
        "visual_validation": visual,
        "warnings": warnings,
    }


def validate_bundle(reading: Path, reception: Path, case_lab: Path | None = None) -> dict[str, Any]:
    files: list[tuple[str, Path]] = [("reading", reading), ("reception", reception)]
    if case_lab:
        files.append(("case-lab", case_lab))

    results = {kind: validate(path, kind) for kind, path in files}
    stems = {kind: path.stem for kind, path in files}
    link_failures: dict[str, list[str]] = {}
    for kind, _path in files:
        links = set(results[kind]["wikilinks"])
        missing_targets = [stem for other, stem in stems.items() if other != kind and stem not in links]
        if missing_targets:
            link_failures[kind] = missing_targets

    metadata_mismatches: dict[str, dict[str, str | None]] = {}
    for key in METADATA_KEYS:
        values = {kind: results[kind]["metadata"].get(key) for kind, _ in files}
        normalized = {value.casefold() for value in values.values() if value}
        if len(normalized) > 1:
            metadata_mismatches[key] = values

    warnings: list[str] = []
    if link_failures:
        warnings.append("Generated notes do not all contain reciprocal Obsidian wikilinks.")
    if metadata_mismatches:
        warnings.append("Bibliographic metadata differs across generated notes: " + ", ".join(metadata_mismatches))

    passed = bool(
        all(result["passed_structural_check"] for result in results.values())
        and not link_failures
        and not metadata_mismatches
    )
    return {
        "mode": "three-file" if case_lab else "paired",
        "passed_structural_check": passed,
        **results,
        "reciprocal_links": not link_failures,
        "link_failures": link_failures,
        "metadata_mismatches": metadata_mismatches,
        "warnings": warnings,
    }


def print_single(result: dict[str, Any]) -> None:
    status = "PASS" if result["passed_structural_check"] else "REVIEW"
    print(f"{status}: {result['file']}")
    for warning in result["warnings"]:
        print(f"- {warning}")
    print(f"- Evidence labels: {result['evidence_labels']}")
    print(f"- Locator signals: {result['locator_signals']}")
    print(f"- Verification flags: {result['verification_flags']}")
    print(f"- Diagrams: {result['visual_validation']['diagram_count']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", nargs="?", type=Path, help="Legacy single-file Markdown dossier")
    parser.add_argument("--reading", type=Path, help="Source-reading note")
    parser.add_argument("--reception", type=Path, help="Scholarly-reception note")
    parser.add_argument("--case-lab", type=Path, help="Optional Theory-to-Case Lab note")
    parser.add_argument("--json", action="store_true", help="Emit JSON only")
    args = parser.parse_args()

    if args.report and (args.reading or args.reception or args.case_lab):
        parser.error("use either a legacy report or --reading with --reception and optional --case-lab")
    if bool(args.reading) != bool(args.reception):
        parser.error("--reading and --reception must be supplied together")
    if args.case_lab and not (args.reading and args.reception):
        parser.error("--case-lab requires both --reading and --reception")
    if not args.report and not args.reading:
        parser.error("provide a legacy report or both --reading and --reception")

    paths = [path for path in (args.report, args.reading, args.reception, args.case_lab) if path]
    for path in paths:
        if not path.is_file():
            parser.error(f"not a file: {path}")

    if args.report:
        result = validate(args.report)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print_single(result)
    else:
        result = validate_bundle(args.reading, args.reception, args.case_lab)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            status = "PASS" if result["passed_structural_check"] else "REVIEW"
            print(f"{status}: {result['mode']} theory notes")
            print_single(result["reading"])
            print_single(result["reception"])
            if args.case_lab:
                print_single(result["case-lab"])
            for warning in result["warnings"]:
                print(f"- Bundle: {warning}")

    return 0 if result["passed_structural_check"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
