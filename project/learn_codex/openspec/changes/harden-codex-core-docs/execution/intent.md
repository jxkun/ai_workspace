# Intent

原始意图锚。开工前由 `Master` 依据用户最初诉求固化，冻结、极少改；改动需用户确认。

## 原始诉求

- 用户要求使用 `$fast-multi-agent`，基于最新的 `$source-study-docs` 契约，把 `docs/core/` 下的 Codex core 源码学习文档整体优化一遍。

## 关键约束

- 默认中文沟通和写文档。
- 以 `repo/codex/` 当前源码快照为第一事实来源。
- 不修改 `repo/codex/` 上游源码。
- 文档成果保留在 `docs/core/`，图像资产复用或放入 `image/core/`。
- 最终流程图、架构图、状态图必须是本地图片引用；不把 Mermaid、PlantUML、ASCII 图作为最终图示交付。
- 关键架构判断需要能回到 `repo/codex/` 的具体文件、类型、函数、测试或协议文件复查。
- 按 OpenSpec change `harden-codex-core-docs` 维护需求真相源和验证状态。

## 明确的非目标

- 不做 `repo/codex/` 的实验性 patch。
- 不扩散到其它 `project/` 子目录。
- 不把每篇文档改成逐函数逐行源码讲解。
- 不为通过脚本而移除必要的学习内容或源码锚点。

## 验收口径

- `docs/core/*.md` 对 latest `$source-study-docs` complete-mode 的机械质量门通过。
- 每篇 substantive core 专题近顶部有 opening synthesis diagram 或明确豁免。
- 复杂流程、状态、边界、失败路径附近有本地图示或明确说明无需新增图。
- 核心抽象、状态、协议、配置、失败路径附近有可审计的 Source / Line range / typed code block，或明确说明本节只做导航、证据在邻近章节。
- `scripts/check_core_docs.py`、`check_source_study_docs.py --complete`、`openspec validate harden-codex-core-docs --strict` 通过，或记录无法通过的具体原因。
