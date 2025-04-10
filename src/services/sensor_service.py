def get_latest_sensor_data(device_id): 
    return { "device_id": device_id, "type": "temperature", "value": 28.5, "timestamp": "2025-03-31T01:20:30+09:00" }

def get_sensor_history(device_id, start_time, end_time, aggregate=None): 
    data = [ {"timestamp": "2025-03-30T10:00:00Z", "value": 27.8}, {"timestamp": "2025-03-30T10:05:00Z", "value": 28.1}, {"timestamp": "2025-03-30T10:10:00Z", "value": 28.0} ] 
    if aggregate: 
        data = [{"timestamp": "2025-03-30T10:00:00Z", "value": 28.0}]
        return data

