#!/usr/bin/env python3
"""Deterministic structural and OOXML QA for growth-equity deliverables."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
S = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
NS_W = {"w": W}
NS_S = {"s": S}

REQUIRED = {
    "source_register": (".xlsx", 2500, 1, None),
    "customer_arr": (".xlsx", 5000, 4, None),
    "minority_model": (".xlsx", 5000, 6, None),
    "ic_evidence": (".docx", 5000, None, 500),
    "public_data_brief": (".docx", 5000, None, 500),
    "public_data_workbook": (".xlsx", 5000, 4, None),
    "value_creation_hiring": (".docx", 5000, None, 500),
    "management_triangulation": (".docx", 5000, None, 400),
    "legal_diligence": (".docx", 5000, None, 400),
    "ic_synthesis": (".docx", 4000, None, 200),
}


def add(report, level, code, message, path=None):
    item = {"level": level, "code": code, "message": message}
    if path is not None:
        item["path"] = str(path)
    report[level + "s"].append(item)


def rgb_value(node, attr="rgb"):
    if node is None:
        return None
    value = node.get(attr) or node.get(f"{{{W}}}{attr}") or node.get(f"{{{S}}}{attr}")
    if not value or value.lower() in {"auto", "none"}:
        return None
    value = value[-6:]
    return value.upper() if re.fullmatch(r"[0-9A-Fa-f]{6}", value) else None


def is_dark(rgb):
    if not rgb:
        return False
    r, g, b = (int(rgb[i : i + 2], 16) / 255 for i in (0, 2, 4))
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return luminance < 0.38


def inspect_docx(path, role, report, minimum_words):
    try:
        with zipfile.ZipFile(path) as zf:
            names = set(zf.namelist())
            if "word/document.xml" not in names or "word/styles.xml" not in names:
                add(report, "error", "DOCX_STRUCTURE", "Missing Word document or styles XML.", path)
                return
            document = ET.fromstring(zf.read("word/document.xml"))
            styles = ET.fromstring(zf.read("word/styles.xml"))
    except (zipfile.BadZipFile, ET.ParseError) as exc:
        add(report, "error", "DOCX_INVALID", f"Unreadable DOCX: {exc}", path)
        return

    texts = [t.text or "" for t in document.findall(".//w:t", NS_W)]
    word_count = len(re.findall(r"\b[\w'’.-]+\b", " ".join(texts)))
    if minimum_words and word_count < minimum_words:
        add(report, "error", "DOCX_TOO_SHALLOW", f"{role} has {word_count} words; minimum is {minimum_words}.", path)

    defaults = styles.find(".//w:docDefaults/w:rPrDefault/w:rPr", NS_W)
    default_fonts = defaults.find("w:rFonts", NS_W) if defaults is not None else None
    default_size = defaults.find("w:sz", NS_W) if defaults is not None else None
    font_values = []
    if default_fonts is not None:
        for key in ("ascii", "hAnsi", "eastAsia", "cs"):
            value = default_fonts.get(f"{{{W}}}{key}")
            if value:
                font_values.append(value)
    if not font_values or any(v.lower() != "times new roman" for v in font_values):
        add(report, "error", "DOCX_DEFAULT_FONT", "Word defaults must explicitly use Times New Roman.", path)
    if default_size is None or default_size.get(f"{{{W}}}val") != "24":
        add(report, "error", "DOCX_DEFAULT_SIZE", "Word default size must be 12 point (OOXML value 24).", path)

    for font in list(styles.findall(".//w:rFonts", NS_W)) + list(document.findall(".//w:rFonts", NS_W)):
        for key in ("ascii", "hAnsi", "eastAsia", "cs"):
            value = font.get(f"{{{W}}}{key}")
            if value and value.lower() != "times new roman":
                add(report, "error", "DOCX_FONT_OVERRIDE", f"Found non-Times New Roman font: {value}.", path)
                break
    for size in list(styles.findall(".//w:sz", NS_W)) + list(styles.findall(".//w:szCs", NS_W)) + list(document.findall(".//w:sz", NS_W)) + list(document.findall(".//w:szCs", NS_W)):
        value = size.get(f"{{{W}}}val")
        if value and value != "24":
            add(report, "error", "DOCX_SIZE_OVERRIDE", f"Found non-12-point Word size value: {value}.", path)
            break

    for cell in document.findall(".//w:tc", NS_W):
        shading = cell.find("w:tcPr/w:shd", NS_W)
        fill = shading.get(f"{{{W}}}fill") if shading is not None else None
        if fill and is_dark(fill[-6:]):
            colors = [rgb_value(c) for c in cell.findall(".//w:color", NS_W)]
            colors = [c for c in colors if c]
            if not colors or any(is_dark(c) for c in colors):
                add(report, "error", "DOCX_LOW_CONTRAST", f"Dark table fill {fill} has missing or dark text color.", path)
                break


def xlsx_colors(styles):
    fonts = []
    for font in styles.findall("s:fonts/s:font", NS_S):
        fonts.append(rgb_value(font.find("s:color", NS_S)))
    fills = []
    for fill in styles.findall("s:fills/s:fill", NS_S):
        pattern = fill.find("s:patternFill", NS_S)
        fills.append(rgb_value(pattern.find("s:fgColor", NS_S)) if pattern is not None else None)
    xfs = []
    for xf in styles.findall("s:cellXfs/s:xf", NS_S):
        xfs.append((int(xf.get("fontId", "0")), int(xf.get("fillId", "0"))))
    return fonts, fills, xfs


def inspect_xlsx(path, role, report, minimum_sheets):
    try:
        with zipfile.ZipFile(path) as zf:
            names = set(zf.namelist())
            if "xl/workbook.xml" not in names or "xl/styles.xml" not in names:
                add(report, "error", "XLSX_STRUCTURE", "Missing workbook or styles XML.", path)
                return
            workbook = ET.fromstring(zf.read("xl/workbook.xml"))
            styles = ET.fromstring(zf.read("xl/styles.xml"))
            sheet_names = sorted(n for n in names if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n))
            if minimum_sheets and len(sheet_names) < minimum_sheets:
                add(report, "error", "XLSX_TOO_FEW_SHEETS", f"{role} has {len(sheet_names)} worksheets; minimum is {minimum_sheets}.", path)
            fonts, fills, xfs = xlsx_colors(styles)
            formula_count = 0
            for name in sheet_names:
                sheet = ET.fromstring(zf.read(name))
                formula_count += len(sheet.findall(".//s:f", NS_S))
                for cell in sheet.findall(".//s:c", NS_S):
                    style_id = int(cell.get("s", "0"))
                    if style_id >= len(xfs):
                        continue
                    font_id, fill_id = xfs[style_id]
                    font_rgb = fonts[font_id] if font_id < len(fonts) else None
                    fill_rgb = fills[fill_id] if fill_id < len(fills) else None
                    if is_dark(fill_rgb) and (font_rgb is None or is_dark(font_rgb)):
                        ref = cell.get("r", "unknown")
                        add(report, "error", "XLSX_LOW_CONTRAST", f"Dark fill with missing or dark font at {name}!{ref}.", path)
                        return
            if role in {"customer_arr", "minority_model", "public_data_workbook"} and formula_count == 0:
                add(report, "error", "XLSX_NO_FORMULAS", f"{role} contains no formulas and is not auditable as an analytical workbook.", path)
    except (zipfile.BadZipFile, ET.ParseError, ValueError) as exc:
        add(report, "error", "XLSX_INVALID", f"Unreadable XLSX: {exc}", path)


def validate(folder):
    report = {
        "validator": "growth-equity-deal-room/1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "folder": str(folder.resolve()),
        "errors": [],
        "warnings": [],
        "files": [],
    }
    manifest_path = folder / "deliverable_manifest.json"
    if not manifest_path.exists():
        add(report, "error", "MANIFEST_MISSING", "deliverable_manifest.json is required.", manifest_path)
        return report
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        add(report, "error", "MANIFEST_INVALID", f"Cannot parse manifest: {exc}", manifest_path)
        return report
    roles = manifest.get("roles")
    if not isinstance(roles, dict):
        add(report, "error", "ROLES_MISSING", "Manifest must contain a roles object.", manifest_path)
        return report

    resolved = {}
    for role, (extension, minimum_bytes, minimum_sheets, minimum_words) in REQUIRED.items():
        entry = roles.get(role)
        if not isinstance(entry, dict):
            add(report, "error", "ROLE_MISSING", f"Missing manifest role: {role}.", manifest_path)
            continue
        status = entry.get("status")
        if status not in {"complete", "scoped", "not_applicable"}:
            add(report, "error", "STATUS_INVALID", f"{role} has invalid final status: {status!r}.", manifest_path)
        if status == "not_applicable":
            if not entry.get("reason"):
                add(report, "error", "NA_REASON_MISSING", f"{role} is not_applicable without a reason.", manifest_path)
            else:
                add(report, "warning", "ROLE_NOT_APPLICABLE", f"{role}: {entry.get('reason')}", manifest_path)
        relative = entry.get("path")
        if not isinstance(relative, str) or not relative.strip():
            add(report, "error", "PATH_MISSING", f"{role} has no output path.", manifest_path)
            continue
        candidate = (folder / relative).resolve()
        try:
            candidate.relative_to(folder.resolve())
        except ValueError:
            add(report, "error", "PATH_ESCAPE", f"{role} points outside the output folder.", candidate)
            continue
        key = str(candidate).lower()
        if key in resolved:
            add(report, "error", "CONSOLIDATED_ROLE", f"{role} and {resolved[key]} point to the same file.", candidate)
            continue
        resolved[key] = role
        if candidate.suffix.lower() != extension:
            add(report, "error", "EXTENSION_WRONG", f"{role} must be {extension}, not {candidate.suffix}.", candidate)
            continue
        if not candidate.is_file():
            add(report, "error", "FILE_MISSING", f"Required file for {role} does not exist.", candidate)
            continue
        size = candidate.stat().st_size
        report["files"].append({"role": role, "path": str(candidate), "bytes": size, "status": status})
        if size < minimum_bytes:
            add(report, "error", "FILE_TOO_SMALL", f"{role} is only {size} bytes; likely empty or superficial.", candidate)
            continue
        if extension == ".docx":
            inspect_docx(candidate, role, report, minimum_words)
        else:
            inspect_xlsx(candidate, role, report, minimum_sheets)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Deal output folder containing deliverable_manifest.json")
    args = parser.parse_args()
    folder = args.folder.resolve()
    if not folder.is_dir():
        print(json.dumps({"errors": [{"code": "FOLDER_MISSING", "message": str(folder)}]}, indent=2))
        return 2
    report = validate(folder)
    report["passed"] = not report["errors"]
    destination = folder / "validation_report.json"
    destination.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"passed": report["passed"], "errors": len(report["errors"]), "warnings": len(report["warnings"]), "report": str(destination)}, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
