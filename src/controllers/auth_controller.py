from flask import request, jsonify 
from src.services.auth_service import authenticate_user

def login(): 
    data = request.get_json() 
    username = data.get("username") 
    password = data.get("password") 
    token_data = authenticate_user(username, password) 
    if token_data: 
        return jsonify(token_data), 200 
    else: 
        return jsonify({"error": "Invalid credentials"}), 401 

