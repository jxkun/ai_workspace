# Codex 源码快照记录

本文记录 `repo/codex/` 的来源和版本锚点。后续所有源码分析都以这里记录的快照为基线。

## 当前基线

| 字段 | 值 |
| --- | --- |
| 上游仓库 | `https://github.com/openai/codex` |
| 本地路径 | `repo/codex/` |
| 目标分支 | `main` |
| main 快照 commit | `1fb5158b3496a05abb89fb992d45737a02511d47` |
| commit 时间 | `2026-09-07T02:28:25Z` |
| commit 说明 | `Preserve saved permissions when resuming or forking remote tasks (#43330)` |
| 获取日期 | `2026-09-07` |
| 获取方式 | GitHub `codeload` tarball；Git clone HTTPS 在当前环境超时 |
| main tarball sha256 | `55cd06c871a3352b23233b05ec68631fa2c74cf205c2f77e3d17fe7f5b08e5e5` |
| 发布版参考 | SourceForge mirror `rust-v0.153.4` |
| SourceForge 源码包 sha256 | `b2bd378ebabf48242132a8a9df39ed41e0f4c5588bd57b138070d1be7fd09507` |
| 本地校验 | `repo/codex/codex-rs/Cargo.toml` 存在，源码目录已解压 |

## 获取记录

首选命令：

```bash
git clone --depth 1 https://github.com/openai/codex.git repo/codex
```

当前环境中 GitHub HTTPS clone 超时，因此改用固定 commit 的源码 tarball：

```bash
curl -L -C - --retry 20 \
  -o /tmp/openai-codex-1fb5158b3496a05abb89fb992d45737a02511d47.tar.gz \
  https://codeload.github.com/openai/codex/tar.gz/1fb5158b3496a05abb89fb992d45737a02511d47
mkdir -p repo/codex
tar -xzf /tmp/openai-codex-1fb5158b3496a05abb89fb992d45737a02511d47.tar.gz \
  -C repo/codex --strip-components=1
```

SourceForge mirror 可作为发布版参考：

```bash
curl -L -C - --retry 20 \
  -o /tmp/openai-codex-0.153.4-source.tar.gz \
  'https://sourceforge.net/projects/openai-codex.mirror/files/rust-v0.153.4/0.153.4%20source%20code.tar.gz/download'
```

## 本地校验命令

```bash
test -f repo/codex/codex-rs/Cargo.toml
sed -n '1,120p' repo/codex/codex-rs/Cargo.toml
```

## 更新规则

- 更新 `repo/codex/` 前，先记录目标 commit 或 release。
- 更新后，必须同步修改本文的 commit、获取方式和校验信息。
- 若上游目录结构变化，必须重新检查 `docs/methodology.md` 中的阅读阶段和源码锚点策略。
- 已完成的专题文档要标注是否基于旧 commit，需要复核时在文档中加入待验证项。
