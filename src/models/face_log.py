
from datetime import datetime 
from src.models import db

class FaceLog(db.Model): 
    __tablename__ = 'face_logs' 
    id = db.Column(db.Integer, primary_key=True) 
    time = db.Column(db.DateTime, default=datetime.utcnow) 
    user_id = db.Column(db.Integer) 
    result = db.Column(db.String(20)) 