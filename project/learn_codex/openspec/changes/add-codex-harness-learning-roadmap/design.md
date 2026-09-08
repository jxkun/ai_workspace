## Context

当前项目已有：

- `repo/codex/`：`openai/codex` 本地源码快照。
- `docs/methodology.md`：通用分析方法论。
- `docs/source-snapshot.md`：源码版本锚点。
- `image/`：图片资产根目录和图示规范。

用户现在需要“先拆解一下 Codex harness 的学习思路和路线全景”，受众是小白，但要求以专家视角系统拆解。因此路线文档需要兼顾两个目标：对初学者足够可读，对后续深入分析足够可执行。

## Goals / Non-Goals

**Goals:**

- 用一份路线文档解释 Codex harness 应该怎么学、先看什么、后看什么。
- 将源码目录映射到 Entry、Core、Support、Extension 四层模型。
- 每个阶段给出目标、源码入口、关键问题、产出、完成标准。
- 生成至少一张可视化图片，帮助读者建立全局心智模型。
- 保持本轮范围为“路线全景拆解”，不提前展开所有专题正文。

**Non-Goals:**

- 不修改 `repo/codex/`。
- 不完成 runtime loop、tool sandbox、memory 等专题的深度正文。
- 不把路线写成 Codex CLI 用户使用教程。
- 不用 Mermaid 或 ASCII 图作为最终图示。

## Decisions

### D1: 用四层模型组织路线

路线采用 Entry、Core、Support、Extension 四层模型：

- Entry：CLI、TUI、app-server 等用户和客户端入口。
- Core：session、turn、tasks、model/tool orchestration 等核心运行循环。
- Support：protocol、rollout、thread store、context fragments、config、history、memory 等支撑系统。
- Extension：tools、sandboxing、MCP、skills、plugins、hooks 等扩展与安全边界。

这样能让小白先看到系统边界，再逐步深入关键链路。

### D2: 采用 7 阶段学习路线

路线按“建立地图 → 理解一次 turn → 理解工具与权限 → 理解持久化与恢复 → 理解扩展点 → 做案例复盘 → 做小实验”的顺序推进。这样比按目录逐个读更适合初学者，因为每阶段都有明确问题和完成标准。

### D3: 文档中只放路线图和源码入口，不展开完整专题正文

本轮交付是路线全景，后续专题文档应由单独 change 或任务继续推进。路线文档可以列出未来文件名，但不应填充大量未验证结论。

### D4: 至少提供两张图片

为了满足可视化要求，本次生成并优先引用矢量版图片：

- `image/learning-roadmap/codex-harness-roadmap-v2.svg`：学习阶段全景，当前推荐版本。
- `image/learning-roadmap/codex-harness-layer-map-v2.svg`：四层源码地图，当前推荐版本。

Markdown 文档引用这些图片；不使用 Mermaid 或 ASCII 图作为最终图示。

## Risks / Trade-offs

- 小白路线过细会过载 → 每阶段只列核心源码入口和关键问题，细节留给专题文档。
- 路线过浅会失去专家价值 → 每阶段都绑定源码目录和具体产出。
- 上游源码快速变化 → 路线文档引用 `docs/source-snapshot.md`，后续更新源码时复核路径。
- 图片生成工具链未统一 → 本轮生成 PNG，后续可补脚本化生成流程。

## Validation

- `docs/codex-harness-learning-roadmap.md` 存在并引用 `image/learning-roadmap/` 下图片。
- 图片文件存在且为有效 SVG；早期 PNG 仅作兼容参考。
- 路线文档不包含 Mermaid/PlantUML/ASCII 作为最终图示。
- OpenSpec strict validate 通过。
