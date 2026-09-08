# Codex Harness 分析文档索引

本目录承载 `openai/codex` harness 的学习、分析和后续实验记录。所有结论以 `../repo/codex/` 的源码快照为准。

## 基础文档

- [分析方法论](methodology.md)：后续如何拆解、阅读、记录、验证 Codex harness。
- [学习路线全景](codex-harness-learning-roadmap.md)：面向小白的系统学习阶段、源码入口和产出规划。
- [Core 层文档索引](core/README.md)：`codex-rs/core` 主要模块的专题文档、源码锚点、质量门和后续加固路线。
- [源码快照](source-snapshot.md)：当前源码来源、版本锚点、获取方式和刷新规则。

## 后续专题

后续专题文档按 [学习路线全景](codex-harness-learning-roadmap.md) 逐步补齐，建议顺序如下：

1. `harness-overview.md`：harness 边界、入口和全局架构。
2. `runtime-loop-analysis.md`：主循环、事件推进和模型交互。
3. `tool-sandbox-analysis.md`：工具执行、sandbox、审批和 `apply_patch`。
4. `protocol-and-events.md`：协议、事件、消息结构和前后端边界。
5. `state-and-memory.md`：会话、rollout、压缩、上下文与 memory。
6. `extension-points.md`：skills、plugins、MCP、hooks 等扩展点。

## 图像资产

图像资产统一放在 `../image/`，并按主题或文档分子目录。Markdown 中只能引用最终生成的图片文件，不把 Mermaid、PlantUML 或 ASCII 流程图作为最终图示。
