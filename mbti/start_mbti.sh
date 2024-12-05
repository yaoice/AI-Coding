#!/bin/bash

# 激活Python虚拟环境（如果有的话）
# source /path/to/your/venv/bin/activate

# 设置工作目录
cd /home/your_username/mbti_test

# 设置Flask运行环境
export FLASK_APP=mbti_test.py
export FLASK_ENV=production

# 启动Flask应用（使用gunicorn，更适合生产环境）
gunicorn -w 4 -b 0.0.0.0:5000 mbti_test:app