# LLM QLoRA 微调框架

<div align="center">

[![License](https://img.shields.io/github/license/agencyos-cn/llm-qlora-finetune-framework?style=flat-square)](./LICENSE)
[![Python 版本](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)](https://www.python.org/downloads/)
[![Stars](https://img.shields.io/github/stars/agencyos-cn/llm-qlora-finetune-framework.svg?style=social&label=Star)](https://github.com/agencyos-cn/llm-qlora-finetune-framework)
[![Forks](https://img.shields.io/github/forks/agencyos-cn/llm-qlora-finetune-framework.svg?style=social&label=Fork)](https://github.com/agencyos-cn/llm-qlora-finetune-framework)

**一个通用的大语言模型QLoRA微调框架，支持多种模型架构**

[English](./README.md) · [中文](./README_zh.md) · [官网](https://agencyos.cn) · [文档](https://agencyos.cn/docs)

</div>

## 🚀 特性

- ✅ **通用支持**: 兼容 Qwen、Llama、GLM、DeepSeek 等主流模型架构
- ✅ **高效训练**: 基于QLoRA算法，显著降低GPU内存需求，实现高效微调
- ✅ **完整流水线**: 集成了训练、合并和转换功能
- ✅ **易部署**: 支持转换为GGUF格式，便于LM Studio等推理引擎使用
- ✅ **量化支持**: 内置4-bit量化支持，模型更小，推理更快
- ✅ **可扩展**: 灵活的配置系统，支持各种模型大小和训练需求

## 📊 项目结构

```
llm-qlora-finetune-framework/
├── config.py                 # 配置文件，包含模型和训练参数
├── run_train.py              # QLoRA微调训练脚本
├── run_merge.py              # 合并基础模型与LoRA适配器脚本
├── run_gguf.py               # 转换为GGUF格式（用于LM Studio）脚本
├── install.bat               # Windows环境安装脚本
├── my_data.jsonl             # 示例训练数据文件（JSONL格式）
├── README.md                 # 文档
└── LICENSE                   # 许可证信息
```

## 🛠️ 快速开始

### 系统要求

- Python 3.8+
- 至少12GB显存（推荐24GB+用于大型模型）
- CUDA兼容GPU（NVIDIA）

### 1. 克隆和设置

```bash
# 克隆仓库
git clone https://github.com/agencyos-cn/llm-qlora-finetune-framework.git
cd llm-qlora-finetune-framework

# 安装依赖
python install.bat  # Windows系统
# 或者
pip install transformers torch peft bitsandbytes accelerate trl datasets llama-cpp-python
```

### 2. 准备训练数据

创建JSONL格式的训练数据集(`my_data.jsonl`)：

```json
{"instruction": "解释量子计算", "input": "", "output": "量子计算是一种利用量子力学现象的计算方式，如叠加态和纠缠态..."}
{"instruction": "写一首关于AI的诗", "input": "", "output": "在硅片的梦想和明亮的电路中，算法与光共舞..."}
```

### 3. 配置训练参数

编辑[config.py](./config.py)自定义训练参数：

```python
# 选择基础模型
BASE_MODEL_PATH = "Qwen/Qwen2-7B-Instruct"  # 或 "meta-llama/Llama-2-7b-chat-hf" 等

# 设置训练参数
DATASET_PATH = "my_data.jsonl"
LORA_R = 32
LORA_ALPHA = 64
LORA_DROPOUT = 0.05
TRAIN_BATCH_SIZE = 1
LEARNING_RATE = 2e-4
TRAIN_EPOCHS = 3
MAX_SEQ_LEN = 2048
```

### 4. 运行训练流水线

按顺序执行脚本：

```bash
# 1. 训练模型
python run_train.py

# 2. 合并LoRA适配器与基础模型
python run_merge.py

# 3. 转换为GGUF格式，用于LM Studio
python run_gguf.py
```

## 📋 配置指南

### 模型选择

修改[config.py](./config.py)在不同模型间切换：

```python
# Qwen系列
BASE_MODEL_PATH = "Qwen/Qwen2-7B-Instruct"

# Llama系列
BASE_MODEL_PATH = "meta-llama/Meta-Llama-3-8B-Instruct"

# GLM系列
BASE_MODEL_PATH = "THUDM/glm-4-9b-chat"

# 本地模型路径
BASE_MODEL_PATH = "./models/local_model"
```

### 训练参数

| 参数 | 描述 | 推荐值 |
|------|------|--------|
| `LORA_R` | LoRA矩阵的秩 | 根据模型大小，16-64 |
| `LORA_ALPHA` | 缩放因子 | 通常是`LORA_R`的2倍 |
| `LORA_DROPOUT` | Dropout率 | 0.05-0.1 |
| `TRAIN_BATCH_SIZE` | 每设备批处理大小 | 1-4（取决于显存） |
| `GRADIENT_ACCUMULATION` | 梯度累积步数 | 8-16 |
| `LEARNING_RATE` | 学习率 | 2e-4 到 5e-5 |
| `TRAIN_EPOCHS` | 训练轮数 | 3-5 |
| `MAX_SEQ_LEN` | 最大序列长度 | 2048-4096 |

## 🧩 支持的模型架构

- [x] **Qwen** (阿里巴巴) - Qwen, Qwen2, Qwen2-Math, Qwen2.5, Qwen3 等
- [x] **Llama** (Meta) - Llama, Llama2, Llama3, CodeLlama 等
- [x] **GLM** (智谱AI) - GLM, GLM2, GLM3, ChatGLM 等
- [x] **DeepSeek** (深度求索) - DeepSeek, DeepSeek-Coder 等
- [x] **Mistral** (Mistral AI) - Mistral, Mixtral 等
- [x] **Baichuan** (百川智能) - Baichuan, Baichuan2 等
- [x] **Yi** (零一万物) - Yi, Yi-Coder 等
- [ ] **更多即将推出！**

## 🔧 高级用法

### 自定义训练数据格式

框架接受JSONL格式的训练数据，包含以下字段：

- `instruction`: 指令或查询
- `input`: 可选的附加上下文或输入
- `output`: 期望的响应

示例：

```json
{
  "instruction": "将以下英文文本翻译为中文:",
  "input": "Hello, how are you today?",
  "output": "你好，今天怎么样？"
}
```

### 多GPU训练

对于多GPU设置，考虑使用Deepspeed或FSDP配合Accelerate：

```bash
accelerate config  # 配置accelerate
accelerate launch run_train.py  # 启动多GPU支持
```

## 🤝 贡献

我们欢迎对LLM QLoRA微调框架的贡献！以下是参与方式：

1. Fork仓库
2. 创建功能分支 (`git checkout -b feature/awesome-feature`)
3. 提交更改 (`git commit -m 'Add awesome feature'`)
4. 推送分支 (`git push origin feature/awesome-feature`)
5. 提交Pull Request

详见我们的[CONTRIBUTING.md](./CONTRIBUTING.md)。

## 📄 许可证

本项目基于Apache 2.0许可证 - 详情请见[LICENSE](./LICENSE)文件。

## 🙏 致谢

- 感谢Hugging Face提供了Transformers库
- 受QLoRA论文及其实现的启发
- 特别感谢开源社区的持续改进

## 💼 关于AgencyOS

AgencyOS是一个构建自主AI代理的开源平台。此框架是我们致力于普及AI技术使命的一部分。

---

<div align="center">

**由 [AgencyOS](https://agencyos.cn) 用 ❤️ 制作**

[![](https://img.shields.io/badge/GitHub-AgencyOS-181717?style=for-the-badge&logo=github)](https://github.com/agencyos-cn)
[![](https://img.shields.io/badge/Website-AgencyOS-0066CC?style=for-the-badge&logo=google-chrome)](https://agencyos.cn)

</div>