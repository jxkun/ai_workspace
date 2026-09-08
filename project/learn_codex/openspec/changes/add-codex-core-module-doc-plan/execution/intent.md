# Intent

原始意图锚。开工前由 `Master` 依据用户最初诉求固化，冻结、极少改；改动需用户确认。

## 原始诉求

- 现针对 Codex harness 的 core 层进行拆解。
- 对 `codex-rs/core` 下每个模块规划详细文档，用于后续逐篇介绍。
- 讲解视角是专家给小白讲，要让小白看完后完全掌握，甚至可以自己设计这段逻辑。
- 构建 OpenSpec，并基于 OpenSpec 把本轮任务推进到完成态。

## 关键约束

- 默认中文。
- 以 `repo/codex/` 的实际源码结构为事实来源，尤其是 `repo/codex/codex-rs/core/src/lib.rs` 和 `repo/codex/codex-rs/core/Cargo.toml`。
- 本轮产物是 core 层文档规划、路线、模板和视觉地图，不是完成所有 core 模块详解正文。
- Markdown 承载正文；流程图、架构图、模块关系图必须使用生成图片，优先 SVG。
- 不修改 `repo/codex/` 上游源码。

## 明确的非目标

- 不逐篇写完所有 core 深度分析文档。
- 不运行或修改 Codex 上游测试。
- 不扩大到 Entry、Support、Extension 的完整专题，只在解释 core 边界时引用它们。

## 验收口径

- 新增 OpenSpec change `add-codex-core-module-doc-plan`，proposal/design/spec/tasks 齐备且 strict validate 通过。
- 新增 `docs/core/README.md` 作为 core 层文档规划入口。
- 规划覆盖 `core/src` 的主要模块与一级目录，并按职责聚类到可执行专题。
- 每个专题规划包含目标、面向小白的讲解重点、源码锚点、图示要求、建议产物和完成标准。
- 至少生成一张 core 层模块地图 SVG，并由文档引用。
