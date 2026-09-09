# Core Images

本目录用于存放 `codex-rs/core` 层分析相关图片。

每张图同时保留 SVG 源文件和同名 PNG 预览文件。文档内嵌使用 PNG，避免部分 Markdown 渲染器无法展示 SVG；需要缩放或继续编辑时使用 SVG。

- `codex-core-module-map-v1.svg`：core 层模块文档规划地图，当前推荐版本。
- `core-crate-boundary-v1.svg`：core crate 对外边界。
- `thread-lifecycle-v1.svg`：thread 创建、提交、事件、恢复生命周期。
- `session-turn-loop-v1.svg`：session/turn 主循环。
- `task-types-v1.svg`：regular、compact、review、user shell 等 task 类型。
- `context-world-state-v1.svg`：context 与 world state 数据流。
- `context-fragment-lifecycle-v1.svg`：context fragment 生命周期。
- `tool-runtime-v1.svg`：工具注册、路由、执行和结果回传。
- `tool-router-handler-v1.svg`：工具路由与 handler 边界。
- `unified-exec-lifecycle-v1.svg`：unified exec 生命周期。
- `exec-output-buffer-v1.svg`：exec 输出缓冲模型。
- `safety-approval-decision-v1.svg`：安全与审批判定链。
- `sandbox-policy-boundary-v1.svg`：sandbox 策略边界。
- `apply-patch-flow-v1.svg`：apply_patch 执行流程。
- `patch-safety-route-v1.svg`：patch 安全路由。
- `config-to-turn-v1.svg`：配置到 turn 的流转。
- `model-client-request-v1.svg`：模型请求构造路径。
- `core-extension-surfaces-v1.svg`：core 扩展入口。
- `mcp-tool-exposure-v1.svg`：MCP 工具曝光与调用。
- `multi-agent-control-v1.svg`：多 agent 控制面。
- `spawn-agent-lifecycle-v1.svg`：子 agent 生命周期。
- `rollout-compaction-resume-v1.svg`：rollout、压缩和恢复。
- `thread-reconstruction-v1.svg`：thread 历史重建。
- `guardian-review-flow-v1.svg`：Guardian 审查流程。
- `attestation-boundary-v1.svg`：attestation 边界。
- `realtime-context-flow-v1.svg`：realtime 上下文流转。
- `image-preparation-v1.svg`：图片预处理流程。
- `turn-observability-v1.svg`：turn 观测字段。
- `supporting-utils-map-v1.svg`：支撑工具地图。

后续每篇 core 专题文档如果包含流程、状态、架构或时序说明，应在本目录或更细子目录下新增 SVG 图片，并从 Markdown 文档中引用。
