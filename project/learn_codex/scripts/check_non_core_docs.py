#!/usr/bin/env python3
"""Validate the non-Core Codex harness documentation set.

The generic source-study checker is still used for quality gates. This script
keeps a project-local contract for the Entry, Support, and Extension layer
overview and deep-dive documents.
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LAYER_DOCS = {
    "entry": {
        "index": ROOT / "docs" / "entry" / "README.md",
        "topics": [
            (
                ROOT / "docs" / "entry" / "00-entry-map.md",
                ROOT / "image" / "architecture" / "harness-entry-layer-v1.png",
            ),
            (
                ROOT / "docs" / "entry" / "01-cli-tui-app-server-flow.md",
                ROOT / "image" / "architecture" / "entry-cli-tui-app-server-flow-v1.png",
            ),
            (
                ROOT / "docs" / "entry" / "02-cli-command-surface.md",
                ROOT / "image" / "architecture" / "entry-cli-command-surface-v1.png",
            ),
            (
                ROOT / "docs" / "entry" / "03-tui-thread-event-routing.md",
                ROOT / "image" / "architecture" / "entry-tui-thread-event-routing-v1.png",
            ),
            (
                ROOT / "docs" / "entry" / "04-app-server-json-rpc-control-plane.md",
                ROOT / "image" / "architecture" / "entry-app-server-json-rpc-control-plane-v1.png",
            ),
        ],
    },
    "support": {
        "index": ROOT / "docs" / "support" / "README.md",
        "topics": [
            (
                ROOT / "docs" / "support" / "00-support-map.md",
                ROOT / "image" / "state-memory" / "harness-support-layer-v1.png",
            ),
            (
                ROOT / "docs" / "support" / "01-protocol-rollout-thread-store.md",
                ROOT / "image" / "state-memory" / "support-protocol-rollout-thread-store-v1.png",
            ),
        ],
    },
    "extension": {
        "index": ROOT / "docs" / "extension" / "README.md",
        "topics": [
            (
                ROOT / "docs" / "extension" / "00-extension-map.md",
                ROOT / "image" / "extension-points" / "harness-extension-layer-v1.png",
            ),
            (
                ROOT / "docs" / "extension" / "01-skills-plugins-mcp-hooks.md",
                ROOT / "image" / "extension-points" / "extension-skills-plugins-mcp-hooks-v1.png",
            ),
        ],
    },
}

REQUIRED_SECTIONS = [
    "## 读完你应掌握什么",
    "## 这个模块解决什么问题",
    "## 源码锚点",
    "## 核心抽象",
    "## 核心代码片段",
    "## 主流程",
    "## 失败模式与边界条件",
    "## 图示",
    "## 复设计练习",
    "## 检查题",
    "## Follow-up Slots",
]
DEEP_DIVE_REQUIRED_SECTIONS = [
    "## 行为证据矩阵",
]

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
SOURCE_REF_RE = re.compile(r"`(repo/codex/[^`]+)`")
FENCE_RE = re.compile(r"^```", re.MULTILINE)
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


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def source_path_from_ref(ref: str) -> Path:
    return ROOT / ref.split("::", 1)[0].split(":", 1)[0]


def check_source_refs(path: Path, text: str) -> None:
    for ref in SOURCE_REF_RE.findall(text):
        if not source_path_from_ref(ref).exists():
            fail(f"{path.relative_to(ROOT)} references missing source anchor: {ref}")


def check_markdown(path: Path, text: str) -> None:
    if len(FENCE_RE.findall(text)) % 2:
        fail(f"{path.relative_to(ROOT)} has an unclosed fenced code block")
    for marker in ["\\n", "TODO:", "TBD", "待补", "未来文档", "future document"]:
        if marker in text:
            fail(f"{path.relative_to(ROOT)} contains stale or generated marker: {marker}")


def check_topic(path: Path, text: str, expected_image: Path) -> None:
    for section in REQUIRED_SECTIONS:
        if section not in text:
            fail(f"{path.relative_to(ROOT)} missing section: {section}")

    image_refs = IMAGE_RE.findall(text)
    if not image_refs:
        fail(f"{path.relative_to(ROOT)} has no image reference")
    expected_rel = Path(os.path.relpath(expected_image, path.parent)).as_posix()
    if expected_rel not in image_refs:
        fail(f"{path.relative_to(ROOT)} does not reference {expected_rel}")
    for ref in image_refs:
        image_path = (path.parent / ref).resolve()
        if not image_path.exists():
            fail(f"{path.relative_to(ROOT)} references missing image: {ref}")
        if image_path.suffix == ".svg":
            ET.parse(image_path)
        if image_path.suffix == ".png":
            source_svg = image_path.with_suffix(".svg")
            if not source_svg.exists():
                fail(f"{path.relative_to(ROOT)} references PNG without matching SVG source: {ref}")
            ET.parse(source_svg)

    rust_blocks = RUST_BLOCK_RE.findall(text)
    if len(rust_blocks) < 3:
        fail(f"{path.relative_to(ROOT)} expected at least 3 Rust snippets")
    if len(SOURCE_LINE_RE.findall(text)) < 3:
        fail(f"{path.relative_to(ROOT)} expected at least 3 Source lines")
    if len(LINE_RANGE_RE.findall(text)) < 3:
        fail(f"{path.relative_to(ROOT)} expected at least 3 Line range lines")
    if not any(ENTITY_DEFINITION_RE.search(block) for block in rust_blocks):
        fail(f"{path.relative_to(ROOT)} expected an entity/state/protocol definition snippet")
    if "### 答案要点" not in text:
        fail(f"{path.relative_to(ROOT)} missing check-question answer guidance")


def check_deep_dive(path: Path, text: str) -> None:
    for section in DEEP_DIVE_REQUIRED_SECTIONS:
        if section not in text:
            fail(f"{path.relative_to(ROOT)} missing section: {section}")
    matrix = text.split("## 行为证据矩阵", 1)[1].split("## ", 1)[0]
    if "Behavior rule" not in matrix or "Test anchor" not in matrix:
        fail(f"{path.relative_to(ROOT)} behavior evidence matrix has no expected header")
    if not any(marker in matrix for marker in ["source-only", "test-gap", "_tests.rs", "/tests/"]):
        fail(
            f"{path.relative_to(ROOT)} behavior evidence matrix must cite tests "
            "or explicitly mark source-only/test-gap"
        )


def main() -> None:
    root_index = read(ROOT / "docs" / "index.md")
    root_readme = read(ROOT / "README.md")
    roadmap = read(ROOT / "docs" / "codex-harness-learning-roadmap.md")
    for layer, paths in LAYER_DOCS.items():
        index = paths["index"]
        index_text = read(index)
        check_markdown(index, index_text)
        check_source_refs(index, index_text)
        topics = paths["topics"]
        if len(topics) < 2:
            fail(f"{layer} must define an overview and at least one deep-dive topic")
        if layer == "entry" and len(topics) < 5:
            fail("entry must define overview, cross-entry flow, CLI, TUI, and app-server topics")
        for topic, image in topics:
            topic_text = read(topic)
            check_markdown(topic, topic_text)
            check_source_refs(topic, topic_text)
            check_topic(topic, topic_text, image)
            if not topic.name.startswith("00-"):
                check_deep_dive(topic, topic_text)
            if topic.name not in index_text:
                fail(f"{index.relative_to(ROOT)} does not link {topic.name}")
            if topic.name not in roadmap:
                fail(f"roadmap does not mention {topic.name}")
        if f"docs/{layer}/README.md" not in root_readme:
            fail(f"README.md does not list docs/{layer}/README.md")
        if f"{layer}/README.md" not in root_index:
            fail(f"docs/index.md does not link {layer}/README.md")

    print("non-core docs ok")


if __name__ == "__main__":
    main()
