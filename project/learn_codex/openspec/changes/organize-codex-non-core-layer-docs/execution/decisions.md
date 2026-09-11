# Decisions

只记录 `Master` 已拍板并冻结的决策，不记录讨论过程。

## D-001

- 决策内容：本轮“另外三层”按现有四层学习路线解释为 `Entry`、`Support`、`Extension`，不包含已经完成的 `Core`。
- 原因：`docs/codex-harness-learning-roadmap.md` 已定义 Entry/Core/Support/Extension 四层，`docs/core/` 已有完整专题集。
- 影响模块：M01, M02, M03, M04, M05
- 生效时间：2026-09-08

## D-002

- 决策内容：采用 OpenSpec 后端，change 名为 `organize-codex-non-core-layer-docs`。
- 原因：项目规则要求修改项目结构、分析方法论或长期任务拆分时先更新 OpenSpec；本轮涉及三层文档目录和长期文档路线。
- 影响模块：M01, M02, M03, M04, M05, M06
- 生效时间：2026-09-08

## D-003

- 决策内容：本轮完成三层入口级总览，不承诺每个子专题都达到 Core 文档集的 16 篇深度。
- 原因：用户要求“进行整理”并推进到完成态；可完成边界应是三层总览、证据地图、索引、图示和校验闭环，细分专题可作为后续 deep dive。
- 影响模块：M02, M03, M04
- 生效时间：2026-09-08

## D-004

- 决策内容：撤销“只有三篇 `00-*map` 即完成”的口径；完成态改为 Entry / Support / Extension 各至少包含一篇真实 deep-dive 专题，并由 README、OpenSpec、脚本和 review 覆盖。
- 原因：用户反馈“只搞了个 map 就没了”，说明上一轮 DONE 判定过早；source-study-docs 的文档整理目标也要求读者能复盘具体 runtime / integration path。
- 影响模块：M07, M09, M10, M11
- 生效时间：2026-09-08
