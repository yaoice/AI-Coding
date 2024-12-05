# Smart Image Caption Generator

[English](README.md) | [中文](README_CN.md)

An intelligent image caption generation tool based on Flask and GPT-4 Vision, supporting automatic caption generation, layer separation, and caption style customization.

## Features

- 🤖 Intelligent caption generation powered by GPT-4 Vision
- 🎨 Automatic foreground and background layer separation
- ✨ Customizable caption styles (font size, color, weight, etc.)
- 📐 Caption position and angle adjustment (drag or slider control)
- 🖼️ Export images with captions
- 📱 Mobile-friendly responsive design

## Technical Stack

- Backend: Python Flask
- AI Model: Azure OpenAI GPT-4 Vision
- Image Processing: rembg, Pillow
- Frontend: HTML5, CSS3, JavaScript
- Server: Gunicorn
- System Service: Systemd

## Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/yaoice/AI-Coding.git
cd text-in-image
```

2. Create and activate the virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create `.env` file and add the following configuration:

```env
AZURE_OPENAI_KEY=your_azure_openai_key
AZURE_OPENAI_ENDPOINT=your_azure_endpoint
```

## Deployment Instructions

### Development Environment

1. Start the Flask application:

```bash
python app.py
```

2. Access: `http://localhost:5001`

### Production Environment

1. Configure the system service:

```bash
# Edit the service configuration file
sudo nano /etc/systemd/system/text-in-image.service
# Copy the content of text-in-image.service and modify the path and username according to your situation

# Create the log directory
sudo mkdir /var/log/text-in-image
sudo chown your_username:your_username /var/log/text-in-image
```

2. Start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl start text-in-image
sudo systemctl enable text-in-image
```

3. Check the service status:

```bash
sudo systemctl status text-in-image
```

## Project Structure

```
.
├── README.md                    # Project description document
├── requirements.txt             # Python dependency package list
├── app.py                      # Flask application main file
├── text-in-image.service       # Systemd service configuration file
├── start_text_in_image.sh      # Production environment startup script
├── static/                     # Static resource directory
│   └── uploads/                # Upload file directory
└── templates/
    └── index.html             # Frontend page template
```

## Usage Instructions

1. Upload an image: Click the "Select Image" button or drag the image to the specified area
2. Generate captions: Click the magic wand button, and the AI will automatically generate suitable captions
3. Customize styles:
   - Adjust font size, color, and weight
   - Adjust caption position by dragging or sliding the slider
   - Use the rotation slider to adjust the caption angle
4. Download the finished product: Click the "Download Image" button to save the image with captions

## Log View

```bash
# Access log
tail -f /var/log/text-in-image/access.log

# Error log
tail -f /var/log/text-in-image/error.log
```

## Notes

- Ensure that Azure OpenAI has been correctly configured with the key and endpoint
- When deploying in a production environment, it is recommended to configure a reverse proxy (such as Nginx) and SSL certificate
- The size of the uploaded image is recommended not to exceed 5MB
- It is recommended to use a modern browser for the best experience