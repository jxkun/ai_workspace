## Context

`implement-codex-core-docs` 的完成口径是第一版完整知识库：专题齐全、结构统一、源码锚点和 SVG 图示存在。这个口径适合从无到有，但还不足以支撑“只看 `docs/core/` 就能充分理解 harness”的目标。

本 change 采用 `$source-study-docs` 契约，把 core 文档集提升到更强的学习文档标准：读者应能从文档复盘一次请求、一次工具调用、一次上下文注入、一次扩展暴露和一次恢复/压缩，而不是只知道源码文件在哪里。

## Goals / Non-Goals

**Goals:**

- 消除 `docs/core/README.md` 的规划态表述，使它成为当前文档集入口。
- 在 README 中明确 core 文档质量分级和 harness-level 充分性门槛。
- 补充关键专题的端到端 trace、矩阵和参考答案要点。
- 让本地校验脚本覆盖更多机械质量门，包括源码锚点、过期措辞和答案闭环。

**Non-Goals:**

- 不把 15 篇文档一次性扩写到逐函数逐行级别。
- 不修改 `repo/codex/` 上游源码。
- 不新增复杂脚本依赖。
- 不要求每篇文档都在本轮生成新图；已有图示不足以表达状态/决策时记录后续图示需求。

## Decisions

### D1: 质量门分三档表达

README 将区分：

- `Skeleton`：文件、章节和图示存在。
- `Guided reading`：概念、源码锚点和主流程清楚。
- `Harness-level`：有可复演 trace、决策/状态矩阵、错误路径、跨模块契约和测试证据。

这样避免把第一版误称为完全充分，也给后续专题加深提供明确判断标准。

### D2: 优先修主干，不做均匀摊薄

本轮优先补强读者理解 harness 的关键路径：

- `02-session-turn-loop`：一次 turn 的端到端 trace。
- `03-context-world-state`：WorldState section 矩阵。
- `04-tool-runtime`：工具执行 trace 和工具矩阵。
- `09-extensions-inside-core`：外部能力进入 core 的矩阵。

前序文档补参考答案要点，解决自测闭环问题。

### D3: 自动校验只做机械检查

`scripts/check_core_docs.py` 继续作为本项目的文档守门脚本，但不冒充语义 review。它负责：

- 文档/章节/图片存在。
- 源码锚点路径大体可解析。
- 完成态文档不保留明显过期规划措辞。
- 检查题有参考答案或答案要点。

解释是否真实、trace 是否因果闭环，仍需要人工 review 或 `$source-study-docs` 审查。

## Validation

- `python3 scripts/check_core_docs.py` 通过。
- `python3 /data00/home/jiangxukun/.trae/skills/source-study-docs/scripts/check_source_study_docs.py --docs-dir docs/core --source-root repo/codex --image-root image/core --complete` 至少不因 README 规划态或答案缺失失败。
- `openspec validate harden-codex-core-docs --strict` 通过。
