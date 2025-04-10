from flask import request, jsonify 
from src.utils.jwt_handler import verify_jwt

def jwt_required_middleware():
    if request.path == '/api/auth/login': 
        return 
    auth_header = request.headers.get("Authorization") 
    if not auth_header: 
        return jsonify({"error": "Unauthorized, no token provided"}), 401 
    token = auth_header.replace("Bearer ", "") 
    if not verify_jwt(token): 
        return jsonify({"error": "Unauthorized, invalid token"}), 401

