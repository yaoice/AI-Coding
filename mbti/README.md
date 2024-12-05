# MBTI Workplace Personality Test Application

[English](./README.md) | [中文](./README_CN.md)

A professional MBTI (Myers-Briggs Type Indicator) workplace personality test web application focused on helping users understand their personality traits and work orientation in the workplace.

## Features

- 10 professional workplace scenario MBTI test questions
- Real-time responsive modern user interface
- Progress bar showing test completion
- Instant calculation and display of test results
- Detailed workplace characteristics for 16 personality types
- Mobile-friendly responsive design

## Tech Stack

- Backend: Python Flask
- Frontend: HTML5, CSS3, JavaScript
- Server: Gunicorn
- System Service: Systemd

## Installation

1. Ensure Python 3.7 or higher is installed

2. Clone the repository:
```bash
git clone https://github.com/yaoice/AI-Coding.git
cd mbti
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory in terminal

2. Run Flask application:
```bash
python mbti_test.py
```

3. Open in browser:
```
http://localhost:5000
```

## Project Structure

```
.
├── README.md               # Project documentation
├── README_CN.md           # Chinese documentation
├── requirements.txt        # Python dependencies
├── mbti_test.py           # Flask application main file
├── mbti.service           # Systemd service configuration
├── start_mbti.sh          # Production startup script
└── templates
    └── index.html         # Frontend template
```

### File Description

- `mbti_test.py`: Contains Flask application logic, MBTI test questions, and result calculation logic
- `mbti.service`: Systemd configuration file for setting up the application as a system service
- `start_mbti.sh`: Script for starting the application with Gunicorn in production
- `templates/index.html`: Template file containing responsive interface design and frontend interaction logic

## Usage Instructions

1. Visit the webpage to see a series of MBTI test questions
2. Choose the option that best fits you for each question
3. Click "Submit Test" after answering all questions
4. The system will immediately display your MBTI type and corresponding personality description

## Notes

- Please ensure all questions are answered
- Choose options that best reflect your true thoughts
- Test results are for reference only