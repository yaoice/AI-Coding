# MBTI职场性格测试应用

[English](./README.md) | [中文](./README_CN.md)

这是一个专业的MBTI（迈尔斯-布里格斯类型指标）职场性格测试Web应用，专注于帮助用户了解自己在职场中的性格特征和工作方向。

## 功能特点

- 提供10个专业的职场场景MBTI测试题
- 实时响应的现代化用户界面
- 进度条显示测试完成度
- 即时计算和显示测试结果
- 包含16种性格类型的详细职场特征描述
- 移动端友好的自适应设计

## 技术栈

- 后端：Python Flask
- 前端：HTML5, CSS3, JavaScript
- 服务器：Gunicorn
- 系统服务：Systemd

## 安装步骤

1. 确保系统已安装Python 3.7或更高版本

2. 克隆仓库：

```bash
git clone https://github.com/yaoice/AI-Coding.git
cd mbti
```

3. 安装依赖包：

```bash
pip install -r requirements.txt
```

## 运行应用

1. 在终端中进入项目目录

2. 运行Flask应用：

```bash
python mbti_test.py
```

3. 打开浏览器访问：
```
http://localhost:5000
```

## 项目结构

```
.
├── README.md               # 英文文档
├── README_CN.md           # 中文文档
├── requirements.txt        # Python依赖包清单
├── mbti_test.py           # Flask应用主文件
├── mbti.service           # Systemd服务配置文件
├── start_mbti.sh          # 生产环境启动脚本
└── templates
    └── index.html         # 前端页面模板
```

### 文件说明

- `mbti_test.py`: 包含Flask应用逻辑、MBTI测试题库和结果计算逻辑
- `mbti.service`: 用于将应用配置为系统服务的Systemd配置文件
- `start_mbti.sh`: 生产环境下使用Gunicorn启动应用的脚本
- `templates/index.html`: 包含响应式界面设计和前端交互逻辑的模板文件

## 使用说明

1. 访问网页后，你会看到一系列MBTI测试问题
2. 为每个问题选择最符合你的选项
3. 回答完所有问题后，点击"提交测试"按钮
4. 系统会立即显示你的MBTI类型和相应的性格描述

## 注意事项

- 请确保回答所有问题
- 选择最符合你真实想法的选项
- 测试结果仅供参考