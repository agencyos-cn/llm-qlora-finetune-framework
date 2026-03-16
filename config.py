# ============================================== #
#          通用大模型 QLoRA 训练配置文件 #
#       支持：Qwen / Llama / GLM / DeepSeek 等 #
# ============================================== #

# --------------------------
# 1. 基座模型配置（切换模型只改这里）
# --------------------------

# 示例1：Qwen3-Coder-30B
BASE_MODEL_PATH = "Qwen/Qwen3-Coder-30B"

# 示例2：Qwen-7B-Chat
# BASE_MODEL_PATH = "Qwen/Qwen-7B-Chat"

# 示例3：Llama-3-8B
# BASE_MODEL_PATH = "meta-llama/Meta-Llama-3-8B-Instruct"

# 示例4：本地模型路径（下载到本地的模型文件夹）
# BASE_MODEL_PATH = "./local_models/Qwen3-Coder-30B"

# --------------------------
# 2. 训练&文件配置
# --------------------------

DATASET_PATH = "my_data.jsonl"          # 你的训练数据
LORA_SAVE_PATH = "./lora_output"        # LoRA 保存路径
MERGED_MODEL_PATH = "./merged_model"    # 合并后模型路径
GGUF_OUTPUT_NAME = "my_finetuned_model-q4_k_m.gguf"  # 最终LM Studio模型名

# --------------------------
# 3. LoRA 通用最优配置（自动适配所有模型）
# --------------------------

LORA_R = 32             # 大模型32，小模型16
LORA_ALPHA = 64         # 固定比例
LORA_DROPOUT = 0.05     # LoRA Dropout率
TRAIN_BATCH_SIZE = 1    # 训练批次大小
GRADIENT_ACCUMULATION = 8  # 梯度累积步数
LEARNING_RATE = 2e-4    # 学习率
TRAIN_EPOCHS = 3        # 训练轮数
MAX_SEQ_LEN = 2048      # 最大序列长度
