# learn_llm

Python LLM Agent 学习空间。

这个仓库用于循序渐进地学习和搭建 LLM Agent：先从基础 Prompt、模型调用、工具调用开始，再进入 LangChain、LangGraph、记忆、RAG、评估，以及可落地的 Agent 应用。

## 目标

- 用小而可运行的例子学习概念，而不是只停留在阅读文档。
- 不同框架的实验彼此隔离，方便对比 LangChain、LangGraph 和原生 SDK 的差异。
- 沉淀可复用的 Prompt、Agent 模式、评估记录和实现决策。
- 从 Notebook 和脚本逐步演进到可测试、可复用的 Python 模块。
- 默认使用中文记录学习笔记、设计说明和协作说明。

## 目录结构

```text
.
├── AGENTS.md                 # AI 编程 Agent 协作约定
├── README.md                 # 项目总览
├── agents/                   # Agent 设计、实验和运行入口
├── configs/                  # 本地配置模板、模型配置、环境变量示例
├── data/
│   ├── raw/                  # 原始样例数据或文档
│   └── processed/            # 示例或测试使用的处理后数据
├── docs/
│   └── roadmap.md            # 总学习路线和阶段规划
├── examples/
│   ├── langchain/            # LangChain 专项示例
│   └── langgraph/            # LangGraph 专项示例
├── notebooks/                # 探索性 Notebook
├── prompts/                  # Prompt 模板和 Prompt 笔记
├── scripts/                  # 本地辅助脚本
├── src/
│   └── learn_llm/            # 可复用 Python 包代码
└── tests/                    # 单元测试和回归测试
```

## 目录说明

### `agents/`

存放 Agent 级别的实验和设计。

适合放完整的 Agent 方案，例如手写 ReAct Agent、LangChain Agent、LangGraph 工作流 Agent。每个 Agent 可以独立维护 `README.md`、`design.md`、`run.py` 和评估记录。

不要把通用框架工具代码放在这里。某个模式稳定后，再把可复用部分沉到 `src/learn_llm/`。

### `configs/`

存放安全的配置模板。

适合放 `.env.example`、模型配置示例、模型供应商路由示例、本地实验配置。真实密钥只放在本地环境变量或未追踪的 `.env` 文件里。

### `data/raw/`

存放原始样例数据。

适合放小型本地文档、玩具数据集、Prompt 输入样例、RAG 示例使用的测试文件。数据应保持小规模且不包含敏感信息。

### `data/processed/`

存放从 `data/raw/` 派生出来的数据。

适合放分块后的文档、临时向量库导出、清洗后的数据集、预处理缓存结果。这里的内容原则上应能从原始数据或脚本重新生成。

### `docs/`

存放学习笔记和项目级文档。

适合放学习路线、概念笔记、设计决策、框架对比、调试记录和架构说明。如果一份文档解释了“为什么这样设计”，就应该放在这里。

### `examples/`

存放可运行的学习示例。

每个示例应聚焦一个概念，并且容易运行。优先写命名清晰的小脚本，不要一开始就写成混杂的大 Demo。当某个 Demo 演进成可复用 Agent 时，把设计记录移动到 `agents/`，共享代码移动到 `src/learn_llm/`。

### `examples/langchain/`

存放 LangChain 专项示例。

适合放 Chat Model 调用、Prompt 模板、Tools、Runnables、Chains、Agents、Retrieval Chains 和 LangChain 评估实验。

### `examples/langgraph/`

存放 LangGraph 专项示例。

适合放图状态、节点、条件边、Checkpoint、Interrupt、人工审批流程和多 Agent 图工作流。

### `notebooks/`

存放探索性 Notebook。

适合做快速实验、可视化、API 行为验证和思路验证。如果 Notebook 中的逻辑变得有用且可复用，应抽取到 `examples/` 或 `src/learn_llm/`。

### `prompts/`

存放可复用 Prompt 资产。

适合放 System Prompt、Prompt 模板、Prompt 版本对比、输出结构说明和 Prompt 行为记录。多个示例共用的 Prompt 应放在这里，而不是复制到各个脚本里。

### `scripts/`

存放本地辅助脚本。

适合放环境初始化、数据预处理、一次性转换、本地评估运行器或维护命令。会被示例或测试导入的代码，应放到 `src/learn_llm/`，不要放在这里。

### `src/learn_llm/`

存放可复用 Python 包代码。

适合放稳定工具函数、共享模型适配器、工具注册器、状态定义、Trace 辅助、RAG 工具和评估辅助代码。这里的代码可以理解框架，但不要被单个 Demo 绑死；能跨示例复用的逻辑优先沉淀到这里。

### `tests/`

存放可复用代码和关键行为的测试。

适合放单元测试、回归测试、解析器测试、工具调用行为检查和评估框架测试。优先覆盖共享代码、状态流转和手动调试成本高的逻辑。

## 学习路线

1. **Python LLM 基础**
   - Chat Completion 调用
   - Prompt 模板
   - 流式输出
   - Tool / Function Calling

2. **Agent 基础**
   - ReAct 循环
   - 工具注册
   - Agent 状态
   - 错误处理和重试策略

3. **LangChain**
   - Chat Models 和 Messages
   - Tools
   - Runnables
   - 简单 Agent
   - Retrieval Chains

4. **LangGraph**
   - 图状态
   - 节点和边
   - 条件路由
   - Human-in-the-loop Checkpoint
   - 多 Agent 工作流

5. **RAG 和记忆**
   - 文档加载
   - 文档分块
   - Embeddings
   - 向量库
   - 对话记忆

6. **评估和可观测性**
   - Golden Test Cases
   - Trace 日志
   - Tool Call 断言
   - 回归检查

7. **Agent 应用化**
   - CLI agent
   - 本地 Web / API 服务
   - 工作流自动化
   - 部署记录

## Notebook 环境

当前项目已初始化项目内 Notebook kernel：

- 虚拟环境：`.venv`
- Python：3.11
- Kernel 显示名：`Python (learn_llm)`
- 说明文档：[docs/notebook-setup.md](./docs/notebook-setup.md)

打开 Notebook 时，选择 `Python (learn_llm)` 作为内核。可以先运行 [notebooks/00_smoke_test.ipynb](./notebooks/00_smoke_test.ipynb) 验证环境。

## 当前状态

当前是一个初始化后的学习骨架。下一步比较适合补充 Python 环境配置文件，以及 `examples/` 下的第一个最小可运行示例。

