 
# config.py
import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/corruption_reports'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'mp3', 'mp4'}