import jwt 
from flask import current_app

def generate_jwt(payload): 
    token = jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256') 
    return token

def verify_jwt(token): 
    try: 
        jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256']) 
        return True 
    except Exception: 
        return False 
