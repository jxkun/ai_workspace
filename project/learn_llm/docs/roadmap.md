# 学习路线

这份路线图用于让学习过程始终围绕“逐步搭建有用的 LLM Agent”展开。

## 阶段 0：工作区基线

- 初始化仓库结构。
- 增加项目说明和 Agent 协作文档。
- 确定 Python 环境管理方式。
- 增加第一个最小 LLM 调用示例。

建议产出：

- `README.md`
- `AGENTS.md`
- `examples/basic_chat.py`
- `configs/.env.example`

## 阶段 1：LLM API 基础

学习重点：

- Messages 和角色
- Prompt 构造
- 流式输出
- 结构化输出
- Tool Calling

实验：

- 最小 Chat 脚本
- 流式输出脚本
- JSON 输出解析
- 一个 Tool Call 示例

## 阶段 2：从零实现 Agent 循环

学习重点：

- ReAct 风格循环
- 工具注册
- Scratchpad / 状态
- 重试和超时处理
- 最终回答控制

实验：

- 计算器、模拟搜索等本地工具
- 面向小型本地数据集的文件读取助手
- 为每个 Agent 步骤记录 Trace 日志

## Phase 3: LangChain

专项路线：[langchain-roadmap.md](./langchain-roadmap.md)

学习重点：

- Chat Model 适配器
- Prompt 模板
- Runnables
- Tools
- Agents
- Retrieval Chains

实验：

- 使用 LangChain 重新实现阶段 2 的 Agent
- 简单文档问答
- Prompt 和 Chain 对比笔记

## Phase 4: LangGraph

学习重点：

- 图状态建模
- 节点组合
- 条件路由
- Interrupt 和 Checkpoint
- 多 Agent 协作

实验：

- 研究助手图
- 计划、执行、反思图
- 人工审批 Checkpoint
- 多 Agent 工作流 Demo

## 阶段 5：RAG 和记忆

学习重点：

- Loader
- 分块策略
- Embeddings
- 向量库
- 长期记忆
- 会话记忆

实验：

- 本地 Markdown 问答
- 对比分块大小
- 增加引用输出
- 增加记忆读写策略

## 阶段 6：评估

学习重点：

- Golden Test Cases
- Tool Call 校验
- Prompt 回归测试
- 成本和延迟追踪

实验：

- 常见问题测试集
- 预期 Tool Call 快照
- 评估报告格式

## 阶段 7：Agent 应用化

学习重点：

- CLI 接口
- 本地 API 服务
- 配置管理
- 可观测性
- 部署记录

实验：

- 支持选择模型的 CLI Agent
- FastAPI 包装
- 本地 Trace 查看或日志输出

