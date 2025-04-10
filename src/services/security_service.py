def query_face_logs(limit=None, start_time=None, end_time=None): # 模拟返回人脸识别日志数据 logs = [ {"time": "2025-03-31T12:00:00Z", "user_id": 1, "result": "accepted", "location": "Entrance A"}, {"time": "2025-03-31T12:05:00Z", "user_id": 2, "result": "denied", "location": "Entrance B"} ] if limit: logs = logs[:int(limit)] return logs EOF

