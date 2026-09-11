## Context

现有学习路线把 Codex harness 拆成四层：

- `Entry`：CLI / TUI / app-server 等入口面。
- `Core`：`codex-rs/core` runtime loop，已由 `docs/core/` 覆盖。
- `Support`：protocol、rollout、thread-store、context-fragments、memory 等支撑能力。
- `Extension`：skills、plugins、MCP、hooks、connectors 等扩展面。

Core 文档已经按 `$source-study-docs` 的强口径加固，另外三层需要以同样的读者路径补齐入口级文档和代表性链路文档。本文档整理的目标不是复制 Core 的全部细分深度，而是让读者先能从三篇 layer overview 理解“谁调用 Core、谁支撑 Core、谁扩展 Core”，再通过每层至少一篇 deep-dive 复盘具体 runtime / integration path。

## Goals / Non-Goals

**Goals:**

- 每层新增一个索引 README、一个 `00-*` 总览文档和一个代表性 `01-*` deep-dive 文档。
- 每个 numbered topic 提供开篇综合图、源码锚点、核心抽象、主流程、失败边界、代码证据、复设计练习和检查题答案。
- 每篇 `01-*` deep-dive 提供行为证据矩阵，关键行为绑定源码和测试证据；没有测试时显式标 `source-only` / `test-gap`。
- 更新总索引和学习路线，使三层文档从规划态进入当前可读状态。
- 增加机械校验，保证图片引用、源码锚点和基础章节不漂移。

**Non-Goals:**

- 不修改 `repo/codex/` 上游源码。
- 不把 Entry / Support / Extension 的所有子模块一次性写成 Core 级别的多篇深挖。
- 不替代 `docs/core/` 对 runtime loop、tools、sandbox、multi-agent 和 compaction 的细节说明。
- 不新增非标准图示格式；正式 Markdown 最终引用 PNG，SVG 作为可编辑源文件保留。

## Decisions

### D1: 三层先落 overview，并补一篇代表性 deep-dive

`docs/core/` 已证明“一层目录 + README + 00 总览 + 后续专题”的形态适合学习路径。非 Core 三层本轮采用同构但更轻量的结构，并至少落一篇代表性 deep-dive，确保每层都有可复盘的具体链路：

- `docs/entry/README.md` + `docs/entry/00-entry-map.md` + `docs/entry/01-cli-tui-app-server-flow.md`
- `docs/support/README.md` + `docs/support/00-support-map.md` + `docs/support/01-protocol-rollout-thread-store.md`
- `docs/extension/README.md` + `docs/extension/00-extension-map.md` + `docs/extension/01-skills-plugins-mcp-hooks.md`

### D2: 代码证据选边界类型和路由函数

三层 overview 不追求逐函数覆盖，而优先证明边界；deep-dive 则复盘具体链路：

- Entry 侧证明 CLI/TUI/app-server 如何把输入变成 core thread/turn 操作。
- Support 侧证明 protocol、rollout、thread-store、context-fragments 和 memory 如何承载状态与持久化。
- Extension 侧证明 skill/plugin/MCP/hook/connector 如何被声明、装载、暴露和执行。

### D3: 图示按层放置并靠近正文

每层总览新增一张开篇综合 PNG，代表性 deep-dive 再各新增一张局部链路 PNG；同目录保留同名 SVG 源文件：

- `image/architecture/harness-entry-layer-v1.png`
- `image/architecture/entry-cli-tui-app-server-flow-v1.png`
- `image/state-memory/harness-support-layer-v1.png`
- `image/state-memory/support-protocol-rollout-thread-store-v1.png`
- `image/extension-points/harness-extension-layer-v1.png`
- `image/extension-points/extension-skills-plugins-mcp-hooks-v1.png`

图示必须在对应 `00-*` 文档开头附近引用，并用邻近文字说明读图顺序和源码锚点。

### D4: 校验脚本独立于 Core 专项脚本

`scripts/check_core_docs.py` 是 Core 专项守门。本 change 新增 `scripts/check_non_core_docs.py`，面向三层 overview + deep-dive 的当前完成口径：文件存在、章节存在、图片存在并可解析、源码锚点存在、每篇至少三段 typed code evidence、检查题有答案；每层至少一个非 `00` deep-dive，且 deep-dive 必须有行为证据矩阵。

## Validation

- `python3 scripts/check_non_core_docs.py` 通过。
- `python3 /data00/home/jiangxukun/.trae/skills/source-study-docs/scripts/check_source_study_docs.py --docs-dir docs/entry --source-root repo/codex --image-root image --complete` 通过。
- 同上分别检查 `docs/support` 与 `docs/extension`。
- `openspec validate organize-codex-non-core-layer-docs --strict` 通过。
