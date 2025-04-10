from flask import request, jsonify 
from src.services.sensor_service import get_latest_sensor_data, get_sensor_history

def get_latest(device_id): 
    result = get_latest_sensor_data(device_id) 
    if result: 
        return jsonify(result), 200 
    else: 
        return jsonify({"error": "Device not found or unauthorized"}), 404

def get_history(device_id): 
    start_time = request.args.get("start") 
    end_time = request.args.get("end") 
    aggregate = request.args.get("aggregate") 
    history = get_sensor_history(device_id, start_time, end_time, aggregate) 
    return jsonify(history), 200 

