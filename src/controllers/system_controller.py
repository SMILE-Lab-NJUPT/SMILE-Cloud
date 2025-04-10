
from flask import request, jsonify 
from src.services.system_service import change_system_mode

def change_mode(): 
    data = request.get_json() 
    mode = data.get("mode") 
    enable = data.get("enable") 
    result = change_system_mode(mode, enable) 
    if result.get("status") == "ok": 
        return jsonify(result), 200 
    else: 
        return jsonify(result), 400 


# src/models/**init**.py
