
from datetime import datetime 
from src.models import db

class SensorData(db.Model): 
    __tablename__ = 'sensor_data' 
    id = db.Column(db.Integer, primary_key=True) 
    device_id = db.Column(db.Integer, nullable=False) 
    sensor_type = db.Column(db.String(50), nullable=False) 
    value = db.Column(db.Float, nullable=False) 
    timestamp = db.Column(db.DateTime, default=datetime.utcnow) 
