#!/usr/bin/env python3
"""Validate the Codex expert-learning documentation path."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "expert-learning"
IMAGE_ROOT = ROOT / "image" / "expert-learning"
CHANGE = ROOT / "openspec" / "changes" / "build-codex-expert-learning-docs"

COURSES = {
    "01-global-model.md": "global-request-lifecycle-v1.png",
    "02-core-runtime-loop.md": "core-runtime-loop-v1.png",
    "03-tools-safety-patch.md": "tool-safety-decision-v1.png",
    "04-state-protocol-memory.md": "state-resume-memory-v1.png",
    "05-extension-system.md": "extension-capability-lifecycle-v1.png",
}

REQUIRED_DOCS = [
    "README.md",
    *COURSES.keys(),
    "exercises.md",
    "expert-checklist.md",
]

REQUIRED_COURSE_SECTIONS = [
    "## 读完你应掌握什么",
    "## 这个模块解决什么问题",
    "## 源码锚点",
    "## 核心抽象",
    "## 核心代码片段",
    "## 主流程",
    "## 失败模式与边界条件",
    "## 行为证据矩阵",
    "## 图示",
    "## 复设计练习",
    "## 检查题",
    "## Follow-up Slots",
]

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
SOURCE_REF_RE = re.compile(r"`(repo/codex/[^`]+)`")
RUST_BLOCK_RE = re.compile(r"```rust\n(.*?)```", re.DOTALL)
SOURCE_LINE_RE = re.compile(r"^(?:\*\*)?Source:(?:\*\*)?\s+`[^`]+`", re.MULTILINE)
LINE_RANGE_RE = re.compile(
    r"^(?:\*\*)?Line range:(?:\*\*)?\s+`?[^`\n]*L?\d+\s*[-:]\s*L?\d+[^`\n]*`?",
    re.MULTILINE,
)
ENTITY_DEFINITION_RE = re.compile(
    r"^\s*(?:pub(?:\([^)]*\))?\s+)?(?:struct|enum|trait)\b",
    re.MULTILINE,
)
FENCE_RE = re.compile(r"^```", re.MULTILINE)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def source_path_from_ref(ref: str) -> Path:
    return ROOT / ref.split("::", 1)[0].split(":", 1)[0]


def check_markdown(path: Path, text: str) -> None:
    if len(FENCE_RE.findall(text)) % 2:
        fail(f"{path.relative_to(ROOT)} has an unclosed fenced code block")
    for marker in ["TODO:", "TBD", "待补", "未来文档", "\\n"]:
        if marker in text:
            fail(f"{path.relative_to(ROOT)} contains stale or generated marker: {marker}")


def check_source_refs(path: Path, text: str, min_refs: int) -> None:
    refs = SOURCE_REF_RE.findall(text)
    if len(refs) < min_refs:
        fail(f"{path.relative_to(ROOT)} expected at least {min_refs} source refs, found {len(refs)}")
    for ref in refs:
        source_path = source_path_from_ref(ref)
        if not source_path.exists():
            fail(f"{path.relative_to(ROOT)} references missing source anchor: {ref}")


def check_course(path: Path, text: str, expected_image: str) -> None:
    for section in REQUIRED_COURSE_SECTIONS:
        if section not in text:
            fail(f"{path.relative_to(ROOT)} missing section: {section}")

    image_refs = IMAGE_RE.findall(text)
    expected_ref = f"../../image/expert-learning/{expected_image}"
    if expected_ref not in image_refs:
        fail(f"{path.relative_to(ROOT)} does not reference {expected_ref}")
    image_path = IMAGE_ROOT / expected_image
    if not image_path.exists():
        fail(f"missing image: {image_path.relative_to(ROOT)}")
    svg_path = image_path.with_suffix(".svg")
    if not svg_path.exists():
        fail(f"missing editable SVG source: {svg_path.relative_to(ROOT)}")
    ET.parse(svg_path)

    rust_blocks = RUST_BLOCK_RE.findall(text)
    if len(rust_blocks) < 3:
        fail(f"{path.relative_to(ROOT)} expected at least 3 Rust snippets")
    if len(SOURCE_LINE_RE.findall(text)) < 3:
        fail(f"{path.relative_to(ROOT)} expected at least 3 Source lines")
    if len(LINE_RANGE_RE.findall(text)) < 3:
        fail(f"{path.relative_to(ROOT)} expected at least 3 Line range lines")
    if not any(ENTITY_DEFINITION_RE.search(block) for block in rust_blocks):
        fail(f"{path.relative_to(ROOT)} expected at least one entity definition snippet")
    if "### 答案要点" not in text:
        fail(f"{path.relative_to(ROOT)} missing check-question answer guidance")
    matrix = text.split("## 行为证据矩阵", 1)[1].split("## ", 1)[0]
    if "Behavior rule" not in matrix or "Test anchor" not in matrix:
        fail(f"{path.relative_to(ROOT)} behavior matrix missing expected headers")
    if not any(marker in matrix for marker in ["source-only", "test-gap", "_tests.rs"]):
        fail(f"{path.relative_to(ROOT)} behavior matrix must cite tests or source-only/test-gap")


def main() -> None:
    index_text = read(DOCS / "README.md")
    root_index = read(ROOT / "docs" / "index.md")
    readme = read(ROOT / "README.md")
    roadmap = read(ROOT / "docs" / "codex-harness-learning-roadmap.md")

    for doc_name in REQUIRED_DOCS:
        path = DOCS / doc_name
        text = read(path)
        check_markdown(path, text)
        if doc_name in COURSES:
            check_source_refs(path, text, 5)
            check_course(path, text, COURSES[doc_name])
        if doc_name != "README.md" and doc_name not in index_text:
            fail(f"docs/expert-learning/README.md does not link {doc_name}")

    if "expert-learning/README.md" not in root_index:
        fail("docs/index.md does not link expert-learning/README.md")
    if "docs/expert-learning/README.md" not in readme:
        fail("README.md does not mention docs/expert-learning/README.md")
    for doc_name in COURSES:
        if f"expert-learning/{doc_name}" not in roadmap:
            fail(f"roadmap does not mention expert-learning/{doc_name}")

    for required in ["proposal.md", "design.md", "tasks.md", "specs/codex-expert-learning-docs/spec.md"]:
        if not (CHANGE / required).exists():
            fail(f"missing OpenSpec artifact: {CHANGE.relative_to(ROOT)}/{required}")

    print("expert learning docs ok")


if __name__ == "__main__":
    main()
