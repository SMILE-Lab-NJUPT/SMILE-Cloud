# API 接口规范说明

## 1. 获取传感器最新数据
- **方法:** GET  
- **URI:** `/api/sensors/{device_id}/latest`  
- **说明:** 用于查询指定设备的最近一次传感器读数  
- **请求参数:** device_id（路径参数）、授权令牌  
- **响应示例:**
```json
{
  "device_id": 101,
  "type": "temperature",
  "value": 28.5,
  "timestamp": "2025-03-31T01:20:30+09:00"
}
```

## 2. 获取传感器历史数据

* **方法:** GET
    
* **URI:** `/api/sensors/{device_id}/history`
    
* **说明:** 提供时间范围内的数据列表，可支持分页或聚合
    
* **请求参数:** start, end（Query 参数：ISO 时间字符串）
    
* **响应示例:**
    

```json
[
  {"timestamp": "2025-03-30T10:00:00Z", "value": 27.8},
  {"timestamp": "2025-03-30T10:05:00Z", "value": 28.1}
]
```

(其它接口请参照此规范编写) 
