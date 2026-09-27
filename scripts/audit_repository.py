"""Audit lokal yang cepat: links, notebook JSON/syntax, Python syntax, artifacts.

External URLs tidak dicek karena hasilnya bergantung jaringan/rate limit. Klaim
standard tetap harus ditinjau manual terhadap sumber authoritative.
"""

from __future__ import annotations

import ast
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
PYTHON_FENCE_PATTERN = re.compile(r"```(?:python|py)\s*\n(.*?)```", re.I | re.S)
GENERATED_PATTERNS = (".DS_Store", "model_*.pkl", "model_*.joblib")


def markdown_issues() -> list[str]:
    issues: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            issues.append(f"empty Markdown: {path.relative_to(ROOT)}")
        for raw_target in LINK_PATTERN.findall(content):
            target = raw_target.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = target.split("#", 1)[0]
            if local and not (path.parent / local).resolve().exists():
                issues.append(
                    f"broken link: {path.relative_to(ROOT)} -> {target}"
                )
        for index, source in enumerate(PYTHON_FENCE_PATTERN.findall(content), 1):
            source = "\n".join(
                line
                for line in source.splitlines()
                if not line.lstrip().startswith(("%", "!"))
            )
            try:
                ast.parse(source)
            except SyntaxError as error:
                issues.append(
                    f"Markdown Python syntax: {path.relative_to(ROOT)} "
                    f"fence {index}: {error.msg} line {error.lineno}"
                )
    return issues


def notebook_issues() -> list[str]:
    issues: list[str] = []
    for path in sorted(ROOT.rglob("*.ipynb")):
        if ".git" in path.parts:
            continue
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            issues.append(f"invalid notebook JSON: {path.relative_to(ROOT)}: {error}")
            continue
        if notebook.get("nbformat") != 4:
            issues.append(f"unsupported nbformat: {path.relative_to(ROOT)}")
        for index, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            source = "\n".join(
                line
                for line in source.splitlines()
                if not line.lstrip().startswith(("%", "!"))
            )
            try:
                ast.parse(source)
            except SyntaxError as error:
                issues.append(
                    f"notebook syntax: {path.relative_to(ROOT)} cell {index}: "
                    f"{error.msg} line {error.lineno}"
                )
    return issues


def python_issues() -> list[str]:
    issues: list[str] = []
    for path in sorted(ROOT.rglob("*.py")):
        if any(part in {".git", ".venv", "venv"} for part in path.parts):
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as error:
            issues.append(
                f"Python syntax: {path.relative_to(ROOT)}: "
                f"{error.msg} line {error.lineno}"
            )
    return issues


def generated_artifact_issues() -> list[str]:
    issues: list[str] = []
    for pattern in GENERATED_PATTERNS:
        for path in ROOT.rglob(pattern):
            if ".git" not in path.parts:
                issues.append(f"generated artifact: {path.relative_to(ROOT)}")
    return issues


def main() -> int:
    issue_groups = {
        "markdown": markdown_issues(),
        "notebook": notebook_issues(),
        "python": python_issues(),
        "artifact": generated_artifact_issues(),
    }
    total = sum(len(issues) for issues in issue_groups.values())
    for name, issues in issue_groups.items():
        print(f"{name}: {'OK' if not issues else f'{len(issues)} issue(s)'}")
        for issue in issues:
            print(f"  - {issue}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
