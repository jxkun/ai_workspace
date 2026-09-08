# Intent

原始意图锚。开工前由 `Master` 依据用户最初诉求固化，冻结、极少改；改动需用户确认。

## 原始诉求

- 按照已有 core 层文档规划，把 core 层文档整理出来。
- 推进到终态。

## 关键约束

- 默认中文。
- 以 `repo/codex/` 的实际源码为第一事实来源。
- 产出面向小白但由专家视角组织，目标是让读者读完后能复设计类似逻辑。
- 每篇文档需要源码锚点、核心抽象、主流程、失败模式、图示、复设计练习、检查题和 Follow-up Slots。
- 图示必须是生成图片，优先 SVG，放入 `image/core/`。
- 不修改 `repo/codex/` 上游源码。

## 明确的非目标

- 不实现 Codex 上游功能。
- 不运行大型 Rust 测试或修改上游代码。
- 不把文档写成普通 Codex CLI 使用教程。

## 验收口径

- `docs/core/README.md` 中规划的 core 专题文档全部存在。
- 每篇专题文档都具备统一结构和源码锚点。
- 每篇涉及流程/架构的专题都有对应 `image/core/*.svg` 生成图片并在文档中引用。
- `docs/index.md` 能进入 core 文档集。
- OpenSpec `implement-codex-core-docs` artifacts 齐备，tasks 全部完成，strict validate 通过。
