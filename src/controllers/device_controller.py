from flask import request, jsonify 
from src.services.device_service import send_device_command

def send_command(device_id): 
    data = request.get_json() 
    result = send_device_command(device_id, data) 
    if result.get("status") == "ok": 
        return jsonify(result), 200 
    else: 
        return jsonify(result), 400 
    

