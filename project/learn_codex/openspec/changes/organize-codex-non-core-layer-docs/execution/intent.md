# Intent

原始意图锚。开工前由 `Master` 依据用户最初诉求固化，冻结、极少改；改动需用户确认。

## 原始诉求

- 用户要求基于 `$fast-multi-agent` 协作模式，对 Codex harness 学习路线里除 Core 以外的另外三层文档进行整理。
- 需要先进行规划，然后再写文档。
- 需要有 review，并推进到完成态。

## 关键约束

- 默认中文沟通和中文文档。
- 以 `repo/codex/` 当前源码快照为第一事实来源，不修改上游源码。
- 修改项目结构、分析方法论或长期任务拆分时先更新 OpenSpec，再更新文档。
- 文档类变更至少检查路径、链接和 OpenSpec 校验。
- 流程图、架构图和状态图最终必须是 `image/` 下生成的本地图片，最终引用 PNG，保留 SVG 源文件。
- 使用 fast-multi-agent 编排：至少有 Coder 写作切片和 Reviewer 质检切片；Master 负责计划、仲裁、收口。

## 明确的非目标

- 不把 `docs/core/` 已有 16 篇文档重写一遍。
- 不在本轮修改 `repo/codex/` 源码。
- 不把 Entry / Support / Extension 的所有子专题一次性扩到 Core 级别深度。
- 不执行 commit、PR 或发布动作。

## 验收口径

- OpenSpec change `organize-codex-non-core-layer-docs` 的 proposal/design/tasks/spec 和执行态文件存在且内容一致。
- Entry / Support / Extension 三层各有 README、`00-*` 总览文档和开篇 PNG。
- 三篇总览文档包含源码锚点、至少三段带 `Source:` 和 `Line range:` 的 Rust 代码证据、主流程、失败边界、复设计练习和检查题答案。
- 总索引和学习路线指向三层当前文档，不再只把它们作为未来文档占位。
- 本地非 Core 文档检查、source-study-docs 检查和 OpenSpec 校验通过，且 review 无阻断级 finding。
