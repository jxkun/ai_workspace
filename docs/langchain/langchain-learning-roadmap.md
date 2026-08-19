# LangChain 学习路线

## 目标定位

这份路线面向已经具备 Python 基础、了解大模型基本调用方式，并希望系统掌握 LangChain 应用开发的人。学习目标不是记 API，而是能够独立设计、开发、调试和维护基于大模型的真实应用。

完成后应具备以下能力：

- 理解 LangChain 的核心抽象：Model、Prompt、Output Parser、Retriever、Tool、Agent、Memory、Graph。
- 能用 LCEL 组合稳定、可测试的调用链。
- 能构建 RAG、工具调用、多轮对话、Agent 工作流等常见应用。
- 能通过 LangSmith 或日志手段定位链路问题、评估效果和优化成本。
- 能判断什么时候应该使用 LangChain，什么时候应该直接使用模型 SDK 或更轻量的封装。

## 前置基础

建议先补齐这些基础，否则学习 LangChain 时容易只停留在“会跑 Demo”：

- Python：函数、类、类型标注、异步编程、虚拟环境、依赖管理。
- LLM 基础：Chat Model、Completion、Token、Temperature、Top-p、Function Calling、Structured Output。
- Prompt 基础：角色消息、上下文窗口、Few-shot、约束输出、失败重试。
- Web/API 基础：HTTP、JSON、鉴权、超时、重试、流式响应。
- 向量检索基础：Embedding、向量数据库、相似度搜索、召回、重排。

## 阶段一：理解 LangChain 的定位

### 学习重点

- LangChain 解决什么问题：编排、连接、抽象、观测、复用。
- LangChain 不解决什么问题：模型能力本身、业务正确性、数据质量、权限安全。
- LangChain 生态组成：
  - `langchain-core`：基础接口和 LCEL。
  - `langchain`：常用链、Agent、工具集。
  - `langchain-community`：社区集成。
  - `langchain-openai` 等 provider 包：模型厂商适配。
  - LangSmith：调试、追踪、评估。
  - LangGraph：复杂状态机和多 Agent 流程。

### 推荐产出

- 写一页笔记：LangChain 和直接调用模型 SDK 的区别。
- 跑通一个最小 Chat Model 调用。
- 明确本地项目的依赖安装方式和环境变量管理方式。

## 阶段二：掌握 LCEL 和基础链路

LCEL 是 LangChain 现代用法的核心，建议优先学习。

### 学习重点

- `Runnable` 抽象。
- `prompt | model | parser` 的管道式组合。
- `invoke`、`batch`、`stream`、`ainvoke`。
- `RunnablePassthrough`、`RunnableLambda`、`RunnableParallel`。
- 链路输入输出结构设计。
- 错误处理、超时、重试、fallback。

### 练习任务

1. 构建一个“文本总结”链：
   - 输入：长文本。
   - 输出：结构化摘要、关键点、待办事项。

2. 构建一个“分类器”链：
   - 输入：用户问题。
   - 输出：意图类型、置信度、原因。

3. 构建一个“路由”链：
   - 按意图分发到不同 prompt。
   - 对不可识别意图返回兜底答案。

### 推荐产出

- `examples/basic_chain.py`
- `examples/router_chain.py`
- 一份链路输入输出约定说明。

## 阶段三：Prompt 和结构化输出

### 学习重点

- `ChatPromptTemplate`。
- System / Human / AI Message 的职责划分。
- Prompt 变量、模板复用、局部变量绑定。
- Output Parser。
- Pydantic 结构化输出。
- JSON 输出失败时的修复和重试策略。
- Prompt 版本管理。

### 练习任务

1. 设计一个结构化信息抽取链：
   - 从自然语言中抽取姓名、时间、地点、事项、优先级。

2. 设计一个业务规则校验链：
   - 输入用户提交内容。
   - 输出是否通过、失败原因、修复建议。

3. 对同一个任务设计 3 个 prompt 版本并比较效果。

### 推荐产出

- `examples/structured_output.py`
- `prompts/` 目录，保存可复用 prompt。
- 一份 prompt 评测记录。

## 阶段四：RAG 基础

RAG 是 LangChain 最常见的落地场景，建议重点投入。

### 学习重点

- 文档加载：Loader。
- 文档切分：Text Splitter。
- Embedding 模型选择。
- Vector Store 接入。
- Retriever 抽象。
- Query 改写。
- Context 拼接。
- 引用来源返回。
- 检索失败兜底。

### 练习任务

1. 构建一个本地知识库问答：
   - 输入 Markdown 文档。
   - 切分、向量化、检索。
   - 回答时附带来源。

2. 优化切分策略：
   - 比较固定长度切分、标题层级切分、语义切分。

3. 优化召回质量：
   - 调整 chunk size。
   - 调整 top-k。
   - 增加 query rewrite。
   - 增加 rerank。

### 推荐产出

- `examples/rag_local_docs.py`
- 一份 RAG 参数对比表。
- 一份“回答错误原因归因”记录。

## 阶段五：工具调用和 Agent

Agent 不应该作为第一选择。先掌握可控链路，再学习 Agent。

### 学习重点

- Tool 的定义方式。
- 工具输入 schema。
- 模型工具调用机制。
- Agent 执行循环。
- ReAct 思路。
- 工具权限和副作用控制。
- 工具调用失败处理。
- 最大迭代次数、超时、成本控制。

### 练习任务

1. 定义一个查询工具：
   - 输入关键词。
   - 返回模拟检索结果。

2. 定义一个计算工具：
   - 执行简单数学计算。
   - 校验非法表达式。

3. 构建一个多工具 Agent：
   - 能判断何时查资料、何时计算、何时直接回答。

### 推荐产出

- `examples/tools.py`
- `examples/agent_basic.py`
- 一份工具权限边界说明。

## 阶段六：Memory 和多轮对话

### 学习重点

- 对话历史的本质是上下文管理，不是永久记忆。
- 短期历史、长期记忆、用户画像的区别。
- History trimming。
- Summary memory。
- 基于检索的长期记忆。
- 会话隔离。
- 隐私和敏感信息处理。

### 练习任务

1. 构建一个多轮客服助手：
   - 保留最近 N 轮对话。
   - 能总结用户诉求。

2. 构建一个带长期记忆的助手：
   - 保存用户偏好。
   - 后续回答中可检索使用。

3. 增加记忆更新规则：
   - 只有明确偏好才写入。
   - 临时信息不写入长期记忆。

### 推荐产出

- `examples/chat_history.py`
- `examples/long_term_memory.py`
- 一份记忆写入规则文档。

## 阶段七：LangGraph 工作流

当应用从单链路变成多步骤、有状态、可恢复、可分支的流程时，再学习 LangGraph。

### 学习重点

- State。
- Node。
- Edge。
- Conditional Edge。
- Checkpoint。
- Human-in-the-loop。
- 多 Agent 协作。
- 流程中断和恢复。

### 练习任务

1. 构建一个内容审核流程：
   - 解析输入。
   - 检查风险。
   - 生成修改建议。
   - 必要时进入人工确认。

2. 构建一个研究助手：
   - 规划问题。
   - 检索资料。
   - 汇总答案。
   - 自检并修正。

3. 构建一个可恢复流程：
   - 中间状态落盘。
   - 失败后从上一步继续。

### 推荐产出

- `examples/langgraph_review_flow.py`
- `examples/langgraph_research_agent.py`
- 一张工作流状态图。

## 阶段八：观测、评估和生产化

### 学习重点

- LangSmith trace。
- 日志字段设计。
- 输入、输出、模型参数、耗时、token、错误信息记录。
- 数据集评估。
- 人工标注和自动评估。
- 回归测试。
- Prompt 变更评估。
- 成本控制。
- 限流、降级、重试、缓存。

### 练习任务

1. 给已有链路接入 trace。
2. 建立 20 条测试样例。
3. 比较两个 prompt 版本的准确率和稳定性。
4. 模拟模型失败、检索失败、工具失败并设计兜底。

### 推荐产出

- `evals/` 目录。
- 一份评估数据集。
- 一份线上化检查清单。

## 推荐学习顺序

建议按下面顺序推进：

1. 先跑通模型调用和最小链路。
2. 学会 LCEL，把链路写成可组合、可测试的结构。
3. 学结构化输出，保证应用能接入真实业务系统。
4. 学 RAG，完成一个本地知识库问答。
5. 学 Tool 和 Agent，但保持工具权限可控。
6. 学 Memory，明确短期上下文和长期记忆边界。
7. 学 LangGraph，用于复杂、有状态流程。
8. 学评估和观测，把 Demo 推向可维护应用。

## 实战项目建议

### 项目一：个人文档问答助手

功能：

- 读取本地 Markdown / PDF。
- 建立向量索引。
- 支持自然语言问答。
- 回答附带引用来源。
- 无依据时拒答。

重点能力：

- Loader。
- Splitter。
- Embedding。
- Retriever。
- RAG prompt。
- 来源追踪。

### 项目二：结构化信息抽取服务

功能：

- 输入自然语言需求。
- 输出结构化 JSON。
- 校验字段合法性。
- 支持失败重试。
- 支持人工修正后再提交。

重点能力：

- Prompt 设计。
- Pydantic schema。
- Output Parser。
- 错误修复。
- 业务字段校验。

### 项目三：带工具调用的任务助手

功能：

- 能查文档。
- 能做简单计算。
- 能调用内部 API 或本地模拟 API。
- 能解释调用结果。
- 能拒绝高风险操作。

重点能力：

- Tool schema。
- Agent。
- 权限控制。
- 执行轨迹。
- 失败兜底。

### 项目四：基于 LangGraph 的审批流助手

功能：

- 解析用户申请。
- 自动补全信息。
- 风险检查。
- 生成审批摘要。
- 人工确认后提交。
- 支持中断恢复。

重点能力：

- StateGraph。
- 条件分支。
- Checkpoint。
- Human-in-the-loop。
- 流程可观测。

## 常见误区

- 一上来就用 Agent，导致行为不可控。
- 只关注 Demo，不关注错误处理和评估。
- 把 prompt 当成一次性文本，没有版本管理。
- RAG 只调 top-k，不分析切分、召回、重排和上下文质量。
- 把 Memory 当数据库，缺少写入规则和隐私边界。
- 工具调用没有权限控制，容易产生副作用风险。
- 没有记录 trace，问题只能靠猜。

## 学习检查清单

- 能解释 `Runnable` 是什么。
- 能写出 `prompt | model | parser` 链路。
- 能让模型稳定输出结构化 JSON。
- 能构建一个带引用来源的 RAG。
- 能定义工具并让模型正确调用。
- 能控制 Agent 的最大执行轮数和失败兜底。
- 能管理多轮对话历史。
- 能用 LangGraph 表达有状态流程。
- 能为链路设计评估样例。
- 能记录关键日志并定位失败原因。

## 建议目录结构

如果后续要在本目录继续沉淀代码和笔记，可以按下面结构组织：

```text
docs/langchain/
├── langchain-learning-roadmap.md
├── notes/
│   ├── 01-overview.md
│   ├── 02-lcel.md
│   ├── 03-rag.md
│   ├── 04-agent.md
│   └── 05-langgraph.md
├── examples/
│   ├── basic_chain.py
│   ├── structured_output.py
│   ├── rag_local_docs.py
│   ├── agent_basic.py
│   └── langgraph_review_flow.py
├── prompts/
│   └── summary_prompt.md
└── evals/
    ├── dataset.jsonl
    └── report.md
```

## 时间安排参考

按每天 1 到 2 小时投入，可以这样安排：

| 周期 | 主题 | 目标 |
| --- | --- | --- |
| 第 1 周 | 基础模型调用、LCEL、Prompt | 能写可组合的基础链路 |
| 第 2 周 | 结构化输出、错误处理、路由 | 能接入业务字段和规则校验 |
| 第 3 周 | RAG | 能做本地知识库问答 |
| 第 4 周 | Tool、Agent、Memory | 能做多轮任务助手 |
| 第 5 周 | LangGraph | 能做有状态工作流 |
| 第 6 周 | 评估、观测、生产化 | 能把 Demo 变成可维护应用 |

## 最终验收标准

学习结束时，建议至少完成一个完整项目，并满足：

- 有清晰的输入输出协议。
- 有结构化输出和字段校验。
- 有异常处理和兜底策略。
- 有最少 20 条评估样例。
- 有日志或 trace 能定位问题。
- 有 README 说明如何运行、如何配置模型、如何扩展。
