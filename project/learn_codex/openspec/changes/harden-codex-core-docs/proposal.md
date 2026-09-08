## Why

`docs/core/` 已完成 15 篇 core 层第一版专题文档，但当前质量门仍偏“文件齐、章节齐、图片齐”。用户希望基于 `$source-study-docs` 的新契约继续质检和优化，使核心文档不只是源码导读，而是逐步达到“读者不看代码也能理解 Codex harness 运行机制”的标准。

## What Changes

- 将 `docs/core/README.md` 从规划入口改成当前文档集索引与质量门说明。
- 为 core 文档集补充 harness-level 充分性契约，明确端到端 trace、决策/状态矩阵、错误路径、跨模块契约、测试证据和参考答案要求。
- 优先加固核心主链路文档：`02-session-turn-loop`、`03-context-world-state`、`04-tool-runtime`、`09-extensions-inside-core`。
- 为缺少参考答案的前序文档补齐检查题答案要点。
- 扩展 `scripts/check_core_docs.py`，让它不只检查骨架，还能发现过期规划措辞、源码锚点路径缺失和缺少答案要点等问题。

## Impact

- 修改 `docs/core/README.md`、部分 `docs/core/*.md` 和 `scripts/check_core_docs.py`。
- 新增 OpenSpec change `harden-codex-core-docs`。
- 不修改 `repo/codex/` 上游源码。
