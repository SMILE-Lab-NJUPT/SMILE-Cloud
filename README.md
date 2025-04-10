
# SMILE-Cloud

SMILE-Cloud是一个基于 RESTful API 设计的后端服务，项目隶属于SMILE团队的基于open Harmony的智能家居系统。


本项目提供设备控制、传感器数据获取、用户认证、人脸识别日志查询以及系统模式切换等接口。

## 目录结构
```bash
awesome-backend-project/
├── docs/
│   ├── api_spec.md           # API 接口详细说明文档，包括各接口功能、请求方法、URI、请求/响应示例
│   ├── architecture.md       # 系统架构设计文档，说明各模块之间的依赖与通信
│   ├── deployment.md         # 部署说明文档，包括 Docker、CI/CD、日志收集、监控等
│   └── testing.md            # 测试计划、单元测试、集成测试和压力测试说明
├── src/
│   ├── app.py                # 项目入口，初始化 Flask 应用、注册蓝图与中间件
│   ├── config/
│   │   ├── __init__.py
│   │   ├── development.py    # 开发环境配置（DEBUG、日志等）
│   │   └── production.py     # 生产环境配置（数据库、缓存、日志级别等）
│   ├── controllers/          # 控制器层，负责接收请求、调用服务层逻辑，返回响应
│   │   ├── auth_controller.py
│   │   ├── device_controller.py
│   │   ├── sensor_controller.py
│   │   ├── security_controller.py
│   │   └── system_controller.py
│   ├── models/               # 数据模型层，可基于 SQLAlchemy（或其他 ORM）建立数据库模型
│   │   ├── __init__.py
│   │   ├── device.py         # 设备模型（如设备ID、状态、注册信息等）
│   │   ├── face_log.py       # 人脸识别日志模型
│   │   ├── sensor_data.py    # 传感器数据模型（设备ID、数值、时间戳等）
│   │   └── user.py           # 用户管理模型
│   ├── routes/               # 路由层，将所有接口映射到对应的控制器
│   │   └── api_routes.py
│   ├── services/             # 业务逻辑层，各模块的服务代码封装核心逻辑
│   │   ├── auth_service.py
│   │   ├── device_service.py
│   │   ├── sensor_service.py
│   │   ├── security_service.py
│   │   └── system_service.py
│   ├── middleware/           # 中间件层，实现身份认证、错误处理、权限校验等
│   │   ├── authentication.py
│   │   └── error_handler.py
│   ├── utils/                # 工具函数层，如日志记录、JWT 处理、数据库连接等
│   │   ├── db.py
│   │   ├── jwt_handler.py
│   │   └── logger.py
│   └── tests/                # 测试代码，包括单元测试与集成测试
│       ├── test_auth.py
│       ├── test_device.py
│       ├── test_sensor.py
│       ├── test_security.py
│       └── test_system.py
├── .gitignore                # Git 忽略文件（如虚拟环境、日志、临时文件等）
├── requirements.txt          # Python 项目依赖包列表
├── README.md                 # 项目简介、功能、安装使用、部署说明
├── Dockerfile                # 基于 Docker 的容器化部署说明
└── docker-compose.yml        # Docker Compose 文件，定义服务、数据库、缓存等

```

## 项目特点

* 模块化设计：Controller, Service, Model, Middleware, Utils 等分层架构。
    
* 完整文档：包含 API 规范、系统架构、部署与测试说明。
    
* Docker 支持：提供 Dockerfile 与 docker-compose.yml，便于容器化部署。
    
* 丰富测试：单元测试与集成测试覆盖主要功能。
    

## 快速上手

1. 克隆仓库：
   ```bash
   git clone https://github.com/SMILE-Lab-NJUPT/SMILE-Cloud.git
   cd SMILE-Cloud
   ```
    
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
    
3. 运行项目（开发环境）：
   ```bash
   python src/app.py
   ```
    
4. 运行单元测试：
   ```bash
   pytest src/tests/
   ```
    

## 部署说明

详见 docs/deployment.md

