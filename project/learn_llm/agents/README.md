# Agents

这个目录用于记录 Agent 实验和可复用 Agent 设计。

当一个 Agent 设计超过几行简短说明后，就为它单独建立一个子目录。

建议结构：

```text
agents/
├── README.md
├── scratch-agent/
│   ├── README.md
│   ├── design.md
│   └── run.py
├── langchain-agent/
│   ├── README.md
│   ├── design.md
│   └── run.py
└── langgraph-agent/
    ├── README.md
    ├── graph.md
    └── run.py
```

## Agent 设计模板

新增 Agent 时，建议说明：

- 目标
- 输入
- 输出
- 工具
- 状态
- 控制流
- 防护边界
- 评估用例

## 实验索引

| Agent | 框架 | 状态 | 说明 |
| --- | --- | --- | --- |
| Scratch agent | Plain Python | 计划中 | 先手写核心 Agent 循环。 |
| LangChain agent | LangChain | 计划中 | 用框架能力重建 Scratch agent。 |
| LangGraph agent | LangGraph | 计划中 | 增加显式状态图和路由。 |

