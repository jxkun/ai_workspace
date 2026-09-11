# Extension 层文档索引

本目录解释 Codex harness 的扩展层：skills、plugins、MCP、hooks 和 connectors 如何把外部能力声明、装载、过滤、暴露和执行到 Core runtime。

本文档集基于源码快照 `repo/codex/`，版本见 [../source-snapshot.md](../source-snapshot.md)。

## 当前文档

- [00-extension-map.md](00-extension-map.md)：Extension 层总览，覆盖 skill metadata、plugin manifest、core-plugins manager、MCP runtime、hook dispatcher 和 connector runtime projection。
- [01-skills-plugins-mcp-hooks.md](01-skills-plugins-mcp-hooks.md)：深入展开 skill 选择、plugin bundle、MCP binding / prepared call、hook payload / result 和 connector projection 的扩展链路。

## 源码入口

- `repo/codex/codex-rs/skills/src/model.rs`、`repo/codex/codex-rs/skills/src/parser.rs`：skill 元数据和 `SKILL.md` frontmatter 解析。
- `repo/codex/codex-rs/plugin/src/manifest.rs`：插件 manifest 的通用结构。
- `repo/codex/codex-rs/core-plugins/src/manifest.rs`、`repo/codex/codex-rs/core-plugins/src/manager.rs`：插件加载、marketplace、remote sync、能力汇总。
- `repo/codex/codex-rs/codex-mcp/src/runtime.rs`、`repo/codex/codex-rs/codex-mcp/src/lib.rs`：线程级 MCP runtime、tool catalog 和 resource/event 能力。
- `repo/codex/codex-rs/hooks/src/types.rs`、`repo/codex/codex-rs/hooks/src/engine/dispatcher.rs`：hook payload、handler 选择和执行。
- `repo/codex/codex-rs/connectors/src/runtime_projection.rs`：connector tool runtime 投影为 installed app state。

## 阅读顺序

1. 先读 [00-extension-map.md](00-extension-map.md)，理解扩展能力如何分成声明、装载、运行时、拦截和投影五类。
2. 再读 [01-skills-plugins-mcp-hooks.md](01-skills-plugins-mcp-hooks.md)，复盘一个扩展能力如何从 skill/plugin 声明进入 MCP/tool/hook/connector 边界。
3. 再读 `docs/core/09-extensions-inside-core.md`，看这些扩展如何进入 Core 的 context 和 tool runtime。

## 当前成熟度

| 层级 | 状态 |
| --- | --- |
| Skeleton | 已有扩展层索引和总览文档。 |
| Guided reading | 已有总览和扩展链路 deep-dive，覆盖声明、选择、MCP binding、hook 执行和 connector projection 的源码锚点与代码证据。 |
| Harness-level | Skills / plugins / MCP / hooks / connectors 基础链路已可复盘；plugin marketplace、MCP auth/elicitation、hook schema 和 connector policy 可继续拆专题。 |
