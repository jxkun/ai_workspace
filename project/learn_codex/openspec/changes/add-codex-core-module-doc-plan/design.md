## Context

`codex-rs/core` 是 Codex harness 的 runtime kernel。`core/src/lib.rs` 暴露了大量模块，既有核心会话/turn，也有工具、安全、配置、MCP、插件、压缩、上下文和持久化支撑。如果直接要求“每个文件一篇文档”，会产生大量低价值文档，初学者也无法把它们组织成可设计的系统模型。

本次设计采用“模块覆盖 + 专题聚类”的方式：覆盖 `core/src` 的主要模块，但按职责聚合成少量高价值专题，每个专题都要求能解释设计动机、关键数据结构、调用链、失败模式和复设计练习。

## Goals / Non-Goals

**Goals:**

- 规划一套覆盖 `codex-rs/core` 主要模块的文档体系。
- 每个规划项都能指导后续产出“专家给小白讲”的深度文档。
- 每个规划项都绑定源码锚点、关键问题、图示要求和完成标准。
- 生成一张 core 模块地图 SVG，帮助理解模块依赖和阅读顺序。
- OpenSpec tasks 全部闭环。

**Non-Goals:**

- 不在本次写完所有 core 模块深度正文。
- 不修改 `repo/codex` 上游源码。
- 不把 Entry/TUI/app-server、protocol crate、rollout crate、extension crate 作为本次完整展开对象；它们只作为 core 边界和依赖被引用。

## Decisions

### D1: 按职责聚类覆盖模块

规划文档按以下专题聚类：

1. Core 总览与模块地图。
2. ThreadManager 与 CodexThread。
3. Session / Turn / Task 主循环。
4. Context / ContextManager / WorldState。
5. Tools / Tool Router / Tool Runtime。
6. Exec / UnifiedExec / Shell。
7. Safety / Sandbox / Approval。
8. ApplyPatch。
9. Config / Environment / Model Client。
10. MCP / Connectors / Plugins / Skills。
11. Agents / Multi-agent / Spawn。
12. Rollout / Compaction / Resume。
13. Guardian / Review / Attestation。
14. Realtime / Voice / Apps / Images。
15. Observability / Timing / Metadata / Utilities。

这种聚类能覆盖 `core/src/lib.rs` 中的主要模块，同时避免逐文件文档造成割裂。

### D2: 每篇专题必须让读者具备“复设计能力”

每篇后续文档不只解释“代码做了什么”，还要回答：

- 如果自己设计这个模块，要解决哪些问题？
- 核心抽象为什么这样切？
- 输入、状态、输出分别是什么？
- 错误、权限、并发、恢复和边界条件如何处理？
- 哪些测试证明设计成立？

### D3: 图片是每篇专题的必选规划项

规划文档只生成一张 core 总览图。后续每篇专题如果涉及流程、架构、状态或时序，必须在规划中声明需要的图片，并放入 `image/core/` 或更细子目录。

### D4: 以源码锚点约束规划质量

每个规划项都要至少列出代表性源码路径；不能只有概念标题。源码锚点优先来自：

- `repo/codex/codex-rs/core/src/lib.rs`
- `repo/codex/codex-rs/core/src/<module>.rs`
- `repo/codex/codex-rs/core/src/<module>/`
- 对应 `*_tests.rs` 或 `tests/`

## Risks / Trade-offs

- 覆盖所有文件会导致规划过重 → 采用职责聚类，文档规划覆盖主要模块，细小 helper 放入所属专题。
- 聚类可能遗漏边缘模块 → 在每个专题中设置“覆盖模块”字段，并用 `core/src/lib.rs` 做回查。
- 小白读不懂核心术语 → 每篇专题要求从“要解决的问题”开始，而不是从类型定义开始。
- 图片质量下降 → 优先 SVG，遵守项目图片质量约束。

## Validation

- `docs/core/README.md` 存在。
- `docs/core/README.md` 覆盖 core 层主要模块聚类、文档清单、阅读顺序和验收标准。
- `image/core/codex-core-module-map-v1.svg` 存在且可解析。
- `docs/index.md` 链接 core 层文档规划。
- `openspec validate add-codex-core-module-doc-plan --strict` 通过。
