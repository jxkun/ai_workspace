## Context

`learn_codex` 是 `ai_workspace/project/` 下的独立学习项目，用于长期分析 `openai/codex` harness。用户明确要求：

- 主要用 Markdown 文件承载文档内容。
- Markdown 原生流程图不作为最终图示，必须使用生成图片代替。
- 需要 `image/` 目录承载图片，内部按页面或主题分子目录。
- 可以拉取最新 Codex 代码到本地，后续基于该版本分析。
- 本轮先设计目录结构、分析方法论、生成 OpenSpec，并推进到完成态。

项目当前是空目录，仅有只读隐藏占位目录。因此本次设计先建立可持续分析的骨架和验收规则。

## Goals / Non-Goals

**Goals:**

- 建立项目自包含目录结构，后续分析不依赖其它 workspace。
- 建立源码快照记录，使“最新版”可追溯到具体 commit 或 release。
- 建立 Markdown 分析方法论，使每个结论可回到源码锚点复查。
- 建立图片资产规范，确保流程图、架构图、状态图和时序图都以生成图片交付。
- 建立 OpenSpec 需求真相源，并把本轮初始化任务闭环。

**Non-Goals:**

- 不在本轮完成所有 Codex harness 专题正文。
- 不修改上游 `repo/codex/` 源码。
- 不搭建复杂实验工具链。
- 不提交密钥、Token、Cookie、生产数据或个人敏感信息。

## Decisions

### D1: 项目自包含，但源码快照放入项目内 `repo/codex/`

`ai_workspace` 根规则建议外部源码放 `repo/`。本项目是专门分析 Codex harness 的独立学习单元，因此在项目内保留 `repo/codex/` 作为本项目专属研究对象，避免和其它项目共享一个会漂移的源码副本。

替代方案是使用 workspace 根 `repo/`，但这样会让 `learn_codex` 的文档、图片和源码版本锚点分离，后续复查成本更高。

### D2: 文档正文和图像资产分离

`docs/` 只承载 Markdown 正文、源码锚点、结论和待验证项。`image/` 是唯一图像资产根目录，并按主题或文档分子目录。

这能同时满足“Markdown 承载内容”和“流程图必须用生成图片”的约束。

### D3: 先方法论，再专题分析

本轮只完成 Stage 0：

- 项目入口和协作规则。
- 源码快照记录。
- 分析方法论。
- 图片资产规范。
- OpenSpec 需求和任务闭环。

后续再按 Entry、Core、Support、Extension 四层模型推进专题分析，避免把初始化任务扩展成不可验收的大型源码解读。

### D4: 每个专题必须绑定源码锚点和图片清单

每篇专题文档都必须包含源码锚点和图像资产清单。没有源码锚点的结论只能标为待验证；流程图类表达没有图片文件时不能算完成。

### D5: 版本锚点采用 main commit 加 release fallback

优先以 GitHub `main` 分支最新 commit 作为“最新版”分析锚点。当前 Git clone HTTPS 超时，但 GitHub API 和 codeload tarball 可访问，因此以固定 commit tarball 获取源码。SourceForge mirror 的最新 release 作为可复现 fallback，并在 `docs/source-snapshot.md` 记录 sha256。

## Directory Shape

```text
learn_codex/
  README.md
  AGENTS.md
  .gitignore
  docs/
    index.md
    methodology.md
    source-snapshot.md
    diagram-policy.md
  image/
    README.md
    methodology/
    architecture/
    runtime-loop/
    tool-sandbox/
    protocol-events/
    state-memory/
    extension-points/
  openspec/
    config.yaml
    changes/setup-codex-harness-study/
      proposal.md
      design.md
      tasks.md
      specs/codex-harness-study-workspace/spec.md
      execution/
  repo/
    codex/
  prompts/
  examples/
  scripts/
  tests/
  configs/
  data/
```

## Risks / Trade-offs

- GitHub clone 不稳定 → 使用 GitHub codeload 固定 commit tarball，SourceForge release mirror 作为 fallback，并记录来源。
- 图片生成工具链暂未固定 → 先定义图片资产契约，后续可在 `scripts/` 补统一生成脚本。
- “完整学习”范围过大 → OpenSpec 把本轮完成态限定为初始化，不提前声称完成全部 harness 分析。
- 上游 Codex 更新频繁 → 每次更新 `repo/codex/` 都必须同步 `docs/source-snapshot.md` 并复核专题源码锚点。

## Migration Plan

这是新项目初始化，无历史迁移。落地顺序：

1. 初始化 OpenSpec change。
2. 建立项目目录和基础文件。
3. 获取并解压源码快照到 `repo/codex/`。
4. 写入方法论、源码快照和图片规范。
5. 运行 `openspec validate setup-codex-harness-study --strict`。
6. 将 `tasks.md` 更新为完成态。

## Open Questions

- 后续专题图像生成工具是否统一为脚本化流程，留到后续 change 决定。
- 深度分析阶段是否需要把部分图源纳入版本管理，默认纳入同一 `image/<topic>/` 子目录。
