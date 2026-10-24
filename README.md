
# LLM Safety Eval Benchmark (GB/T 45654-2025)

本项目是基于中国国家标准 GB/T 45654-2025《网络安全技术 生成式人工智能服务安全基本要求》的开源大模型安全评估测试工具包,包含合规级关键词库、测试题库及自动化裁判脚本。。

## 🎯 核心特性
- **合规级测试用例集**：将国标附录 B 的评估方法转化为结构化 CSV 测试用例，覆盖数据安全、模型安全及服务安全三大维度。
- **自动化评测引擎**：基于 LLM-as-a-Judge 范式，提供 Python 脚本直接调用本地（Ollama）或云端大模型接口，自动判定模型输出的安全性（Safe/Unsafe）。
- **开箱即用**：提供极简的 Prompt 模板与 API 调用代码。

## 📂 目录结构
- `GB-T45654_test_cases.csv`：基于国标GB/T 45654-2025-B.2 章节的结构化评估用例集。
- `src/evaluator.py`：LLM 裁判自动化评测脚本。
- `requirements.txt`：项目依赖。

## 🚀 快速开始

1. 克隆仓库并安装依赖：
   ```bash
   git clone https://github.com/kaling666666/LLM-Safety-Eval-Benchmark_GB-T-45654.git
   cd LLM-Safety-Eval-Benchmark_GB-T-45654
   pip install -r requirements.txt