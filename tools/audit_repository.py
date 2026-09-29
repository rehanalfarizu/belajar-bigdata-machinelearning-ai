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
GENERATED_PATTERNS = (
    ".DS_Store",
    "*.pyc",
    "__pycache__",
    "*.egg-info",
    "model_*.pkl",
    "model_*.joblib",
)
LEARNING_PHASES = (
    "01_FOUNDATION",
    "02_DATA_AND_MACHINE_LEARNING",
    "03_AI_AND_DATA_SYSTEMS",
    "04_DIGITAL_TWIN_ENGINEERING",
    "05_PROFESSIONAL_AND_RESEARCH",
)
REQUIRED_ROOT_PATHS = (
    "README.md",
    "START_HERE.md",
    "ROADMAP_6_BULAN.md",
    "PROGRESS_TRACKER.md",
    "HOW_TO_USE_THIS_REPO.md",
    *LEARNING_PHASES,
    "06_PROJECTS",
    "07_PROBLEM_SOLVING",
    "08_WORKPLACE_SIMULATION",
    "learning_journal",
    "tools",
    ".ai_context",
)
REQUIRED_LAB_SECTIONS = (
    "## 1. TUJUAN",
    "## 2. PREREQUISITE",
    "## 3. SETUP",
    "## 4. PREDICTION BEFORE RUN",
    "## 5. LANGKAH PRAKTIKUM",
    "## 6. OBSERVATION",
    "## 7. WHY",
    "## 8. MODIFICATION",
    "## 9. FAILURE EXPERIMENT",
    "## 10. DEBUGGING",
    "## 11. WORKPLACE CONNECTION",
    "## 12. CHECKPOINT",
)
PHASE_ONE_LAB_COUNTS = {
    "01_computer_fundamentals": 6,
    "02_python_fundamental": 10,
    "03_python_professional": 13,
    "04_math_statistics": 11,
}
PHASE_TWO_LAB_COUNTS = {
    "01_data_analysis_sql": 3,
    "02_data_mining": 2,
    "03_ml_fundamental": 3,
    "04_ml_advanced": 2,
    "05_time_series": 2,
    "06_deep_learning": 2,
}


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
            if not any(part in {".git", ".venv", "venv"} for part in path.parts):
                issues.append(f"generated artifact: {path.relative_to(ROOT)}")
    return issues


def lab_contract_issues() -> list[str]:
    issues: list[str] = []
    phase_contracts = (
        ("01_FOUNDATION", PHASE_ONE_LAB_COUNTS),
        ("02_DATA_AND_MACHINE_LEARNING", PHASE_TWO_LAB_COUNTS),
    )
    for phase_name, chapter_counts in phase_contracts:
        phase = ROOT / phase_name
        for chapter_name, expected_count in chapter_counts.items():
            lab_dir = phase / chapter_name / "04_LABS"
            guides = sorted(lab_dir.glob("[0-9][0-9]_*.md"))
            if len(guides) != expected_count:
                issues.append(
                    f"{chapter_name}: expected {expected_count} lab guides, "
                    f"found {len(guides)}"
                )
            for guide in guides:
                content = guide.read_text(encoding="utf-8")
                positions = [content.find(section) for section in REQUIRED_LAB_SECTIONS]
                missing = [
                    section
                    for section, position in zip(REQUIRED_LAB_SECTIONS, positions)
                    if position == -1
                ]
                if missing:
                    issues.append(
                        f"{guide.relative_to(ROOT)} missing: {', '.join(missing)}"
                    )
                elif positions != sorted(positions):
                    issues.append(
                        f"{guide.relative_to(ROOT)} has lab sections out of order"
                    )
    return issues


def phase_two_contract_issues() -> list[str]:
    issues: list[str] = []
    phase = ROOT / "02_DATA_AND_MACHINE_LEARNING"
    required_chapter_dirs = (
        "01_TEORI",
        "04_LABS",
        "05_EXERCISES",
        "06_PROBLEM_SOLVING",
        "07_DEBUGGING",
        "08_PROJECT",
        "09_CHECKPOINT",
    )
    for chapter_name in PHASE_TWO_LAB_COUNTS:
        chapter = phase / chapter_name
        for directory in required_chapter_dirs:
            if not (chapter / directory).is_dir():
                issues.append(f"{chapter_name}: missing {directory}")
        lesson_count = len(list((chapter / "01_TEORI").glob("[0-9][0-9]_*.md")))
        if lesson_count < 4:
            issues.append(f"{chapter_name}: only {lesson_count} sequential lessons")

    month_two = ROOT / "06_PROJECTS/month_02_data_ml_system/README.md"
    if month_two.exists():
        milestones = len(re.findall(r"^## M\d+ ", month_two.read_text(encoding="utf-8"), re.M))
        if milestones != 10:
            issues.append(f"Month 2 project: expected 10 milestones, found {milestones}")

    for relative in (
        "07_PROBLEM_SOLVING/data/problems.md",
        "07_PROBLEM_SOLVING/machine_learning/problems.md",
    ):
        content = (ROOT / relative).read_text(encoding="utf-8")
        for level in range(1, 6):
            if f"## Level {level}" not in content:
                issues.append(f"{relative}: missing Level {level}")
    return issues


def structure_issues() -> list[str]:
    issues: list[str] = []
    if (ROOT / "materi").exists():
        issues.append("legacy learning directory still exists: materi/")
    for relative in REQUIRED_ROOT_PATHS:
        if not (ROOT / relative).exists():
            issues.append(f"required path missing: {relative}")
    root_readme = ROOT / "README.md"
    if root_readme.exists() and "buka [START_HERE.md]" not in root_readme.read_text(
        encoding="utf-8"
    ):
        issues.append("root README does not explicitly direct beginners to START_HERE")
    for phase_name in LEARNING_PHASES:
        phase = ROOT / phase_name
        if not phase.is_dir():
            continue
        if not (phase / "README.md").is_file():
            issues.append(f"phase README missing: {phase_name}/README.md")
        for chapter in sorted(phase.glob("[0-9][0-9]_*")):
            if not chapter.is_dir():
                continue
            chapter_readme = chapter / "README.md"
            if not chapter_readme.is_file():
                issues.append(
                    f"chapter README missing: {chapter.relative_to(ROOT)}/README.md"
                )
            elif "Mulai dari sini" not in chapter_readme.read_text(encoding="utf-8"):
                issues.append(
                    f"chapter entrypoint missing 'Mulai dari sini': "
                    f"{chapter_readme.relative_to(ROOT)}"
                )
    for path in ROOT.rglob("*"):
        if path.is_dir() and ".git" not in path.parts:
            try:
                next(path.iterdir())
            except StopIteration:
                issues.append(f"empty directory: {path.relative_to(ROOT)}")
    return issues


def main() -> int:
    issue_groups = {
        "structure": structure_issues(),
        "markdown": markdown_issues(),
        "notebook": notebook_issues(),
        "python": python_issues(),
        "lab contract": lab_contract_issues(),
        "phase 2 contract": phase_two_contract_issues(),
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
