# Support 层文档索引

本目录解释 Codex harness 的支撑层：协议类型、上下文片段、rollout JSONL、thread store 和 memory extension 如何让 Core runtime 能跨 turn、跨恢复、跨客户端维持一致状态。

本文档集基于源码快照 `repo/codex/`，版本见 [../source-snapshot.md](../source-snapshot.md)。

## 当前文档

- [00-support-map.md](00-support-map.md)：Support 层总览，覆盖 `protocol`、`history`、`rollout`、`thread-store`、`context-fragments`、`ext/memories` 的职责边界。
- [01-protocol-rollout-thread-store.md](01-protocol-rollout-thread-store.md)：深入展开 `Submission` / `Op` / `EventMsg`、`RolloutItem`、rollout JSONL、`ThreadStore`、context fragment 和 memory extension 的支撑链路。

## 源码入口

- `repo/codex/codex-rs/protocol/src/protocol.rs`：Core SQ/EQ 协议、事件、submission、context tags。
- `repo/codex/codex-rs/history/src/lib.rs`：模型历史和 rollout 持久化领域类型。
- `repo/codex/codex-rs/rollout/src/lib.rs`、`repo/codex/codex-rs/rollout/src/recorder.rs`：JSONL rollout 解析、记录、压缩、搜索和恢复辅助。
- `repo/codex/codex-rs/thread-store/src/store.rs`：storage-neutral thread persistence trait。
- `repo/codex/codex-rs/context-fragments/src/fragment.rs`：模型上下文片段渲染和 metadata passthrough。
- `repo/codex/codex-rs/ext/memories/src/extension.rs`：memory prompt/context/tools 对 Core extension registry 的贡献。

## 阅读顺序

1. 先读 [00-support-map.md](00-support-map.md)，理解 Support 层不是“杂工具”，而是 Core 的状态、协议和恢复基座。
2. 再读 [01-protocol-rollout-thread-store.md](01-protocol-rollout-thread-store.md)，把输入协议、事件、rollout、thread-store 和 context fragment 串成一条可恢复链路。
3. 再读 `docs/core/03-context-world-state.md` 与 `docs/core/11-rollout-compaction-resume.md`，把支撑类型如何被 Core 调用串起来。

## 当前成熟度

| 层级 | 状态 |
| --- | --- |
| Skeleton | 已有支撑层索引和总览文档。 |
| Guided reading | 已有总览和支撑链路 deep-dive，覆盖协议、持久化、上下文和 memory 的源码锚点与代码证据。 |
| Harness-level | Protocol / rollout / thread-store / context 基础链路已可复盘；rollout 搜索、thread-store 本地实现和 memory read/write pipeline 可继续拆专题。 |
