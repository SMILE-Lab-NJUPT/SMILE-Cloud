
from flask import request, jsonify 
from src.services.security_service import query_face_logs

def get_face_logs(): 
    limit = request.args.get("limit") 
    start_time = request.args.get("start") 
    end_time = request.args.get("end") 
    logs = query_face_logs(limit, start_time, end_time) 
    return jsonify(logs), 200 

