
from flask import Blueprint, request 
from src.controllers import sensor_controller, auth_controller, device_controller, security_controller, system_controller

api_bp = Blueprint('api', __name__, url_prefix='/api')

def register_routes(app): # 传感器接口 api_bp.add_url_rule('/sensors/int:device_id/latest', view_func=lambda device_id: sensor_controller.get_latest(device_id), methods=['GET']) api_bp.add_url_rule('/sensors/int:device_id/history', view_func=lambda device_id: sensor_controller.get_history(device_id), methods=['GET'])

    # 设备控制接口
    api_bp.add_url_rule('/devices/<int:device_id>/command', view_func=device_controller.send_command, methods=['POST'])

    # 人脸识别日志查询接口
    api_bp.add_url_rule('/security/face_logs', view_func=security_controller.get_face_logs, methods=['GET'])

    # 用户认证接口
    api_bp.add_url_rule('/auth/login', view_func=auth_controller.login, methods=['POST'])

    # 系统模式切换接口
    api_bp.add_url_rule('/system/mode', view_func=system_controller.change_mode, methods=['POST'])

    app.register_blueprint(api_bp)

