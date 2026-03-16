from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TrainingArguments
from peft import LoraConfig
from trl import SFTTrainer
from datasets import load_dataset
import torch
import config as cfg

print("✅ 开始加载模型：", cfg.BASE_MODEL_PATH)

# 4bit 量化配置（通用）
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

# 加载模型&分词器
model = AutoModelForCausalLM.from_pretrained(
    cfg.BASE_MODEL_PATH,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(
    cfg.BASE_MODEL_PATH,
    trust_remote_code=True
)
tokenizer.pad_token = tokenizer.eos_token

# LoRA 通用配置
lora_config = LoraConfig(
    r=cfg.LORA_R,
    lora_alpha=cfg.LORA_ALPHA,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_dropout=cfg.LORA_DROPOUT,
    bias="none",
    task_type="CAUSAL_LM"
)

# 训练参数
train_args = TrainingArguments(
    output_dir=cfg.LORA_SAVE_PATH,
    per_device_train_batch_size=cfg.TRAIN_BATCH_SIZE,
    gradient_accumulation_steps=cfg.GRADIENT_ACCUMULATION,
    learning_rate=cfg.LEARNING_RATE,
    num_train_epochs=cfg.TRAIN_EPOCHS,
    logging_steps=5,
    save_strategy="epoch",
    fp16=True,
    optim="paged_adamw_8bit"
)

# 加载数据
dataset = load_dataset("json", data_files=cfg.DATASET_PATH)
dataset = dataset["train"].train_test_split(test_size=0.05)

# 启动训练
trainer = SFTTrainer(
    model=model,
    args=train_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    peft_config=lora_config,
    tokenizer=tokenizer,
    max_seq_length=cfg.MAX_SEQ_LEN
)

print("🚀 开始训练...")
trainer.train()
trainer.save_model(cfg.LORA_SAVE_PATH)
print(f"✅ 训练完成！LoRA保存至：{cfg.LORA_SAVE_PATH}")
