import subprocess
import config as cfg

print("📦 开始转换为 LM Studio 可用的 GGUF 格式...")

cmd = f'''
python -m llama_cpp.convert "{cfg.MERGED_MODEL_PATH}" ^
--outfile "{cfg.GGUF_OUTPUT_NAME}" ^
--quantize q4_k_m
'''

subprocess.run(cmd, shell=True)
print(f"✅ 转换完成！文件：{cfg.GGUF_OUTPUT_NAME}")
print("👉 直接拖入 LM Studio -> My Models 即可使用！")