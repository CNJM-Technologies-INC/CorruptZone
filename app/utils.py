 
# utils.py
import os
from werkzeug.utils import secure_filename
from . import mongo
import uuid

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_file(file, report_id, app_config):
    if file and allowed_file(file.filename, app_config['ALLOWED_EXTENSIONS']):
        filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
        upload_dir = os.path.join(app_config['UPLOAD_FOLDER'], str(report_id))
        os.makedirs(upload_dir, exist_ok=True)
        
        filepath = os.path.join(upload_dir, filename)
        file.save(filepath)
        return f'uploads/{report_id}/{filename}'
    return None