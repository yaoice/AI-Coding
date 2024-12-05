#!/bin/bash

# 激活Python虚拟环境（如果有的话）
# source /path/to/your/venv/bin/activate

# 设置工作目录
cd /root/text-in-image

# 设置Flask运行环境
export FLASK_APP=app.py
export FLASK_ENV=production

# 启动Flask应用（使用gunicorn，更适合生产环境）
gunicorn -w 4 -b 0.0.0.0:5001 app:app
