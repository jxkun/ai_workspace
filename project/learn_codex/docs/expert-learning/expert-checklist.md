# Codex Harness 专家验收清单

这份清单用于判断读者是否已经从“能看懂文档”进入“能用源码证据解释和重设计 Codex harness”的状态。

## 1. 全局解释能力

- 能用 Entry / Core / Support / Extension 四层解释 Codex harness。
- 能说明 CLI、TUI、app-server 为什么是入口面，而不是 runtime kernel。
- 能说出 `Op`、`EventMsg`、`CodexThread`、`RolloutItem` 各自保护的边界。
- 能根据 `repo/codex/codex-rs/Cargo.toml` 判断一个 crate 大致属于哪类能力。

## 2. 主循环复盘能力

- 能复盘 `TurnInputRequest -> TurnInputMode -> run_turn -> StepContext -> run_sampling_request`。
- 能解释模型请求为什么依赖 history、world state、tools、config 和 extensions。
- 能说明工具输出为什么可能触发 follow-up sampling。
- 能定位 turn cancel、pre-compact、pending input、stream retry 的源码入口。

## 3. 工具和安全判断能力

- 能区分 `ToolRegistry`、`ToolRouter`、`ToolSpec` 和 handler runtime。
- 能解释 `ToolOrchestrator::run` 为什么要统一 approval、sandbox、network 和 retry。
- 能根据 `AskForApproval` 和 `SandboxPolicy` 判断一次执行是否可能被拒绝。
- 能区分 `exec_command` 和 `apply_patch` 的事件、状态和安全语义。

## 4. 状态和恢复能力

- 能说明 `Submission` id 如何关联输入和事件。
- 能解释 `RolloutItem` 为什么包含 response item、event、world state、turn context、compaction 等多类记录。
- 能说明 `WorldStateSection` 的 `snapshot` 和 `render_diff` 分别解决什么问题。
- 能复盘 resume/fork 为什么需要 checkpoint 和重放，而不是简单加载全文。

## 5. 扩展系统能力

- 能区分 skill、plugin、MCP、hook、connector、agent 的职责。
- 能解释 plugin manifest 为什么可以包含 skills、MCP servers、apps 和 hooks。
- 能说明 MCP tool event 中 `plugin_id`、`connector_id`、`read_only_hint` 的用途。
- 能设计一个新扩展能力的声明、加载、暴露、执行、事件和失败路径。

## 6. 源码证据能力

- 任意讲一个机制时，能给出至少一个源码路径和一个符号。
- 对 runtime、state、protocol、safety、extension 结论，能指出测试证据或明确 `source-only` / `test-gap`。
- 能把文档中的流程图映射回真实源码，而不是只复述概念。
- 能发现文档里缺少代码片段、实体定义、失败路径或测试证据的地方。

## 7. 源码校验入口

最终自测至少要能回到这些源码入口：

- `repo/codex/codex-rs/core/src/codex_thread.rs::CodexThread`：验证 thread 对外 API 和 submission 边界。
- `repo/codex/codex-rs/core/src/session/turn.rs::run_turn`：验证 turn 主循环、step context 和 sampling 入口。
- `repo/codex/codex-rs/core/src/tools/orchestrator.rs::ToolOrchestrator::run`：验证工具 approval、sandbox 和 retry 外壳。
- `repo/codex/codex-rs/history/src/lib.rs::RolloutItem`：验证 rollout 可恢复记录类型。
- `repo/codex/codex-rs/skills/src/model.rs::SkillMetadata`：验证 skill 声明、policy 和 scope。

## 8. 最终验收题

请闭卷回答下面 5 个问题，再用源码校验：

1. 一次用户输入从 app-server 到模型请求至少经过哪些对象？
2. 一个 shell 工具调用在哪些位置可能被拦截或拒绝？
3. 恢复一个历史 thread 时，哪些 rollout item 会影响模型可见上下文？
4. 一个 plugin 如何把 MCP 工具暴露给模型，并如何被事件追踪？
5. 如果让你从零设计一个最小 Codex-like harness，你会如何切 thread、turn、tool、history、extension 边界？

答案通过标准：

- 每题至少能说出 3 个源码锚点或协议类型。
- 每题能指出一个失败分支。
- 第 5 题能给出清晰的 owner、state、event、persistence、safety 分工。
