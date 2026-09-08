# Notebook 环境说明

本项目使用项目内虚拟环境 `.venv` 作为 Notebook kernel，避免依赖系统 Python。当前系统默认 `python3` 是 3.7，不适合后续学习 LangChain / LangGraph，所以项目内环境使用 Python 3.11。

## 当前环境

- Python：`.venv/bin/python`
- Python 版本：3.11
- Kernel 名称：`learn-llm`
- Kernel 显示名：`Python (learn_llm)`
- Kernel 安装位置：`.venv/share/jupyter/kernels/learn-llm`

## 已安装基础依赖

- `ipykernel`
- `ipython`
- `ipywidgets`
- `python-dotenv`

这些依赖足够让 VS Code、Jupyter、Trae 或其他 Notebook 前端选择本项目内核并运行 `.ipynb`。

## 常用命令

验证 Python：

```bash
.venv/bin/python --version
```

验证 kernel：

```bash
JUPYTER_DATA_DIR=.venv/share/jupyter \
.venv/bin/python -m jupyter kernelspec list
```

重新注册 kernel：

```bash
.venv/bin/python -m ipykernel install --prefix .venv --name learn-llm --display-name "Python (learn_llm)"
```

在 Notebook 前端中选择内核：

```text
Python (learn_llm)
```

## 安装可选依赖

项目使用 `uv` 管理依赖。由于当前环境的 home cache 不可写，建议显式设置缓存目录和 Python 安装目录：

```bash
UV_CACHE_DIR=/tmp/uv-cache \
UV_PYTHON_INSTALL_DIR=.uv/python \
/home/jiangxukun/.local/bin/uv sync
```

安装 LangChain / LangGraph 学习依赖：

```bash
UV_CACHE_DIR=/tmp/uv-cache \
UV_PYTHON_INSTALL_DIR=.uv/python \
/home/jiangxukun/.local/bin/uv pip install --python .venv/bin/python ".[llm]"
```

安装数据分析依赖：

```bash
UV_CACHE_DIR=/tmp/uv-cache \
UV_PYTHON_INSTALL_DIR=.uv/python \
/home/jiangxukun/.local/bin/uv pip install --python .venv/bin/python ".[analysis]"
```

安装本地 JupyterLab 服务端：

```bash
UV_CACHE_DIR=/tmp/uv-cache \
UV_PYTHON_INSTALL_DIR=.uv/python \
/home/jiangxukun/.local/bin/uv pip install --python .venv/bin/python ".[notebook]"
```

启动 JupyterLab：

```bash
JUPYTER_DATA_DIR=.venv/share/jupyter \
.venv/bin/jupyter lab --no-browser --ip 127.0.0.1
```

## 注意事项

- 不要使用系统 `python`，它当前指向 Python 2.7。
- 不要使用系统 `python3` 作为学习环境，它当前是 Python 3.7。
- 当前环境的 home 目录部分位置不可写，执行 Jupyter 命令时建议设置 `JUPYTER_DATA_DIR=.venv/share/jupyter`。
- 后续 Notebook 默认选择 `Python (learn_llm)`。
- 真实 API Key 放在未提交的 `.env` 文件中，不要写入 Notebook。
