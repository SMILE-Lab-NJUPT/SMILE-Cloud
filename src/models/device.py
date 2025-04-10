from src.models import db

class Device(db.Model): 
    __tablename__ = 'devices' 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=False) 
    status = db.Column(db.String(20), nullable=False, default='off') 
    # 可扩展其它设备相关字段 EOF
