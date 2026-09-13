# Codex Harness 分析文档索引

本目录承载 `openai/codex` harness 的学习、分析和后续实验记录。所有结论以 `../repo/codex/` 的源码快照为准。

## 基础文档

- [分析方法论](methodology.md)：后续如何拆解、阅读、记录、验证 Codex harness。
- [学习路线全景](codex-harness-learning-roadmap.md)：面向小白的系统学习阶段、源码入口和产出规划。
- [专家学习路径](expert-learning/README.md)：从全局模型、Core 主循环、工具安全、状态恢复到扩展体系的课程化学习路径。
- [Entry 层文档索引](entry/README.md)：CLI、TUI、app-server 等入口面如何收敛到 Core thread / turn 边界。
- [Core 层文档索引](core/README.md)：`codex-rs/core` 主要模块的专题文档、源码锚点、质量门和后续加固路线。
- [Support 层文档索引](support/README.md)：protocol、rollout、thread-store、context-fragments 和 memory 等支撑能力。
- [Extension 层文档索引](extension/README.md)：skills、plugins、MCP、hooks、connectors 等扩展点如何进入 harness。
- [源码快照](source-snapshot.md)：当前源码来源、版本锚点、获取方式和刷新规则。

## 当前专题

专题文档按 [学习路线全景](codex-harness-learning-roadmap.md) 和四层模型维护：

0. [专家学习路径](expert-learning/README.md)：面向小白到专家的课程入口。
1. [Entry 层总览](entry/00-entry-map.md)：CLI/TUI/app-server 到 Core thread / turn 的入口边界。
2. [Entry 入口链路](entry/01-cli-tui-app-server-flow.md)：CLI dispatch、TUI app-server session、thread/start 和 turn/start 的实际链路。
3. [Entry CLI 命令面](entry/02-cli-command-surface.md)：`Subcommand`、root overrides、guard 和 headless `exec`。
4. [Entry TUI 线程事件路由](entry/03-tui-thread-event-routing.md)：`ChatWidget`、`AppServerSession`、`ThreadEventChannel` 和 active/side thread。
5. [Entry app-server 控制面](entry/04-app-server-json-rpc-control-plane.md)：typed `ClientRequest`、initialize gate、serialization scope 和 processor dispatch。
6. [Core 层文档集](core/README.md)：Core runtime、turn loop、tools、安全、上下文、恢复和 multi-agent。
7. [Support 层总览](support/00-support-map.md)：协议、历史、rollout、thread-store、context-fragments 和 memory。
8. [Support 支撑链路](support/01-protocol-rollout-thread-store.md)：`Submission`、`Op`、`EventMsg`、`RolloutItem`、JSONL 和 `ThreadStore`。
9. [Extension 层总览](extension/00-extension-map.md)：skills、plugins、MCP、hooks、connectors 的声明与运行时边界。
10. [Extension 扩展链路](extension/01-skills-plugins-mcp-hooks.md)：skill 选择、plugin bundle、MCP binding、hook 和 connector projection。
11. [专家课程 01：全局心智模型](expert-learning/01-global-model.md)：四层模型和一次请求的全局生命周期。
12. [专家课程 02：Core 主循环](expert-learning/02-core-runtime-loop.md)：thread/session/turn、step context、model sampling 和 tool follow-up。
13. [专家课程 03：工具安全与 Patch](expert-learning/03-tools-safety-patch.md)：tool router、approval、sandbox、exec 和 apply_patch。
14. [专家课程 04：状态协议与 Memory](expert-learning/04-state-protocol-memory.md)：submission、event、rollout、world state、resume 和 memory。
15. [专家课程 05：扩展体系](expert-learning/05-extension-system.md)：skills、plugins、MCP、hooks、connectors 和 multi-agent。
16. [专家练习集](expert-learning/exercises.md) 与 [专家验收清单](expert-learning/expert-checklist.md)：验证源码定位、流程复盘、故障诊断和重设计能力。

## 图像资产

图像资产统一放在 `../image/`，并按主题或文档分子目录。Markdown 中只能引用最终生成的图片文件，不把 Mermaid、PlantUML 或 ASCII 流程图作为最终图示。
