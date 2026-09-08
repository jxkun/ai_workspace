## Why

`codex-rs/core` 是 Codex harness 的核心实现层，包含 thread/session/turn、工具调度、上下文、配置、安全、MCP、插件、压缩、rollout 等大量模块。直接按文件阅读会让初学者陷入细节，难以形成“我也能设计这套逻辑”的系统理解。因此需要先规划一套 core 层专题文档体系，明确每个模块如何讲、先后顺序、源码锚点和图示要求。

## What Changes

- 新增 core 层文档规划入口 `docs/core/README.md`。
- 按 `repo/codex/codex-rs/core/src/lib.rs` 和 `core/src` 实际结构，将 core 模块聚类为可学习专题。
- 为每个专题规划未来文档名、学习目标、小白讲解重点、源码锚点、建议图示、产出和完成标准。
- 新增 core 层模块地图 SVG，放在 `image/core/` 并由 Markdown 引用。
- 更新 `docs/index.md`，把 core 层规划纳入后续专题入口。
- 本次不完成所有 core 深度分析正文，只完成系统规划和验收基线。

## Capabilities

### New Capabilities

- `codex-core-module-doc-plan`: 提供覆盖 `codex-rs/core` 主要模块的文档规划、学习顺序、源码锚点和图示要求。

### Modified Capabilities

- None.

## Impact

- 新增文档：`docs/core/README.md`。
- 新增图片：`image/core/codex-core-module-map-v1.svg`。
- 新增 OpenSpec change：`openspec/changes/add-codex-core-module-doc-plan/`。
- 更新索引：`docs/index.md`。
- 不修改 `repo/codex/` 源码。
