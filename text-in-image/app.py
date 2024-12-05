from flask import Flask, render_template, request, jsonify
import os
from openai import AzureOpenAI
import base64
from dotenv import load_dotenv
from PIL import Image, ImageFilter
import numpy as np
from rembg import remove, new_session
from io import BytesIO

load_dotenv()

# 初始化rembg会话，这会触发模型下载（如果尚未下载）
try:
    print("Initializing rembg model...")
    session = new_session()
    print("rembg model initialized successfully")
except Exception as e:
    print(f"Error initializing rembg model: {e}")
    # 如果需要，这里可以添加更多的错误处理逻辑

app = Flask(__name__)

# 配置Azure OpenAI客户端
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    print("Received image generation request")
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # 读取图片数据并转换为base64
        image_data = file.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
        
        # 调用Azure OpenAI的GPT-4o mini API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "你是一个简洁的图片描述生成器。请用不超过10个字描述图片的核心内容。不要包含多余的修饰词。"
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "请用不超过10个字描述这张图片的核心内容。"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=50
        )
        
        caption = response.choices[0].message.content
        if len(caption) > 10:
            caption = caption[:10] + "..."
            
        return jsonify({'caption': caption})
    
    except Exception as e:
        print(f"Error in generate_caption: {str(e)}")  # 添加错误日志
        return jsonify({'error': str(e)}), 500

@app.route('/separate_layers', methods=['POST'])
def separate_layers():
    """处理图片分离前景和背景层
    
    请求参数:
        - image: 图片文件
    
    返回:
        - JSON对象，包含base64编码的背景层和前景层图片
    """
    print("Processing layer separation request...")
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # 读取图片
        image_data = file.read()
        image = Image.open(BytesIO(image_data))
        
        # 分离图层
        background, foreground = extract_background(image)
        
        # 将图层转换为base64
        background_buffer = BytesIO()
        background.save(background_buffer, format='PNG')
        background_base64 = base64.b64encode(background_buffer.getvalue()).decode('utf-8')
        
        foreground_buffer = BytesIO()
        foreground.save(foreground_buffer, format='PNG')
        foreground_base64 = base64.b64encode(foreground_buffer.getvalue()).decode('utf-8')
        
        return jsonify({
            'background_layer': f'data:image/png;base64,{background_base64}',
            'foreground_layer': f'data:image/png;base64,{foreground_base64}'
        })
    
    except Exception as e:
        print(f"Error in layer separation: {str(e)}")
        return jsonify({'error': str(e)}), 500

def extract_background(image):
    """提取图片的背景层和前景层，保持原始尺寸"""
    # 保存原始尺寸
    original_size = image.size
    
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    # 使用初始化的会话进行背景移除
    foreground = remove(image, session=session)
    
    # 确保前景图层尺寸与原图相同
    if foreground.size != original_size:
        foreground = foreground.resize(original_size, Image.Resampling.LANCZOS)
    
    # 转换为numpy数组以便更快的处理
    original_array = np.array(image)
    foreground_array = np.array(foreground)
    
    # 创建新的前景和背景数组
    new_foreground = np.zeros_like(original_array)
    new_background = np.zeros_like(original_array)
    
    # 获取alpha通道
    alpha = foreground_array[:, :, 3]
    
    # 对alpha进行预处理以减少抖动
    alpha_image = Image.fromarray(alpha)
    # 使用中值滤波去除噪点，保持边缘锐利
    alpha_image = alpha_image.filter(ImageFilter.MedianFilter(size=3))
    alpha = np.array(alpha_image)
    
    # 使用更严格的阈值处理
    alpha = np.where(alpha > 200, 255, alpha)  # 高透明度区域
    alpha = np.where(alpha < 50, 0, alpha)     # 低透明度区域
    
    # 对中间值区域进行处理，确保平滑过渡但不产生灰色区域
    mask = (alpha >= 50) & (alpha <= 200)
    alpha[mask] = np.where(alpha[mask] > 127, 255, 0)
    
    # 使用原始颜色创建前景和背景
    new_foreground[:, :, :3] = original_array[:, :, :3]
    new_foreground[:, :, 3] = alpha
    
    new_background[:, :, :3] = original_array[:, :, :3]
    new_background[:, :, 3] = 255 - alpha
    
    # 确保返回的图层尺寸与原图相同
    background = Image.fromarray(new_background)
    foreground = Image.fromarray(new_foreground)
    
    if background.size != original_size:
        background = background.resize(original_size, Image.Resampling.LANCZOS)
    if foreground.size != original_size:
        foreground = foreground.resize(original_size, Image.Resampling.LANCZOS)
    
    return background, foreground

if __name__ == '__main__':
    app.run(port=5001, debug=True)