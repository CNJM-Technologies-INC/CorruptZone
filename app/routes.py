# routes.py
import uuid
from flask import Blueprint, render_template, jsonify, request, current_app
from .models import Report
from .utils import save_file
import json

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/api/submit-report', methods=['POST'])
def submit_report():
    try:
        data = request.form
        latitude = float(data.get('latitude'))
        longitude = float(data.get('longitude'))
        incident_type = data.get('incident_type')
        description = data.get('description')
        
        if not all([latitude, longitude, incident_type, description]):
            return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400
        
        evidence_files = []
        if 'evidence' in request.files:
            files = request.files.getlist('evidence')
            for file in files:
                file_path = save_file(file, str(uuid.uuid4()), current_app.config)
                if file_path:
                    evidence_files.append(file_path)
        
        report = Report.create(
            incident_type=incident_type,
            description=description,
            latitude=latitude,
            longitude=longitude,
            evidence_files=evidence_files
        )
        
        return jsonify({
            'status': 'success',
            'message': 'Report submitted successfully',
            'report_id': report['_id']
        })
        
    except Exception as e:
        current_app.logger.error(f"Error submitting report: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@main.route('/api/get-reports')
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
        current_app.logger.error(f"Error getting reports: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@main.route('/api/get-stats')
def get_stats():
    try:
        return jsonify(Report.get_stats())
    except Exception as e:
        current_app.logger.error(f"Error getting stats: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@main.route('/api/get-recent-reports')
def get_recent_reports():
    try:
        limit = int(request.args.get('limit', 5))
        reports = Report.get_recent(limit)
        return jsonify([{
            'id': str(report['_id']),
            'incident_type': dict(Report.INCIDENT_TYPES)[report['incident_type']],
            'description': report['description'],
            'created_at': report['created_at'].isoformat(),
            'has_evidence': bool(report['evidence_files']),
            'location': {
                'latitude': report['location']['coordinates'][1],
                'longitude': report['location']['coordinates'][0]
            }
        } for report in reports])
    except Exception as e:
        current_app.logger.error(f"Error getting recent reports: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500