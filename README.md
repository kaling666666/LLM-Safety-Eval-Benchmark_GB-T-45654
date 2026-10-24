# LLM Safety Eval Benchmark (GB/T 45654-2025)

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

本项目是基于中国国家标准 **GB/T 45654-2025《网络安全技术 生成式人工智能服务安全基本要求》** 的开源大模型安全评估测试工具包。包含合规级关键词库、测试题库及自动化裁判脚本。

## 🎯 核心特性
- **合规级测试用例集**：将国标附录 B 的评估方法转化为结构化评测用例，覆盖数据安全、模型安全及服务安全三大维度。
- **自动化评测引擎**：基于 LLM-as-a-Judge 范式，提供 Python 脚本直接调用本地（Ollama）或云端大模型接口，自动判定模型输出的安全性（Safe/Unsafe）并计算安全合格率。
- **开箱即用**：提供极简的 Prompt 模板、自动化批量评测脚本与 API 调用代码。
- **安全分类模型**：内置基于 LLM 的（Zero-Shot）安全分类器，可自动将输入文本映射至国标附录 A 的 31 类风险中，并输出分类准确率。
- **真实合规题库**：内置超 2000+ 条基于国标构建的生成内容测试题库、1100+ 条拒答题库及 11000+ 类敏感关键词库，支持开箱即用的批量评测。
- **与时俱进**：不定期更新词库。

## 📂 项目结构
- `assets/images`：演示截图与图片资源。
- `assets/references`：GB/T-45654原件以及OWASP大语言模型人工智能应用Top10安全威胁2025原件。
- `datasets/raw/`：安全评估测试用例集。
- `datasets/sap/`：核心测试数据集（包含关键词库、内容测试题库、拒答题库及原始 Excel）。
- `outputs/`：模型跑分评测报告生成目录（JSON 格式）。
- `src/core/evaluator.py`：单条测试的 LLM 裁判评测脚本。
- `src/core/classifier_zeroshot.py`：基于大模型的安全风险分类器。
- `src/scripts/batch_eval.py`：自动化批量评测引擎（读取 datasets，输出报告）。
- `src/scripts/excel_to_json.py`：将关键词库、内容测试题库、拒答题库的Excel转换成JSON 格式，更新Excel表格后运行可以覆盖原先测试数据。
- `outputs`：产出报告。
- `requirements.txt`：项目依赖。

## 📊 运行效果展示

### 🛡️ 安全裁判结果可视化
![安全合格率饼图](assets/images/safety_pie_chart.png)

### 📈 细粒度风险分类结果
![分类准确率柱状图](assets/images/classifier_accuracy_chart.png)

## 🚀 快速开始

### 方式一：本地 Python 环境运行

1. 克隆仓库并安装依赖：
   ```bash
   git clone https://github.com/kaling666666/LLM-Safety-Eval-Benchmark_GB-T-45654.git
   cd LLM-Safety-Eval-Benchmark_GB-T-45654
   pip install -r requirements.txt
   ```

2. 启动本地大模型（以 Ollama 为例）：
   ```bash
   ollama run qwen2.5:7b
   ```
   
3. 运行批量评测脚本：
    ```bash
   python src/batch_eval.py
   ```

### 方式二：使用 Docker 一键运行
   ```bash
   docker build -t gb-safety-eval
   docker run --rm gb-safety-eval
   ```

## 📚 参考文献

本项目在设计与评测标准上参考了以下官方文档：
- [GB/T 45654-2025 网络安全技术 生成式人工智能服务安全基本要求](./assets/references/GBT+45654-2025.pdf)
- [OWASP 大语言模型人工智能应用 Top 10 安全威胁 2025](./assets/references/OWASP大语言模型人工智能应用Top10安全威胁2025.pdf)

⚠️ 免责声明
本仓库中的测试数据集仅供安全合规评测与学术研究使用，请勿用于恶意攻击。使用者需自行承担相关法律责任。

本项目采用 Apache License 2.0 协议开源。