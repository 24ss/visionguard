# VisionGuard

VisionGuard is a minimal AI-based CCTV anomaly detection system using YOLOv8, OpenCV, and Flask.

## 🔧 Tech Stack

- Python
- OpenCV + YOLOv8
- Flask
- Docker
- GitHub Actions (CI)
- (Optional) React frontend

## 🚀 Quick Start

### Run Locally

1. Clone the repo:
```bash
git clone https://github.com/yourusername/VisionGuard.git
cd VisionGuard
```

2. (Optional) Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python backend/main.py
```

### Run with Docker

```bash
docker-compose up --build
```

## 📁 Structure

```
VisionGuard/
├── backend/
│   ├── main.py
│   ├── models/
│   ├── static/frames/
│   ├── utils.py
│   └── requirements.txt
├── frontend/ (optional)
├── sample_data/
│   └── test_video.mp4
├── docker-compose.yml
├── Dockerfile
└── .github/
    └── workflows/
        └── ci.yml
```

## ✅ Features

- Real-time anomaly detection using YOLOv8
- Flask API serving alert info
- Sample video included
- Minimal and functional

## 📷 Sample Input

Place your CCTV footage in `sample_data/` folder.

## 📦 Notes

- Keep it simple, keep it running.
- Focused on sudden movement and people anomalies.

