## Why

`learn_codex` 已具备源码快照和基础方法论，但还缺少一份面向初学者的 Codex harness 学习路线全景。没有路线图时，读者很容易从 `core` 或 `tui` 的大文件直接进入细节，无法形成对入口、主循环、工具执行、安全边界、状态持久化和扩展点的整体理解。

## What Changes

- 新增 `docs/codex-harness-learning-roadmap.md`，用专家视角为初学者拆解学习路径。
- 基于 `repo/codex/` 的真实目录给出 Entry、Core、Support、Extension 四层源码地图。
- 将学习过程拆成阶段，每阶段明确目标、源码入口、关键问题、建议产出和完成标准。
- 新增路线全景图片，放入 `image/learning-roadmap/` 并由 Markdown 引用。
- 更新文档索引，让后续学习从路线图进入。

## Capabilities

### New Capabilities

- `codex-harness-learning-roadmap`: 提供面向初学者、源码锚定、带图片资产的 Codex harness 学习路线全景。

### Modified Capabilities

- None.

## Impact

- 新增学习路线文档：`docs/codex-harness-learning-roadmap.md`。
- 新增图片资产：`image/learning-roadmap/`。
- 更新文档索引：`docs/index.md`。
- 新增 OpenSpec change：`openspec/changes/add-codex-harness-learning-roadmap/`。
- 不修改 `repo/codex/` 上游源码。
