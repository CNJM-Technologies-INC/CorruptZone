# models.py
from datetime import datetime, timedelta
from bson import ObjectId
from . import mongo
import uuid

class Report:
    INCIDENT_TYPES = [
        ('bribery', 'Bribery'),
        ('fraud', 'Fraud'),
        ('embezzlement', 'Embezzlement'),
        ('other', 'Other')
    ]
    
    @staticmethod
    def create(incident_type, description, latitude, longitude, evidence_files=None):
        report = {
            '_id': str(uuid.uuid4()),
            'incident_type': incident_type,
            'description': description,
            'location': {
                'type': 'Point',
                'coordinates': [longitude, latitude]
            },
            'created_at': datetime.utcnow(),
            'evidence_files': evidence_files or []
        }
        mongo.db.reports.insert_one(report)
        return report
    
    @staticmethod
    def get_recent(limit=5):
        return list(mongo.db.reports.find().sort('created_at', -1).limit(limit))
    
    @staticmethod
    def get_stats():
        total = mongo.db.reports.count_documents({})
        recent = mongo.db.reports.count_documents({
            'created_at': {'$gte': datetime.utcnow() - timedelta(days=30)}
        })
        locations = len(mongo.db.reports.distinct('location.coordinates'))
        
        by_type = {}
        for type_code, _ in Report.INCIDENT_TYPES:
            by_type[type_code] = mongo.db.reports.count_documents({'incident_type': type_code})
            
        return {
            'total_reports': total,
            'recent_reports': recent,
            'locations_count': locations,
            'reports_by_type': by_type
        }