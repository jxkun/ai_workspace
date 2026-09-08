## Why

`learn_codex` 需要成为一个可持续学习和分析 `openai/codex` harness 的项目，而不是零散笔记目录。当前目录缺少项目入口、源码快照、图片资产规则、方法论和可验收的 OpenSpec 计划，后续分析容易失去版本锚点或偏成普通 Codex 使用教程。

## What Changes

- 新增项目级目录结构，区分 `docs/`、`image/`、`repo/`、`examples/`、`scripts/`、`tests/`、`configs/`、`data/` 的职责。
- 新增 `repo/codex/` 作为本地 `openai/codex` 源码快照目录，并记录快照来源、commit 和 fallback 下载方式。
- 新增以 Markdown 为主的分析文档体系，并定义后续专题文档的分析模板、阶段节奏和源码证据规范。
- 新增 `image/` 图片资产根目录和图示规范，强制流程图、架构图、状态图和时序图以生成图片作为最终交付。
- 新增项目级 `README.md`、`AGENTS.md`、`.gitignore`，让后续 agent 能按本项目规则继续工作。
- 本次变更不完成全部 Codex harness 深度分析正文，只完成分析工程的结构、方法论和可复现基线。

## Capabilities

### New Capabilities

- `codex-harness-study-workspace`: 规定 Codex harness 学习项目的目录结构、源码快照、Markdown 文档方法论、图片资产约束和完成验收方式。

### Modified Capabilities

- None.

## Impact

- 新增项目内文档和配置：`README.md`、`AGENTS.md`、`.gitignore`、`docs/`、`image/`。
- 新增 OpenSpec change：`openspec/changes/setup-codex-harness-study/`。
- 新增本地源码快照目录：`repo/codex/`。
- 不修改上游 `openai/codex` 源码，不引入真实密钥或生产数据。
