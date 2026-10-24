# 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制项目所有文件
COPY . .

# 设置环境变量（默认连接本地 Ollama）
ENV EVAL_API_URL="http://host.docker.internal:11434/v1/chat/completions"
ENV EVAL_MODEL="qwen2.5:7b"

# 默认运行批量评测脚本
CMD ["python", "src/batch_eval.py"]