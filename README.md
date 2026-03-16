# LLM QLoRA Fine-tuning Framework

<div align="center">

[![License](https://img.shields.io/github/license/agencyos-cn/llm-qlora-finetune-framework?style=flat-square)](./LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)](https://www.python.org/downloads/)
[![Stars](https://img.shields.io/github/stars/agencyos-cn/llm-qlora-finetune-framework.svg?style=social&label=Star)](https://github.com/agencyos-cn/llm-qlora-finetune-framework)
[![Forks](https://img.shields.io/github/forks/agencyos-cn/llm-qlora-finetune-framework.svg?style=social&label=Fork)](https://github.com/agencyos-cn/llm-qlora-finetune-framework)

**A Universal Large Language Model QLoRA Fine-tuning Framework Supporting Multiple Model Architectures**

[English](./README.md) · [中文](./README_zh.md) · [官网](https://agencyos.cn) · [文档](https://agencyos.cn/docs)

</div>

## 🚀 Features

- ✅ **Universal Support**: Compatible with Qwen, Llama, GLM, DeepSeek, and other mainstream model architectures
- ✅ **Efficient Training**: Based on QLoRA algorithm for efficient fine-tuning with reduced GPU memory usage
- ✅ **Complete Pipeline**: Integrated training, merging, and conversion capabilities
- ✅ **Easy Deployment**: Supports conversion to GGUF format for LM Studio and other inference engines
- ✅ **Quantization**: Built-in 4-bit quantization support for smaller models and faster inference
- ✅ **Scalable**: Flexible configuration system supporting various model sizes and training requirements

## 📊 Project Structure

```
llm-qlora-finetune-framework/
├── config.py                 # Configuration file with model & training parameters
├── run_train.py              # Training script for QLoRA fine-tuning
├── run_merge.py              # Script to merge base model with LoRA adapter
├── run_gguf.py               # Conversion script to GGUF format for LM Studio
├── install.bat               # Installation script for Windows environments
├── my_data.jsonl             # Example training data file (JSONL format)
├── README.md                 # Documentation
└── LICENSE                   # License information
```

## 🛠️ Quick Start

### Prerequisites

- Python 3.8+
- At least 12GB VRAM (recommended 24GB+ for larger models)
- CUDA-compatible GPU (NVIDIA)

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/agencyos-cn/llm-qlora-finetune-framework.git
cd llm-qlora-finetune-framework

# Install dependencies
python install.bat  # For Windows
# OR
pip install transformers torch peft bitsandbytes accelerate trl datasets llama-cpp-python
```

### 2. Prepare Your Data

Create a training dataset in JSONL format (`my_data.jsonl`):

```json
{"instruction": "Explain quantum computing", "input": "", "output": "Quantum computing is a type of computation that harnesses the physical phenomena of quantum mechanics..."}
{"instruction": "Write a poem about AI", "input": "", "output": "In silicon dreams and circuits bright, Where algorithms dance with light..."}
```

### 3. Configure Training Parameters

Edit [config.py](./config.py) to customize your training:

```python
# Select your base model
BASE_MODEL_PATH = "Qwen/Qwen2-7B-Instruct"  # Or "meta-llama/Llama-2-7b-chat-hf", etc.

# Set training parameters
DATASET_PATH = "my_data.jsonl"
LORA_R = 32
LORA_ALPHA = 64
LORA_DROPOUT = 0.05
TRAIN_BATCH_SIZE = 1
LEARNING_RATE = 2e-4
TRAIN_EPOCHS = 3
MAX_SEQ_LEN = 2048
```

### 4. Run the Training Pipeline

Execute the scripts in order:

```bash
# 1. Train the model
python run_train.py

# 2. Merge the LoRA adapter with the base model
python run_merge.py

# 3. Convert to GGUF format for use with LM Studio
python run_gguf.py
```

## 📋 Configuration Guide

### Model Selection

Modify [config.py](./config.py) to switch between different models:

```python
# Qwen Series
BASE_MODEL_PATH = "Qwen/Qwen2-7B-Instruct"

# Llama Series
BASE_MODEL_PATH = "meta-llama/Meta-Llama-3-8B-Instruct"

# GLM Series
BASE_MODEL_PATH = "THUDM/glm-4-9b-chat"

# Local Model Path
BASE_MODEL_PATH = "./models/local_model"
```

### Training Parameters

| Parameter | Description | Recommended Value |
|-----------|-------------|-------------------|
| `LORA_R` | Rank of LoRA matrices | 16-64 depending on model size |
| `LORA_ALPHA` | Scaling factor | Usually 2x `LORA_R` |
| `LORA_DROPOUT` | Dropout rate | 0.05-0.1 |
| `TRAIN_BATCH_SIZE` | Batch size per device | 1-4 depending on VRAM |
| `GRADIENT_ACCUMULATION` | Gradient accumulation steps | 8-16 |
| `LEARNING_RATE` | Learning rate | 2e-4 to 5e-5 |
| `TRAIN_EPOCHS` | Number of training epochs | 3-5 |
| `MAX_SEQ_LEN` | Maximum sequence length | 2048-4096 |

## 🧩 Supported Model Architectures

- [x] **Qwen** (Alibaba Cloud) - Qwen, Qwen2, Qwen2-Math, Qwen2.5, Qwen3, etc.
- [x] **Llama** (Meta) - Llama, Llama2, Llama3, CodeLlama, etc.
- [x] **GLM** (Zhipu AI) - GLM, GLM2, GLM3, ChatGLM, etc.
- [x] **DeepSeek** (DeepSeek) - DeepSeek, DeepSeek-Coder, etc.
- [x] **Mistral** (Mistral AI) - Mistral, Mixtral, etc.
- [x] **Baichuan** (Baichuan) - Baichuan, Baichuan2, etc.
- [x] **Yi** (01.AI) - Yi, Yi-Coder, etc.
- [ ] **More coming soon!**

## 🔧 Advanced Usage

### Custom Training Data Format

The framework accepts training data in JSONL format with the following fields:

- `instruction`: The instruction or query
- `input`: Optional additional context or input
- `output`: The desired response

Example:

```json
{
  "instruction": "Translate the following English text to Chinese:",
  "input": "Hello, how are you today?",
  "output": "你好，今天怎么样？"
}
```

### Multi-GPU Training

For multi-GPU setups, consider using DeepSpeed or FSDP with Accelerate:

```bash
accelerate config  # Configure accelerate
accelerate launch run_train.py  # Launch with multi-GPU support
```

## 🤝 Contributing

We welcome contributions to the LLM QLoRA Fine-tuning Framework! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See our [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to Hugging Face for providing the Transformers library
- Inspired by the QLoRA paper and implementation
- Special thanks to the open-source community for continuous improvements

## 💼 About AgencyOS

AgencyOS is an open-source platform for building autonomous AI agents. This framework is part of our mission to democratize AI technology.

---

<div align="center">

**Made with ❤️ by [AgencyOS](https://agencyos.cn)**

[![](https://img.shields.io/badge/GitHub-AgencyOS-181717?style=for-the-badge&logo=github)](https://github.com/agencyos-cn)
[![](https://img.shields.io/badge/Website-AgencyOS-0066CC?style=for-the-badge&logo=google-chrome)](https://agencyos.cn)

</div>