# Entry 层文档索引

本目录解释 Codex harness 的入口层：用户、终端 UI、非交互 CLI、远程 app-server 客户端如何把请求送进同一套 Core thread / turn 边界。它回答“请求从哪里来、入口层负责什么、什么时候必须交给 `codex-core`”。

本文档集基于源码快照 `repo/codex/`，版本见 [../source-snapshot.md](../source-snapshot.md)。

## 当前文档

- [00-entry-map.md](00-entry-map.md)：Entry 层总览，覆盖 CLI、TUI、app-server、app-server-protocol 与 turn request processor 的边界。
- [01-cli-tui-app-server-flow.md](01-cli-tui-app-server-flow.md)：深入展开 CLI dispatch、TUI `AppServerSession`、app-server `thread/start` / `turn/start` 到 Core 的入口链路。
- [02-cli-command-surface.md](02-cli-command-surface.md)：拆分 CLI 命令面，解释 `Subcommand`、root config overrides、remote/worktree guard 和 `exec` headless 初始操作。
- [03-tui-thread-event-routing.md](03-tui-thread-event-routing.md)：拆分 TUI 线程事件路由，解释 `ChatWidget` 输入、`AppServerSession`、`ThreadEventChannel`、active/side thread 和 failover。
- [04-app-server-json-rpc-control-plane.md](04-app-server-json-rpc-control-plane.md)：拆分 app-server JSON-RPC 控制面，解释 typed `ClientRequest`、initialize gate、serialization scope 和 processor dispatch。

## 源码入口

- `repo/codex/codex-rs/cli/src/main.rs`：顶层 `codex` 命令分发，决定进入 TUI、`exec`、`review`、app-server 等路径。
- `repo/codex/codex-rs/tui/src/app.rs`：TUI 的应用状态、线程事件通道、交互状态和 app-server session 协调。
- `repo/codex/codex-rs/app-server/src/message_processor.rs`：JSON-RPC `ClientRequest` 的统一分发点。
- `repo/codex/codex-rs/app-server/src/request_processors/thread_processor.rs`：线程 start/resume/fork/read/list 等请求的 host-side 处理。
- `repo/codex/codex-rs/app-server/src/request_processors/turn_processor.rs`：`turn/start` 输入校验、环境覆盖、settings override 和 `CodexThread` 提交。
- `repo/codex/codex-rs/app-server-protocol/src/protocol/v2/thread.rs`：app-server 线程 API 的 wire shape。

## 阅读顺序

1. 先读 [00-entry-map.md](00-entry-map.md)，建立 CLI/TUI/app-server 都汇入 core thread 的模型。
2. 再读 [01-cli-tui-app-server-flow.md](01-cli-tui-app-server-flow.md)，复盘一次入口请求如何变成 `ThreadManager` / `CodexThread` 操作。
3. 按兴趣拆读 [02-cli-command-surface.md](02-cli-command-surface.md)、[03-tui-thread-event-routing.md](03-tui-thread-event-routing.md)、[04-app-server-json-rpc-control-plane.md](04-app-server-json-rpc-control-plane.md)。
4. 再回到 `docs/core/00-core-map.md` 和 `docs/core/01-thread-lifecycle.md`，把入口层交出的 `ThreadManager` / `CodexThread` 继续向下追。

## 当前成熟度

| 层级 | 状态 |
| --- | --- |
| Skeleton | 已有入口索引和总览文档。 |
| Guided reading | 已有总览、入口链路 deep-dive，以及 CLI/TUI/app-server 三个分部专题，包含源码锚点、开篇 PNG、主流程和代码证据。 |
| Harness-level | Entry 层主要入口面已可复盘；remote-control daemon 和 app-server protocol export 仍可继续拆专题。 |
