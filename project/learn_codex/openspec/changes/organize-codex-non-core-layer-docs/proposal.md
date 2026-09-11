## Why

`docs/core/` 已经形成较完整的 Core 层专题文档，但学习路线里定义的另外三层 `Entry`、`Support`、`Extension` 仍停留在路线图和图片目录占位状态。读者如果只从当前文档进入，会直接跳到 Core 细节，缺少入口面、支撑层和扩展面的并行心智模型。

## What Changes

- 新增 `docs/entry/`、`docs/support/`、`docs/extension/` 三个文档目录，每层提供 README 索引、`00-*` 总览文档和至少一篇代表性 `01-*` deep-dive。
- 为三层总览和代表性 deep-dive 新增本地 PNG 图示，并在同目录保留 SVG 源文件，放在 `image/architecture/`、`image/state-memory/`、`image/extension-points/`。
- 三层文档采用与 `docs/core/` 一致的 source-study-docs 结构：源码锚点、核心抽象、主流程、失败边界、核心代码片段、行为证据矩阵、复设计练习和检查题答案。
- 更新 `docs/index.md`、`docs/codex-harness-learning-roadmap.md` 和根 README，使非 Core 三层成为当前可读文档，而不是悬空规划。
- 新增本地校验脚本，检查三层文档文件、图片、源码锚点、代码证据和 OpenSpec 状态。

## Impact

- 修改文档、图片资产、OpenSpec change 和校验脚本。
- 不修改 `repo/codex/` 上游源码。
- 不把本轮定义为所有非 Core 细分专题的最终深挖完成；本轮完成口径是三层 overview + 每层至少一篇代表性 deep-dive + 校验门禁。
