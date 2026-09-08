## Why

`docs/core/README.md` 已经完成 `codex-rs/core` 的文档规划，但目前还只是规划入口。用户要求按规划把 core 层文档整理到终态，因此需要实际产出每个规划专题的第一版完整文档和配套 SVG 图，形成可连续学习的 core 层知识库。

## What Changes

- 按 `docs/core/README.md` 的规划新增 core 层专题文档。
- 每篇文档使用统一教学结构：掌握目标、模块问题、源码锚点、核心抽象、主流程、失败模式与边界、图示、复设计练习、检查题、Follow-up Slots。
- 为每篇专题补充至少一张生成 SVG 图片，放在 `image/core/` 并由 Markdown 引用。
- 更新 `docs/core/README.md` 和 `docs/index.md`，使读者能进入完整 core 文档集。
- 不修改 `repo/codex/` 上游源码。

## Capabilities

### New Capabilities

- `codex-core-docs`: 提供覆盖 `codex-rs/core` 主要模块的中文专题文档集和配套 SVG 图示。

### Modified Capabilities

- `codex-core-module-doc-plan`: 从文档规划升级为已落地的 core 文档索引和覆盖状态。

## Impact

- 新增 `docs/core/*.md` 专题文档。
- 新增 `image/core/*.svg` 图像资产。
- 更新 `docs/core/README.md` 与 `docs/index.md`。
- 新增 OpenSpec change `openspec/changes/implement-codex-core-docs/`。
