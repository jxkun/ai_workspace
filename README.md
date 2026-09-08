# AI Workspace

这是一个用于沉淀 AI 学习、实验、项目和 Agent 协作约定的个人工作空间。

这里不是单一应用仓库，而是一个 workspace：不同主题可以放在不同子项目中，公共资料、路线图和协作规则放在根目录统一管理。

## 目录结构

```text
.
├── AGENTS.md                 # 根目录 Agent 协作约定
├── README.md                 # Workspace 总览
├── docs/                     # 跨项目文档、学习路线和资料沉淀
├── project/                  # 具体 AI 项目或学习工程
└── repo/                     # 外部仓库、实验仓库或待研究代码
```

## 当前内容

### `docs/`

存放跨项目的文档和学习路线。

- `docs/langchain/langchain-learning-roadmap.md`：LangChain 系统学习路线。

### `project/`

存放可以独立运行、独立演进的项目。

- `project/learn_llm/`：Python LLM Agent 学习空间，包含示例、Prompt、配置、Notebook、测试和 Agent 设计记录。
- `project/saya/`：预留项目目录。

### `repo/`

用于放置外部源码、临时研究仓库或需要单独追踪的代码副本。

如果某个目录本身已经是独立 Git 仓库，尽量不要把它和根 workspace 的提交历史混在一起；必要时在根 `.gitignore` 或文档里明确说明。

## 使用方式

### 新增学习文档

跨项目通用资料放到 `docs/<topic>/` 下，例如：

```text
docs/langchain/
docs/langgraph/
docs/rag/
docs/prompt-engineering/
```

如果文档只服务于某个子项目，优先放到该项目自己的 `docs/` 目录。

### 新增项目

新项目放到 `project/<project_name>/`，建议至少包含：

```text
project/<project_name>/
├── README.md
├── AGENTS.md
├── docs/
├── examples/
├── scripts/
├── src/
└── tests/
```

不是每个项目都必须一次性建全所有目录；先保证 README 写清楚目标、运行方式和边界，再随着项目演进补齐。

### 新增实验代码

- 短期探索可以放在对应项目的 `notebooks/`、`examples/` 或 `scripts/`。
- 会被复用的逻辑应移动到项目的 `src/`。
- 可重复验证的行为应补到项目的 `tests/`。

## 工作原则

- 默认使用中文记录说明、设计和协作信息。
- 代码、库名、API、命令和配置键保持原文。
- 每个子项目尽量自包含：自己的 README、依赖、运行方式和 Agent 约定放在项目内。
- 根目录只放跨项目规则和索引，不承载具体项目的大量实现细节。
- 不提交真实 API Key、私有 Token、生产数据或大体积生成物。
- 对 AI Agent 相关实验，优先沉淀可复现步骤、输入输出样例、失败案例和取舍记录。

## Git 远端

当前 workspace 已关联远端：

```bash
git@github.com:starry-night-pro/ai_workspace.git
```

首次提交前建议检查：

```bash
git status
git remote -v
```
