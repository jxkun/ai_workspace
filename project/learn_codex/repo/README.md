# 外部源码副本

`repo/` 用于放本项目专属的外部源码研究对象。

## `repo/codex/`

`repo/codex/` 是 `openai/codex` 的本地源码快照目录，用于后续分析 Codex harness。该目录不纳入版本管理；需要恢复时按 `../docs/source-snapshot.md` 中的命令重新获取。

当前初始化使用 GitHub `codeload` 固定 commit tarball 获取源码，因为本机环境中 `git clone https://github.com/openai/codex.git` 超时。
