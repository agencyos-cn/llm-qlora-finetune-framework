# 大模型 QLoRA 微调工具

这是一个通用的大模型微调工具，支持 Qwen 全系列、Llama 全系列、GLM 全系列、DeepSeek 全系列以及任何开源 Hugging Face 模型。

## 功能特性

- ✅ 支持多种大模型架构
- ✅ 基于 QLoRA 算法，高效微调
- ✅ 集成训练、合并、转换功能
- ✅ 支持量化以减少显存占用

## 使用方法（超级简单）

### 1. 切换模型

只需要修改 [config.py](file:根目录/llm_qlora_train/config.py) 里的一行：

```python
BASE_MODEL_PATH = "你的模型ID或本地路径"
```

### 2. 准备数据

准备 `my_data.jsonl` 文件（每行一条）：

```json
{"instruction":"你的指令","input":"补充内容","output":"标准输出"}
```

### 3. 执行流程

1. 运行 [install.bat](file:根目录/llm_qlora_train/install.bat) 安装环境
2. 运行 [run_train.py](file:根目录/llm_qlora_train/run_train.py) 训练
3. 运行 [run_merge.py](file:根目录/llm_qlora_train/run_merge.py) 合并
4. 运行 [run_gguf.py](file:根目录/llm_qlora_train/run_gguf.py) 转 LM Studio 格式

## 两个 pip 命令的核心区别（最终总结）

| 命令 | 用途 | 能否微调 |
|------|------|----------|
| `pip install transformers torch sentencepiece` | 仅推理 / 对话，运行模型 | ❌ 不能训练 |
| `pip install transformers torch peft bitsandbytes accelerate trl datasets` | 完整训练环境 | ✅ 支持 LoRA/QLoRA 微调 |

## 环境安装

运行 [install.bat](file:根目录/llm_qlora_train/install.bat) 自动安装所需依赖：

```bash
install.bat
```

或者手动安装完整训练环境：

```bash
pip install transformers torch peft bitsandbytes accelerate trl datasets llama_cpp_python
```

## 配置文件说明

主要配置项位于 [config.py](file:根目录/llm_qlora_train/config.py)，包括：

- `BASE_MODEL_PATH`: 基础模型路径或HuggingFace模型ID
- `TRAIN_DATA_PATH`: 训练数据路径
- `OUTPUT_DIR`: 训练输出目录
- `LORA_RANK`: LoRA 秩
- `LORA_ALPHA`: LoRA 缩放因子
- `LORA_DROPOUT`: LoRA dropout率
- `BATCH_SIZE`: 批处理大小
- `GRADIENT_ACCUMULATION_STEPS`: 梯度累积步数
- `EPOCHS`: 训练轮数
- `LEARNING_RATE`: 学习率
- `CUTOFF_LEN`: 输入序列最大长度
- `LORA_SAVE_PATH`: LoRA模型保存路径
- `MERGED_MODEL_PATH`: 合并后模型保存路径
- `GGUF_OUTPUT_NAME`: GGUF格式输出文件名

## 文件说明

- [run_train.py](file:根目录/llm_qlora_train/run_train.py): 执行模型训练
- [run_merge.py](file:根目录/llm_qlora_train/run_merge.py): 合并基础模型和LoRA适配器
- [run_gguf.py](file:根目录/llm_qlora_train/run_gguf.py): 转换为GGUF格式用于LM Studio
- [config.py](file:根目录/llm_qlora_train/config.py): 配置文件
- [install.bat](file:根目录/llm_qlora_train/install.bat): 依赖安装脚本

## 支持的模型

- ✅ Qwen 全系列
- ✅ Llama 全系列
- ✅ GLM 全系列
- ✅ DeepSeek 全系列
- ✅ 任何开源 Hugging Face 模型

## 极简使用说明书（3 步上手）

1. **配置**: 修改 [config.py](file:根目录/llm_qlora_train/config.py) 中的模型路径和训练参数
2. **准备数据**: 创建 `my_data.jsonl` 文件并填入训练数据
3. **执行**: 按顺序运行 [install.bat](file:根目录/llm_qlora_train/install.bat) → [run_train.py](file:根目录/llm_qlora_train/run_train.py) → [run_merge.py](file:根目录/llm_qlora_train/run_merge.py) → [run_gguf.py](file:根目录/llm_qlora_train/run_gguf.py)