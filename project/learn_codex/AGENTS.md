# learn_codex Agent 协作规则

本目录用于学习和分析 `openai/codex` harness。所有工作应围绕本项目的源码快照、分析文档、图像资产和 OpenSpec 进行，不向其它 `project/` 子目录扩散。

## 工作语言

- 默认使用中文沟通和编写文档。
- 引用源码符号、文件路径、命令和配置键时保留原文。

## 源码分析原则

- 以 `repo/codex/` 的实际代码为第一事实来源。
- 任何架构判断必须给出源码锚点，至少包含文件路径；关键结论应尽量补充函数、类型、测试或协议文件。
- 不直接修改 `repo/codex/` 中的上游源码，除非用户明确要求做实验性 patch。
- 如果更新源码快照，必须同步更新 `docs/source-snapshot.md`。

## 文档与图片约束

- 主要分析成果放在 `docs/`。
- Markdown 文档可以写列表、表格和源码引用，但最终流程图、架构图、状态图必须使用生成的图片。
- 图片统一放在 `image/`，并按文档或主题分子目录，例如 `image/methodology/`、`image/architecture/`。
- 文档引用图片时使用相对路径，例如 `../image/architecture/runtime-loop.png`。
- 不把 Mermaid、PlantUML、ASCII 流程图作为最终图示交付；如需用 DSL 生成图片，DSL 源文件也应和导出的图片一起放入对应 `image/` 子目录。
- 正式文档最终引用 PNG 图，SVG 作为可编辑源文件保留在同一目录；PNG 必须从 SVG 或高分辨率画布导出，保证文字清晰、线条稳定、无明显像素感或锯齿。
- 图片应采用清晰层级、充足留白、统一字体、柔和线条和稳定配色；如果用户指出观感问题，优先新增更高质量版本并更新文档引用，旧图可保留作历史兼容。

## OpenSpec 约束

- 本项目的需求和阶段任务优先沉淀到 `openspec/changes/`。
- 当前初始化 change 是 `setup-codex-harness-study`。
- 修改项目结构、分析方法论或长期任务拆分时，应先更新对应 OpenSpec，再更新文档。

## 验证要求

- 文档类变更至少检查路径、链接和 OpenSpec 校验。
- 与源码分析有关的结论要能回到 `repo/codex/` 的具体文件复查。
- 示例或脚本引入新依赖时，同步更新 README 或对应文档。
