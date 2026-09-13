# Codex Harness 专家练习集

本文用于验证读者是否真正理解 Codex harness。练习分为源码定位、流程复盘、故障诊断和重设计四类。每题都要能回到 `repo/codex/` 的源码锚点复查。

## 1. 源码定位题

### 1.1 入口到 Core

题目：用户从 app-server 发起一个 `turn/start`，请找出它最终进入 Core 的协议对象和外部操作面。

答案要点：

- 协议对象应落到 `repo/codex/codex-rs/protocol/src/protocol.rs::Op::TurnInput`。
- turn 输入结构应查看 `repo/codex/codex-rs/protocol/src/turn_input.rs::TurnInputRequest`。
- Core 对外操作面应查看 `repo/codex/codex-rs/core/src/codex_thread.rs::CodexThread::submit`。
- 继续深读可转到 [01-global-model.md](01-global-model.md) 和 [02-core-runtime-loop.md](02-core-runtime-loop.md)。

### 1.2 工具安全边界

题目：模型请求执行 shell 命令时，在哪里判断是否要 approval 和 sandbox？

答案要点：

- 工具路由先看 `repo/codex/codex-rs/core/src/tools/router.rs::ToolRouter`。
- per-step 工具装配看 `repo/codex/codex-rs/core/src/tools/spec_plan.rs::build_tool_router`。
- approval/sandbox 统一外壳看 `repo/codex/codex-rs/core/src/tools/orchestrator.rs::ToolOrchestrator::run`。
- policy 类型看 `repo/codex/codex-rs/protocol/src/protocol.rs::AskForApproval` 和 `SandboxPolicy`。

### 1.3 恢复材料

题目：一次恢复为什么不能只读模型消息？需要定位哪些持久化记录？

答案要点：

- rollout 类型看 `repo/codex/codex-rs/history/src/lib.rs::RolloutItem`。
- JSONL 行 envelope 看 `repo/codex/codex-rs/history/src/lib.rs::RolloutLine`。
- JSON 解码边界看 `repo/codex/codex-rs/rollout/src/lib.rs::decode_rollout_line`。
- 反向扫描和正向重放看 `repo/codex/codex-rs/core/src/session/rollout_reconstruction.rs::reconstruct_history_from_rollout`。

## 2. 流程复盘题

### 2.1 一次普通 turn

题目：不打开源码，复述一次用户输入如何变成模型响应和事件输出。

答案要点：

- Entry 生成 `Op::TurnInput`。
- `CodexThread::submit` 送入 Core。
- `TurnInputMode` 决定 start 或 steer。
- `run_turn` 做 pre-compact、hook、step context capture。
- `run_sampling_request` 构造 prompt 和 `ToolCallRuntime`。
- 模型输出变成文本事件、工具调用、token usage 或 error event。
- 工具输出进入后续模型输入，直到 `TurnComplete` 或错误/取消。

### 2.2 一次工具调用

题目：复盘模型调用工具时的最小路径。

答案要点：

- 当前 step 构建 `ToolRouter`。
- tool call 通过 router 找 runtime handler。
- `ToolOrchestrator::run` 处理 approval 和 sandbox。
- handler 执行并发出 begin/end/delta 等事件。
- 结果进入 history 和后续 prompt，可能触发 follow-up sampling。

### 2.3 一次 resume

题目：复盘恢复一个历史线程时，哪些记录会影响模型上下文？

答案要点：

- `SessionMeta` 提供 session/thread 元信息。
- `ResponseItem` 和 `Compacted` 影响模型历史。
- `TurnContext`、`WorldState`、`RetainedContext` 影响恢复时的上下文重建。
- `EventMsg` 影响可观察历史和客户端展示。
- `rollout_reconstruction` 会处理 checkpoint、rollback、legacy compaction 等分支。

## 3. 故障诊断题

### 3.1 用户说“命令没有执行”

答案要点：

- 先确认模型是否真的发出了 tool call。
- 检查 `ToolRouter` 中该工具是否对模型可见。
- 检查 `AskForApproval` 和 `SandboxPolicy` 是否导致 declined/rejected。
- 检查是否有 `ExecCommandBeginEvent`、`ExecCommandEndEvent` 或 `ExecCommandStatus::Declined`。
- 如果是 patch，改查 `PatchApplyBeginEvent` / `PatchApplyEndEvent` 和 `PatchApplyStatus`。

### 3.2 用户说“恢复后上下文不对”

答案要点：

- 先确认 `RolloutLine` 是否能被解析。
- 检查是否存在 `Compacted`、`TurnContext`、`WorldState`、`RetainedContext`。
- 检查 `rollout_reconstruction` 是否命中 legacy compaction、rollback 或 checkpoint 逻辑。
- 分清 memory stale 和 current turn state 缺失。

### 3.3 用户说“MCP 工具没有出现”

答案要点：

- 检查 plugin/MCP 配置是否加载。
- 检查 `build_tool_router` 是否 append MCP tools。
- 检查 apps/connectors 是否 enabled。
- 检查 startup failure 或 auth/elicitation 事件。
- 检查模型可见 spec，而不只是 MCP server 自身是否存在。

## 4. 重设计题

### 4.1 设计最小 agent harness

要求：

- 定义 `Op` 和 `Event` 两个协议枚举。
- 定义 `Thread` 对外 API，不暴露内部 session。
- 定义 `run_turn`，包含 context capture、model call、tool call、event output。
- 定义 JSONL history，至少保存输入、输出、工具结果、错误和 compaction。
- 定义 tool approval 和 sandbox policy。

评分要点：

- 协议边界清楚。
- 状态 owner 清楚。
- 工具副作用有安全外壳。
- 恢复不依赖 UI 进程内存。
- 错误能被用户和模型共同观察。

### 4.2 设计一个新扩展能力

要求：

- 判断能力应作为 skill、plugin、MCP、hook、connector 还是 agent。
- 写出声明、加载、模型可见、执行、事件回传、失败处理路径。
- 明确是否需要 approval、sandbox、network 或 auth。

评分要点：

- 不把 skill 当成任意代码执行。
- 不把 plugin 当成单一工具。
- MCP/tool 结果有事件和审计字段。
- 失败路径不会绕过 Core。

## 5. 完成记录

完成这些题目后，读者应回到 [expert-checklist.md](expert-checklist.md) 做最终自测。
