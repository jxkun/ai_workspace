# Scripts

本目录用于存放项目本地辅助脚本，例如图片生成、链接校验、源码锚点检查等。

当前本地校验入口：

```bash
python3 scripts/check_core_docs.py
python3 scripts/check_non_core_docs.py
python3 scripts/check_expert_learning_docs.py
```

专家学习目录还需要配合通用 source-study-docs complete 检查：

```bash
python3 /data00/home/jiangxukun/.trae/skills/source-study-docs/scripts/check_source_study_docs.py --docs-dir docs/expert-learning --source-root repo/codex --image-root image/expert-learning --complete --code-evidence-policy per-topic
```
