## Context

`add-codex-core-module-doc-plan` 已完成 core 层文档规划，定义了 `docs/core/README.md`、专题拆分、逐模块覆盖矩阵和 core 模块地图。当前 change 将规划变成可阅读的第一版文档集。

文档需要面向初学者，但不能停留在概念介绍。每篇都必须从“如果我自己设计这个模块，要先解决什么问题”入手，再连接到源码中的真实抽象和调用链。

## Goals / Non-Goals

**Goals:**

- 产出 core 层专题文档集，覆盖 `docs/core/README.md` 规划中的全部专题。
- 每篇文档提供源码锚点、主流程、边界条件、设计推导、练习题和后续深入点。
- 每篇文档至少引用一张 `image/core/*.svg` 图示。
- 保持图示清晰，优先 SVG，遵循项目图片质量约束。
- 更新索引和 OpenSpec tasks 到完成态。

**Non-Goals:**

- 不修改 `repo/codex/` 上游源码。
- 不追求逐函数逐行讲解。
- 不运行大型 Rust 测试。
- 不把 core 之外的 CLI/TUI/app-server/protocol 作为完整专题展开；只在解释 core 边界时引用。

## Decisions

### D1: 第一版文档以“可复设计”为完成口径

每篇文档不只是说明源码在哪里，而要包含：

- 模块解决的问题。
- 核心抽象和边界。
- 主流程。
- 失败模式。
- 如果自己重新设计，需要做出的关键决策。
- 检查题。

### D2: 每篇文档使用一张主图

每篇专题至少有一张 SVG 主图，表达核心结构、生命周期或决策链。复杂专题后续可以追加多张图，但本轮先保证全覆盖。

### D3: 先全覆盖，再精修深挖

本轮目标是第一版完整知识库：每篇有足够结构和源码锚点，能指导后续深读。更细的逐函数分析、实验和源码引用行号精修可以在后续专题迭代中完成。

## Risks / Trade-offs

- 15 篇文档一次性产出可能深度不均 → 用统一模板和验收清单保证最低质量，并在 Follow-up Slots 标出后续加深点。
- SVG 数量较多 → 统一放在 `image/core/`，并在 `image/core/README.md` 汇总。
- 源码持续变化 → 每篇引用 `docs/source-snapshot.md`，并以当前本地快照为基线。

## Validation

- `docs/core/01-thread-lifecycle.md` 到 `docs/core/14-observability-utilities.md` 以及 `docs/core/00-core-map.md` 存在。
- 每篇专题文档包含源码锚点和至少一张 `image/core/*.svg` 引用。
- `image/core/*.svg` 可被 XML parser 解析。
- `openspec validate implement-codex-core-docs --strict` 通过。
