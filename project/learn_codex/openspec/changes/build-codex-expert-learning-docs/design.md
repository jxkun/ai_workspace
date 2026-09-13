## Context

`learn_codex` 目前已有四层源码导读：

- Entry: `docs/entry/`
- Core: `docs/core/`
- Support: `docs/support/`
- Extension: `docs/extension/`

这些文档适合按模块深读，但初学者还需要一个课程化路径：先建立全局模型，再沿一次请求理解主循环，随后拆解高风险工具执行、长期状态恢复和扩展能力接入，最后用练习确认是否真正掌握。

## Goals / Non-Goals

**Goals:**

- 建立 `docs/expert-learning/` 作为“小白到专家”的学习入口。
- 用 5 篇课程文档串联现有四层导读，不复制所有细节，但给出足够源码证据和运行链路。
- 每篇课程都有本地 PNG 开篇图、源码锚点、代码片段、行为证据矩阵、失败边界、检查题答案。
- 增加练习集和专家验收清单，使读者能验证自己是否具备源码定位、流程复盘、故障诊断和重设计能力。
- 增加项目级校验脚本，防止专家学习目录退化成普通链接列表。

**Non-Goals:**

- 不重写现有 `docs/core` / `docs/entry` / `docs/support` / `docs/extension` 全部内容。
- 不逐文件覆盖 `repo/codex/codex-rs` 所有 crate。
- 不修改上游源码。
- 不做实验性 patch 或运行 Codex harness。

## Decisions

### D1: 专家教材只做主路径课程，不替代模块文档

`docs/expert-learning/` 负责把读者带过专家理解路径，深层模块细节仍链接到现有四层文档。这样避免重复维护两套完整专题，同时给初学者一个更顺滑的阅读顺序。

### D2: 五篇核心课程固定为学习主干

课程顺序固定为：

1. `01-global-model.md`
2. `02-core-runtime-loop.md`
3. `03-tools-safety-patch.md`
4. `04-state-protocol-memory.md`
5. `05-extension-system.md`

这个顺序对应“先看系统，再看主循环，再看动作边界，再看长期状态，最后看扩展定制”。

### D3: 练习和验收是正式交付，不是 follow-up

`exercises.md` 和 `expert-checklist.md` 是本 change 的完成条件。每道练习都要有答案要点，否则文档无法证明读者是否从小白走到专家口径。

### D4: 图像采用手写 SVG + rsvg 导出 PNG

新增图都放在 `image/expert-learning/`，Markdown 引用 PNG，保留同名 SVG。图像表达源码链路和职责边界，不使用 Mermaid、PlantUML 或 ASCII 图作为最终交付。

## Validation

- `python3 scripts/check_expert_learning_docs.py`
- `python3 /data00/home/jiangxukun/.trae/skills/source-study-docs/scripts/check_source_study_docs.py --docs-dir docs/expert-learning --source-root repo/codex --image-root image/expert-learning --complete`
- `python3 scripts/check_core_docs.py`
- `python3 scripts/check_non_core_docs.py`
- `openspec validate build-codex-expert-learning-docs --strict`
