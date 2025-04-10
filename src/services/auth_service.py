from src.utils.jwt_handler import generate_jwt 
from datetime import datetime, timedelta

# 模拟用户数据；真实场景下应查询数据库

USERS = { "alice": {"password": "123456", "role": "admin"}, "bob": {"password": "password", "role": "user"} }

def authenticate_user(username, password): 
    user = USERS.get(username) 
    if user and user["password"] == password: 
        payload = { "username": username, "role": user["role"], "exp": datetime.utcnow() + timedelta(seconds=3600) } 
        token = generate_jwt(payload) 
        return {"token": token, "expires_in": 3600}
        return None 

