from flask import Flask, jsonify, request 
from src.routes.api_routes import register_routes 
from src.middleware.error_handler import register_error_handlers 
from src.middleware.authentication import jwt_required_middleware 
from src.utils.logger import setup_logger 

def create_app(config_object): 
    app = Flask(__name__) 
    app.config.from_object(config_object)
    # 初始化日志与数据库
    setup_logger(app)
    # init_db(app)

    # 注册 API 路由
    register_routes(app)

    # 注册全局错误处理器
    register_error_handlers(app)

    # JWT 验证中间件（除登录外所有接口）
    app.before_request(jwt_required_middleware)

    return app

if __name__ == '__main__': 
    from src.config.development import DevelopmentConfig 
    app = create_app(DevelopmentConfig) 
    app.run(host='0.0.0.0', port=5000, debug=True) 

