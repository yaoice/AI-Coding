# 智能图片字幕生成器

[English](README.md) | [中文](README_CN.md)

一个基于Flask和GPT-4 Vision的智能图片字幕生成工具，支持自动生成字幕、图层分离和字幕样式自定义。

## 功能特点

- 🤖 基于 GPT-4 Vision的智能字幕生成
- 🎨 自动分离图片前景和背景层
- ✨ 支持字幕样式自定义（字体大小、颜色、粗细等）
- 📐 支持字幕位置和角度调整（拖拽或滑块控制）
- 🖼️ 支持导出带字幕的图片
- 📱 移动端友好的响应式设计

## 技术栈

- 后端：Python Flask
- AI 模型：Azure OpenAI GPT-4 Vision
- 图像处理：rembg, Pillow
- 前端：HTML5, CSS3, JavaScript
- 服务器：Gunicorn
- 系统服务：Systemd

## 安装步骤

1. 克隆仓库：

```bash
git clone https://github.com/yaoice/AI-Coding.git
cd text-in-image
```

2. 创建并激活虚拟环境（推荐）：

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

4. 配置环境变量：
创建 `.env` 文件并添加以下配置：

```env
AZURE_OPENAI_KEY=your_azure_openai_key
AZURE_OPENAI_ENDPOINT=your_azure_endpoint
```

## 部署说明

### 开发环境运行

1. 启动 Flask 应用：

```bash
python app.py
```

2. 访问：`http://localhost:5001`

### 生产环境部署

1. 配置系统服务：

```bash
# 编辑服务配置文件
sudo nano /etc/systemd/system/text-in-image.service
# 复制 text-in-image.service 的内容并根据实际情况修改路径和用户名

# 创建日志目录
sudo mkdir /var/log/text-in-image
sudo chown your_username:your_username /var/log/text-in-image
```

2. 启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl start text-in-image
sudo systemctl enable text-in-image
```

3. 检查服务状态：

```bash
sudo systemctl status text-in-image
```

## 项目结构

```
.
├── README.md                    # 项目说明文档
├── requirements.txt             # Python依赖包清单
├── app.py                      # Flask应用主文件
├── text-in-image.service       # Systemd服务配置文件
├── start_text_in_image.sh      # 生产环境启动脚本
├── static/                     # 静态资源目录
│   └── uploads/                # 上传文件目录
└── templates/
    └── index.html             # 前端页面模板
```

## 使用说明

1. 上传图片：点击"选择图片"按钮或拖拽图片到指定区域
2. 生成字幕：点击魔法棒按钮，AI 将自动生成合适的字幕
3. 自定义样式：
   - 调整字体大小、颜色和粗细
   - 通过拖拽或滑块调整字幕位置
   - 使用旋转滑块调整字幕角度
4. 下载成品：点击"下载图片"按钮保存带字幕的图片

## 日志查看

```bash
# 访问日志
tail -f /var/log/text-in-image/access.log

# 错误日志
tail -f /var/log/text-in-image/error.log
```

## 注意事项

- 确保已正确配置 Azure OpenAI 的密钥和端点
- 生产环境部署时建议配置反向代理（如 Nginx）和 SSL 证书
- 上传图片大小建议不超过 5MB
- 建议使用现代浏览器以获得最佳体验