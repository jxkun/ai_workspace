#!/usr/bin/env python3
"""Validate the Codex core documentation set.

This script checks the project-local documentation contract:
- all planned core Markdown files exist,
- every core topic has the required teaching sections,
- every image reference resolves to a local file,
- every core topic has at least one image before the final diagram index,
- every Markdown fenced code block is closed,
- all referenced SVG files are parseable XML.
- the core code-evidence guide contains the required source snippets.
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "core"

REQUIRED_DOCS = [
    "00-core-map.md",
    "01-thread-lifecycle.md",
    "02-session-turn-loop.md",
    "03-context-world-state.md",
    "04-tool-runtime.md",
    "05-exec-shell.md",
    "06-safety-sandbox-approval.md",
    "07-apply-patch.md",
    "08-config-env-model-client.md",
    "09-extensions-inside-core.md",
    "10-agents-and-spawn.md",
    "11-rollout-compaction-resume.md",
    "12-guardian-review-attestation.md",
    "13-realtime-apps-images.md",
    "14-observability-utilities.md",
    "15-core-code-evidence.md",
]

REQUIRED_SECTIONS = [
    "## 读完你应掌握什么",
    "## 这个模块解决什么问题",
    "## 源码锚点",
    "## 核心抽象",
    "## 主流程",
    "## 失败模式与边界条件",
    "## 图示",
    "## 复设计练习",
    "## 检查题",
    "## Follow-up Slots",
]

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
SOURCE_REF_RE = re.compile(r"`(repo/codex/[^`]+)`")
ANSWER_MARKERS = ("参考回答", "答案要点", "合理答案")
STALE_INDEX_PHRASES = ("未来文档", "下一步建议先写")
GENERATED_GARBAGE = (
    '\\n"}Ieading',
    "\\n+",
    "CODE_EDIT_COMMAND_OUTPUT",
)
CONFLICT_MARKER_RE = re.compile(r"^(<<<<<<<|=======|>>>>>>>)", re.MULTILINE)
PATCH_RESIDUE_PHRASES = ("*** Begin Patch", "*** End Patch")
PER_TOPIC_CODE_EVIDENCE_DOCS = REQUIRED_DOCS
TYPED_RUST_BLOCK_RE = re.compile(r"```rust\n(.*?)```", re.DOTALL)
SOURCE_LINE_RE = re.compile(r"^(?:\*\*)?Source:(?:\*\*)?\s+`[^`]+`", re.MULTILINE)
LINE_RANGE_RE = re.compile(
    r"^(?:\*\*)?Line range:(?:\*\*)?\s+`?[^`\n]*L?\d+\s*[-:]\s*L?\d+[^`\n]*`?",
    re.MULTILINE,
)
ENTITY_DEFINITION_RE = re.compile(
    r"^\s*(?:pub(?:\([^)]*\))?\s+)?(?:struct|enum|trait)\b",
    re.MULTILINE,
)
CODE_EVIDENCE_REQUIREMENTS = [
    (
        "外部只通过 `CodexThread` 操作会话",
        "repo/codex/codex-rs/core/src/codex_thread.rs::CodexThread",
        "repo/codex/codex-rs/core/src/codex_thread.rs:177-222",
    ),
    (
        "turn 输入只有三种路由结果",
        "repo/codex/codex-rs/protocol/src/turn_input.rs::TurnInputMode",
        "repo/codex/codex-rs/protocol/src/turn_input.rs:128-190",
    ),
    (
        "sampling 前绑定 tool runtime 和 prompt",
        "repo/codex/codex-rs/core/src/session/turn.rs::run_sampling_request",
        "repo/codex/codex-rs/core/src/session/turn.rs:1415-1460",
    ),
    (
        "WorldState section 是可持久化、可 diff 的状态合约",
        "repo/codex/codex-rs/core/src/context/world_state/mod.rs::WorldStateSection",
        "repo/codex/codex-rs/core/src/context/world_state/mod.rs:228-264",
    ),
    (
        "每个 step 的工具集合由 router 现场装配",
        "repo/codex/codex-rs/core/src/tools/spec_plan.rs::build_tool_router",
        "repo/codex/codex-rs/core/src/tools/spec_plan.rs:125-166",
    ),
    (
        "approval 和 sandbox 是所有工具共享的外壳",
        "repo/codex/codex-rs/core/src/tools/orchestrator.rs::ToolOrchestrator::run",
        "repo/codex/codex-rs/core/src/tools/orchestrator.rs:121-176",
    ),
    (
        "子 agent 创建先占位，失败自动释放",
        "repo/codex/codex-rs/core/src/agent/registry.rs::reserve_spawn_slot",
        "repo/codex/codex-rs/core/src/agent/registry.rs:96-118",
    ),
    (
        "resume/fork 先反向找 checkpoint，再正向重放",
        "repo/codex/codex-rs/core/src/session/rollout_reconstruction.rs::reconstruct_history_from_rollout",
        "repo/codex/codex-rs/core/src/session/rollout_reconstruction.rs:133-172",
    ),
]
CODE_EVIDENCE_REQUIRED_TESTS = [
    "repo/codex/codex-rs/core/src/thread_manager_tests.rs",
    "repo/codex/codex-rs/core/src/session/turn_input_tests.rs",
    "repo/codex/codex-rs/core/src/session/turn_tests.rs",
    "repo/codex/codex-rs/core/src/context/world_state/world_state_tests.rs",
    "repo/codex/codex-rs/core/src/tools/router_tests.rs",
    "repo/codex/codex-rs/core/src/tools/sandboxing_tests.rs",
    "repo/codex/codex-rs/core/src/agent/registry_tests.rs",
    "repo/codex/codex-rs/core/src/session/rollout_reconstruction_tests.rs",
]
FENCE_RE = re.compile(r"^```", re.MULTILINE)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def source_path_from_ref(ref: str) -> Path:
    path = ref.split("::", 1)[0].split(":", 1)[0]
    return (ROOT / path).resolve()


def check_source_refs(path: Path, text: str) -> None:
    for ref in SOURCE_REF_RE.findall(text):
        source_path = source_path_from_ref(ref)
        if not source_path.exists():
            fail(f"{path.relative_to(ROOT)} references missing source anchor: {ref}")


def check_answer_guidance(path: Path, text: str) -> None:
    if "## 检查题" not in text:
        fail(f"{path.relative_to(ROOT)} missing section: ## 检查题")
    after_questions = text.split("## 检查题", 1)[1]
    before_followup = after_questions.split("## Follow-up Slots", 1)[0]
    if not any(marker in before_followup for marker in ANSWER_MARKERS):
        fail(f"{path.relative_to(ROOT)} missing check-question answer guidance")


def check_nearby_diagram(path: Path, text: str) -> None:
    before_diagram_index = text.split("## 图示", 1)[0]
    if not IMAGE_RE.search(before_diagram_index):
        fail(
            f"{path.relative_to(ROOT)} needs a local diagram near the main flow "
            "or key explanatory section before ## 图示"
        )


def check_markdown_fences(path: Path, text: str) -> None:
    fence_count = len(FENCE_RE.findall(text))
    if fence_count % 2 != 0:
        fail(f"{path.relative_to(ROOT)} has an unclosed fenced code block")


def check_patch_residue(path: Path, text: str) -> None:
    if CONFLICT_MARKER_RE.search(text):
        fail(f"{path.relative_to(ROOT)} contains merge conflict marker")
    if path.name == "15-core-code-evidence.md":
        for phrase in PATCH_RESIDUE_PHRASES:
            if phrase in text:
                fail(f"{path.relative_to(ROOT)} contains patch residue: {phrase}")


def check_per_topic_code_evidence(path: Path, text: str) -> None:
    if "## 核心代码片段" not in text and "## Core Code Evidence" not in text:
        fail(f"{path.relative_to(ROOT)} missing section: ## 核心代码片段")
    rust_blocks = TYPED_RUST_BLOCK_RE.findall(text)
    if len(rust_blocks) < 3:
        fail(
            f"{path.relative_to(ROOT)} expected at least 3 Rust code evidence blocks, "
            f"found {len(rust_blocks)}"
        )
    source_lines = len(SOURCE_LINE_RE.findall(text))
    if source_lines < 3:
        fail(
            f"{path.relative_to(ROOT)} expected at least 3 code evidence Source lines, "
            f"found {source_lines}"
        )
    line_ranges = len(LINE_RANGE_RE.findall(text))
    if line_ranges < 3:
        fail(
            f"{path.relative_to(ROOT)} expected at least 3 code evidence Line range lines, "
            f"found {line_ranges}"
        )
    entity_blocks = sum(1 for block in rust_blocks if ENTITY_DEFINITION_RE.search(block))
    if entity_blocks < 1:
        fail(
            f"{path.relative_to(ROOT)} expected at least 1 entity/state/protocol "
            f"definition snippet, found {entity_blocks}"
        )


def check_aggregate_code_evidence(path: Path, text: str) -> None:
    if "核心代码片段" not in text and "Code Evidence" not in text:
        fail(f"{path.relative_to(ROOT)} missing code evidence section")
    rust_blocks = text.count("```rust")
    if rust_blocks < len(CODE_EVIDENCE_REQUIREMENTS):
        fail(
            f"{path.relative_to(ROOT)} expected at least "
            f"{len(CODE_EVIDENCE_REQUIREMENTS)} Rust code evidence blocks, found {rust_blocks}"
        )
    for heading, source, line_range in CODE_EVIDENCE_REQUIREMENTS:
        section = f"### Code Evidence: {heading}"
        if section not in text:
            fail(f"{path.relative_to(ROOT)} missing code evidence heading: {heading}")
        if f"Source: `{source}`" not in text:
            fail(f"{path.relative_to(ROOT)} missing code evidence source anchor: {source}")
        if f"Line range: `{line_range}`" not in text:
            fail(f"{path.relative_to(ROOT)} missing code evidence line range: {line_range}")
    if "## 测试证据" not in text:
        fail(f"{path.relative_to(ROOT)} missing section: ## 测试证据")
    for test_anchor in CODE_EVIDENCE_REQUIRED_TESTS:
        if f"`{test_anchor}`" not in text:
            fail(f"{path.relative_to(ROOT)} missing test evidence anchor: {test_anchor}")


def check_index() -> None:
    index = DOCS / "README.md"
    if not index.exists():
        fail(f"missing document: {index.relative_to(ROOT)}")
    text = index.read_text(encoding="utf-8")
    for phrase in STALE_INDEX_PHRASES:
        if phrase in text:
            fail(f"{index.relative_to(ROOT)} contains stale planning phrase: {phrase}")
    for name in REQUIRED_DOCS:
        if f"({name})" not in text and f"`docs/core/{name}`" not in text:
            fail(f"{index.relative_to(ROOT)} does not link or list: {name}")


def main() -> None:
    check_index()

    for name in REQUIRED_DOCS:
        path = DOCS / name
        if not path.exists():
            fail(f"missing document: {path.relative_to(ROOT)}")

        text = path.read_text(encoding="utf-8")
        for phrase in GENERATED_GARBAGE:
            if phrase in text:
                fail(f"{path.relative_to(ROOT)} contains generated garbage: {phrase}")
        check_patch_residue(path, text)
        check_markdown_fences(path, text)
        for section in REQUIRED_SECTIONS:
            if section not in text:
                fail(f"{path.relative_to(ROOT)} missing section: {section}")
        check_source_refs(path, text)
        check_answer_guidance(path, text)
        check_nearby_diagram(path, text)
        if name in PER_TOPIC_CODE_EVIDENCE_DOCS:
            check_per_topic_code_evidence(path, text)
        if name == "15-core-code-evidence.md":
            check_aggregate_code_evidence(path, text)

        refs = IMAGE_RE.findall(text)
        if not refs:
            fail(f"{path.relative_to(ROOT)} has no image reference")

        for ref in refs:
            if ref.startswith(("http://", "https://")):
                fail(f"{path.relative_to(ROOT)} references remote image: {ref}")
            image_path = (path.parent / ref).resolve()
            if not image_path.exists():
                fail(f"{path.relative_to(ROOT)} references missing image: {ref}")
            if image_path.suffix == ".svg":
                ET.parse(image_path)

    print("core docs ok")


if __name__ == "__main__":
    main()
