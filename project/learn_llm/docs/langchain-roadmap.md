# LangChain 学习路线

这份路线用于按实践顺序学习 LangChain。目标不是背 API，而是理解核心抽象，并能基于这些抽象搭建、调试和评估 Agent 应用。

## 学习目标

- 理解 LangChain 的核心构件：Models、Messages、Prompts、Output Parsers、Runnables、Tools、Retrievers 和 Agents。
- 用小示例学习，并能和 Plain Python 实现进行对比。
- 判断什么时候 LangChain 有帮助，什么时候直接使用原生 SDK 更简单。
- 在进入 LangGraph 之前，先理解状态、工具调用和 Chain 组合。

## 阶段 1：基础模型调用

学习重点：

- Chat Models
- Message 类型
- 模型参数
- 流式输出
- Provider 配置

实践：

- 在 `examples/langchain/` 下创建一个最小 Chat 示例。
- 对比非流式输出和流式输出。
- 通过配置控制模型名、temperature、timeout 和重试设置。

预期产出：

- `examples/langchain/01_basic_chat.py`
- `configs/langchain.env.example`

推荐资料：

- LangChain Python 官方文档：https://python.langchain.com/docs/
- Chat Models 概念页：https://python.langchain.com/docs/concepts/chat_models/
- Messages 概念页：https://python.langchain.com/docs/concepts/messages/

## 阶段 2：Prompt 和输出解析

学习重点：

- `ChatPromptTemplate`
- System / User Message 模板
- Few-shot Prompting
- 结构化输出
- Output Parsers

实践：

- 构建一个从短文本需求中抽取结构化字段的 Prompt。
- 增加 JSON 或 Pydantic 风格的输出结构。
- 在 `prompts/` 中记录 Prompt 版本。

预期产出：

- `examples/langchain/02_prompt_and_parser.py`
- `prompts/langchain/extract_task_fields.md`

推荐资料：

- Prompt Templates 概念页：https://python.langchain.com/docs/concepts/prompt_templates/
- Structured Outputs 概念页：https://python.langchain.com/docs/concepts/structured_outputs/
- Output Parsers 概念页：https://python.langchain.com/docs/concepts/output_parsers/

## 阶段 3：Runnables 和 Chains

学习重点：

- LangChain Expression Language
- Runnable 组合
- `invoke`、`batch` 和 `stream`
- 步骤之间的数据流
- 调试 Chain 的输入输出

实践：

- 将 Prompt、Model 和 Parser 组合成一个 Runnable Chain。
- 在 Prompt 前增加一个小的预处理函数。
- 在模型响应后增加一个后处理函数。

预期产出：

- `examples/langchain/03_runnable_chain.py`

推荐资料：

- Runnables 概念页：https://python.langchain.com/docs/concepts/runnables/
- LangChain Expression Language 指南：https://python.langchain.com/docs/concepts/lcel/

## 阶段 4：Tools

学习重点：

- Tool 定义
- Tool Schema
- Tool Calling
- Tool 结果处理
- 错误处理

实践：

- 创建本地工具，例如计算器、当前目录读取器、模拟搜索。
- 让模型选择工具，并观察 Tool Call Payload。
- 增加失败用例，观察 Chain 如何表现。

预期产出：

- `examples/langchain/04_tools.py`
- `src/learn_llm/tools/`

推荐资料：

- Tools 概念页：https://python.langchain.com/docs/concepts/tools/
- Tool Calling 概念页：https://python.langchain.com/docs/concepts/tool_calling/

## 阶段 5：Retrieval 和 RAG

学习重点：

- Document Loaders
- Text Splitters
- Embeddings
- Vector Stores
- Retrievers
- Retrieval-Augmented Generation
- 带引用的回答

实践：

- 在 `data/raw/` 放几份 Markdown 文档。
- 构建一个本地文档问答示例。
- 对比不同 chunk size 的效果。
- 回答时返回来源引用。

预期产出：

- `examples/langchain/05_rag_markdown_qa.py`
- `data/raw/sample_docs/`
- `docs/rag-notes.md`

推荐资料：

- Retrieval 概念页：https://python.langchain.com/docs/concepts/retrieval/
- Document Loaders 概念页：https://python.langchain.com/docs/concepts/document_loaders/
- Text Splitters 概念页：https://python.langchain.com/docs/concepts/text_splitters/
- Embedding Models 概念页：https://python.langchain.com/docs/concepts/embedding_models/
- Vector Stores 概念页：https://python.langchain.com/docs/concepts/vectorstores/

## 阶段 6：Agents

学习重点：

- Agent 循环
- 工具选择
- Agent 状态
- 中间步骤
- 停止条件
- 失败模式

实践：

- 用 LangChain Tools 重建手写 ReAct Agent。
- 增加一组安全的本地工具。
- 记录每次工具调用和最终回答。
- 对比 LangChain 版本和 Plain Python 版本。

预期产出：

- `agents/langchain-agent/README.md`
- `agents/langchain-agent/design.md`
- `examples/langchain/06_agent_with_tools.py`

推荐资料：

- Agents 概览：https://python.langchain.com/docs/concepts/agents/
- Tools 概念页：https://python.langchain.com/docs/concepts/tools/
- LangGraph 官方文档：https://langchain-ai.github.io/langgraph/

## 阶段 7：记忆和对话状态

学习重点：

- Chat History
- 短期记忆
- 长期记忆
- 状态持久化
- 用户 / 会话边界

实践：

- 给一个简单助手增加 Chat History。
- 将会话状态放在 Prompt 构造逻辑之外维护。
- 对比有无 Retrieval 时的记忆表现。

预期产出：

- `examples/langchain/07_chat_history.py`
- `docs/memory-notes.md`

推荐资料：

- Memory 概念页：https://python.langchain.com/docs/concepts/memory/
- Chat History 概念页：https://python.langchain.com/docs/concepts/chat_history/

## 阶段 8：评估和可观测性

学习重点：

- 回归用例
- 预期 Tool Call
- 延迟和成本记录
- Trace 检查
- LangSmith 基础

实践：

- 为一个 Chain 创建小型 Golden Dataset。
- 对结构化输出做断言。
- 记录中间步骤。
- 用相同输入对比不同 Prompt 版本。

预期产出：

- `tests/test_langchain_extract_task_fields.py`
- `docs/evaluation-notes.md`

推荐资料：

- LangSmith 官方文档：https://docs.smith.langchain.com/
- LangChain 测试指南：https://python.langchain.com/docs/how_to/#testing

## 阶段 9：工程化模式

学习重点：

- 配置管理
- 依赖边界
- 共享工具
- 重试策略
- 超时控制
- 模型降级
- 部署形态

实践：

- 将稳定工具沉淀到 `src/learn_llm/`。
- 保持示例可运行，不依赖隐藏状态。
- 为一个 LangChain 示例增加小型 CLI 包装。

预期产出：

- `src/learn_llm/langchain_utils/`
- `scripts/run_langchain_demo.py`

## 推荐学习顺序

1. 先阅读 Chat Models、Messages、Prompts 和 Runnables 的概念页。
2. 用非常小的脚本完成阶段 1 到阶段 3。
3. 先学 Tools，再学 Agents。
4. 先做 RAG，再做复杂 Agent。
5. 先构建一个 LangChain Agent，再进入 LangGraph 学习更显式的工作流控制。
6. 等一两个示例稳定后，再补评估和回归测试。

## 学习资料优先级

建议按这个顺序使用资料：

1. LangChain Python 官方文档：https://python.langchain.com/docs/
2. LangGraph 官方文档：https://langchain-ai.github.io/langgraph/
3. LangSmith 官方文档：https://docs.smith.langchain.com/
4. LangChain GitHub 示例：https://github.com/langchain-ai/langchain
5. LangChain Academy，如果当前环境可访问：https://academy.langchain.com/

LangChain 变化比较快，API 用法优先看官方文档。博客和视频更适合理解直觉，不建议作为当前代码写法的唯一依据。

