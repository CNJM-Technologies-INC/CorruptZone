# app.py
from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from datetime import datetime, timedelta
import os
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/corruption_reports'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'pdf', 'mp3', 'mp4'}

# Initialize MongoDB
mongo = PyMongo(app)

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def save_file(file, report_id):
    if file and allowed_file(file.filename):
        filename = secure_filename(f"{uuid.uuid4()}_{file.filename}")
        upload_dir = os.path.join(app.config['UPLOAD_FOLDER'], str(report_id))
        os.makedirs(upload_dir, exist_ok=True)
        
        filepath = os.path.join(upload_dir, filename)
        file.save(filepath)
        return f'uploads/{report_id}/{filename}'
    return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/map')
def map_view():
    return render_template('map.html')

@app.route('/api/submit-report', methods=['POST'])
def submit_report():
    try:
        data = request.form
        latitude = float(data.get('latitude'))
        longitude = float(data.get('longitude'))
        incident_type = data.get('incident_type')
        description = data.get('description')
        
        if not all([latitude, longitude, incident_type, description]):
            return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400
        
        report_id = str(uuid.uuid4())
        evidence_files = []
        
        if 'evidence' in request.files:
            files = request.files.getlist('evidence')
            for file in files:
                file_path = save_file(file, report_id)
                if file_path:
                    evidence_files.append(file_path)
        
        report = {
            '_id': report_id,
            'incident_type': incident_type,
            'description': description,
            'location': {
                'type': 'Point',
                'coordinates': [longitude, latitude]
            },
            'created_at': datetime.utcnow(),
            'evidence_files': evidence_files
        }
        
        mongo.db.reports.insert_one(report)
        
        return jsonify({
            'status': 'success',
            'message': 'Report submitted successfully',
            'report_id': report_id
        })
        
    except Exception as e:
        app.logger.error(f"Error submitting report: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/get-reports')
def get_reports():
    try:
        reports = list(mongo.db.reports.find())
        features = [{
            'type': 'Feature',
            'geometry': report['location'],
            'properties': {
                'id': str(report['_id']),
                'incident_type': report['incident_type'],
                'description': report['description'],
                'created_at': report['created_at'].isoformat(),
                'has_evidence': bool(report['evidence_files'])
            }
        } for report in reports]
        
        return jsonify({
            'type': 'FeatureCollection',
            'features': features
        })
    except Exception as e:
        app.logger.error(f"Error getting reports: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/get-stats')
def get_stats():
    try:
        total = mongo.db.reports.count_documents({})
        recent = mongo.db.reports.count_documents({
            'created_at': {'$gte': datetime.utcnow() - timedelta(days=30)}
        })
        locations = len(mongo.db.reports.distinct('location.coordinates'))/2
        
        types = ['bribery', 'fraud', 'embezzlement', 'other']
        by_type = {t: mongo.db.reports.count_documents({'incident_type': t}) for t in types}
        
        return jsonify({
            'total_reports': total,
            'recent_reports': recent,
            'locations_count': locations,
            'reports_by_type': by_type
        })
    except Exception as e:
        app.logger.error(f"Error getting stats: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/get-recent-reports')
def get_recent_reports():
    try:
        limit = int(request.args.get('limit', 5))
        reports = list(mongo.db.reports.find().sort('created_at', -1).limit(limit))
        
        return jsonify([{
            'id': str(report['_id']),
            'incident_type': report['incident_type'],
            'description': report['description'],
            'created_at': report['created_at'].isoformat(),
            'has_evidence': bool(report['evidence_files']),
            'location': {
                'latitude': report['location']['coordinates'][1],
                'longitude': report['location']['coordinates'][0]
            }
        } for report in reports])
    except Exception as e:
        app.logger.error(f"Error getting recent reports: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
@app.route('/view-reports')
def view_reports():
    return render_template('view_reports.html')

@app.route('/api/get-filtered-reports')
def get_filtered_reports():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        type_filter = request.args.get('type', '')
        date_filter = request.args.get('date', 'all')
        search = request.args.get('search', '')
        
        query = {}
        
        if type_filter:
            query['incident_type'] = type_filter
            
        if date_filter != 'all':
            date_ranges = {
                'today': timedelta(days=1),
                'week': timedelta(days=7),
                'month': timedelta(days=30),
                'year': timedelta(days=365)
            }
            if date_filter in date_ranges:
                query['created_at'] = {
                    '$gte': datetime.utcnow() - date_ranges[date_filter]
                }
        
        if search:
            query['$or'] = [
                {'description': {'$regex': search, '$options': 'i'}},
                {'incident_type': {'$regex': search, '$options': 'i'}}
            ]
        
        total = mongo.db.reports.count_documents(query)
        reports = list(mongo.db.reports.find(query)
                      .sort('created_at', -1)
                      .skip((page - 1) * per_page)
                      .limit(per_page))
        
        return jsonify({
            'reports': [{
                'id': str(report['_id']),
                'incident_type': report['incident_type'],
                'description': report['description'],
                'created_at': report['created_at'].isoformat(),
                'has_evidence': bool(report['evidence_files']),
                'status': report.get('status', 'new'),
                'location': {
                    'latitude': report['location']['coordinates'][1],
                    'longitude': report['location']['coordinates'][0]
                }
            } for report in reports],
            'total': total,
            'page': page,
            'per_page': per_page
        })
        
    except Exception as e:
        app.logger.error(f"Error getting filtered reports: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)