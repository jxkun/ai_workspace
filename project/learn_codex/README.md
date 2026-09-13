# Codex Harness 学习与分析

本项目用于系统学习和分析 `openai/codex` harness 的实现与设计思想。项目以 Markdown 文档为主载体，但图示不使用 Markdown 原生流程图或 ASCII 图作为最终交付；所有流程图、架构图、状态图都必须生成图片并放入 `image/`。

## 目录结构

```text
learn_codex/
  README.md
  AGENTS.md
  .gitignore
  docs/
    methodology.md
    source-snapshot.md
    expert-learning/
    entry/
    core/
    support/
    extension/
  image/
    methodology/
    expert-learning/
    architecture/
    state-memory/
    extension-points/
  openspec/
    changes/
      setup-codex-harness-study/
  repo/
    codex/
  prompts/
  examples/
  scripts/
  tests/
  configs/
  data/
```

## 关键约束

- `repo/codex/` 是本地源码快照目录，后续分析以该目录的实际代码为准。
- `docs/` 只放项目专属学习文档、分析方法论和阶段成果。
- `image/` 是图像资产根目录，按文档或主题继续分子目录。
- 文档可以引用图片，但最终图示必须是图片文件，不能依赖 Mermaid、PlantUML、ASCII 图等 Markdown 内嵌图示。
- 每篇分析文档都要给出源码锚点，至少包含路径、符号或测试文件。

## 当前状态

- OpenSpec 初始化 change: `openspec/changes/setup-codex-harness-study/`
- 文档入口: `docs/index.md`
- 方法论入口: `docs/methodology.md`
- 学习路线: `docs/codex-harness-learning-roadmap.md`
- 专家学习路径: `docs/expert-learning/README.md`
- 源码快照记录: `docs/source-snapshot.md`
- 当前四层文档入口: `docs/entry/README.md`、`docs/core/README.md`、`docs/support/README.md`、`docs/extension/README.md`
