from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch
import config as cfg

print("🔗 开始合并基座模型 + LoRA...")

# 加载基座
model = AutoModelForCausalLM.from_pretrained(
    cfg.BASE_MODEL_PATH,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

# 加载LoRA
model = PeftModel.from_pretrained(model, cfg.LORA_SAVE_PATH)

# 合并权重
model = model.merge_and_unload()

# 保存
tokenizer = AutoTokenizer.from_pretrained(cfg.BASE_MODEL_PATH, trust_remote_code=True)
model.save_pretrained(cfg.MERGED_MODEL_PATH)
tokenizer.save_pretrained(cfg.MERGED_MODEL_PATH)

print(f"✅ 合并完成！模型保存至：{cfg.MERGED_MODEL_PATH}")