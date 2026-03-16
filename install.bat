@echo off
REM 文件类型: 安装脚本
REM 用途: 一键环境安装

echo ============== 创建Python环境 ==============
conda create -n llm_train python=3.10 -y
conda activate llm_train

echo ============== 安装依赖 ==============
pip install --upgrade pip
pip install torch transformers peft bitsandbytes accelerate trl datasets sentencepiece protobuf llama-cpp-python

echo ============== 安装完成 ==============
pause
