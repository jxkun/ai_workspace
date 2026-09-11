# 图示与图片资产策略

本项目强制使用生成图片承载图示。Markdown 只负责正文、源码锚点和图片引用。

## 基本原则

- 流程图、架构图、状态图、时序图必须导出为图片文件。
- 图片统一放在 `image/`，按文档或主题分子目录。
- 文档正文不得依赖 Mermaid、PlantUML 或 ASCII 图作为最终表达。
- 如果使用 DSL 或草图源生成图片，源文件和导出图片放在同一个主题目录。
- 图片需要能回到源码锚点，不能只是抽象装饰图。
- 正式 Markdown 文档最终引用 PNG 图，SVG 作为同目录可编辑源文件保留；PNG 必须从 SVG 或高分辨率画布导出，保证抗锯齿、文字清晰和线条稳定。
- 不交付像素感明显、线条粗糙、文字发虚、布局拥挤的图片。

## 推荐工作流

1. 在 Markdown 中先写清图要回答的问题。
2. 从 `repo/codex/` 找到对应源码锚点。
3. 生成图片源文件或直接生成图片。
4. 同时保留 `svg` 源文件和同名 `png` 预览；正式 Markdown 引用 `png`。
5. 在 Markdown 中引用图片。
6. 检查图片文件是否存在、路径是否有效、缩放查看是否清晰。

## 初始图片

- `image/methodology/codex-harness-study-methodology-v2.png`：本项目分析方法论总览图，当前推荐版本。

后续专题图片应跟随专题目录命名，例如：

- `image/runtime-loop/runtime-loop-main-v1.png`
- `image/tool-sandbox/tool-execution-approval-v1.png`
- `image/state-memory/thread-rollout-memory-v1.png`
