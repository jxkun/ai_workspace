# Intent

原始意图锚。开工前由 `Master` 依据用户最初诉求固化，冻结、极少改；改动需用户确认。

## 原始诉求

- 这个目录用于学习和分析 Codex harness。
- 希望完整学习 Codex harness 的实现和思想。
- 主要使用 Markdown 文件承载具体文档内容。
- Markdown 自身流程图等表达较丑，必须用具体生成的图片替代流程图。
- 需要 `image/` 目录承载图片，内部按需分子目录。
- 可以把 Codex 最新版代码拉取到本地，后续基于此版本分析。
- 本轮先设计目录结构，产出后续分析方法论，生成 OpenSpec，并推进到完成态。

## 关键约束

- 默认中文文档。
- OpenSpec 必须作为本轮需求真相源。
- 源码快照必须有版本锚点，不能只写“最新版”。
- 图示强制使用生成图片作为最终资产，不能只用 Mermaid、PlantUML 或 ASCII 图。
- 本轮完成态只覆盖初始化和方法论，不代表已经完成全部 Codex harness 深度分析。

## 明确的非目标

- 不在本轮完成所有 Codex harness 专题正文。
- 不修改上游 Codex 源码。
- 不搭建复杂实验工具链。
- 不触碰 `learn_llm` 或 workspace 中其它无关改动。

## 验收口径

- `learn_codex` 下存在清晰项目目录和基础协作文件。
- `docs/methodology.md` 说明后续如何分析 Codex harness。
- `image/` 存在，并有可执行的图片资产规范和至少一张初始图片。
- `repo/codex/` 有本地源码快照，`docs/source-snapshot.md` 记录来源与版本。
- OpenSpec proposal/design/spec/tasks 存在，并通过严格校验。
- `tasks.md` 能反映本轮初始化工作已完成。
