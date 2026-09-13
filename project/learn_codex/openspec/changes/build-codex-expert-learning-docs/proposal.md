## Why

现有 `docs/core`、`docs/entry`、`docs/support`、`docs/extension` 已经形成源码导读和 harness-level 加固基线，但读者仍需要一条更清晰的“从小白到专家”的课程路径。用户希望以技术专家视角拆解 Codex 核心流程，同时让初学者读完后能复盘设计、定位源码、判断边界并做二次设计。

## What Changes

- 新增 `docs/expert-learning/` 专家教材入口和五篇核心课程，按“全局 -> 核心主循环 -> 工具安全 -> 状态恢复 -> 扩展体系”组织。
- 新增练习集和专家验收清单，把源码定位、流程复盘、故障诊断、重设计能力纳入学习闭环。
- 新增 `image/expert-learning/` 下的 PNG/SVG 图像资产，所有专题开篇和关键流程使用本地 PNG 图。
- 新增 `scripts/check_expert_learning_docs.py`，对专家学习目录做项目级机械检查。
- 更新 `docs/index.md`、`README.md`、`docs/codex-harness-learning-roadmap.md` 和 `scripts/README.md`，把专家教材作为当前可执行学习路径。

## Impact

- 不修改 `repo/codex/` 上游源码。
- 复用现有 Core、Entry、Support、Extension 文档作为证据库和深读入口。
- 新文档以 `docs/source-snapshot.md` 记录的 `repo/codex/` commit 为源码基线。
