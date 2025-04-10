
# SMILE-Cloud

SMILE-Cloud是一个基于 RESTful API 设计的后端服务，项目隶属于SMILE团队的基于open Harmony的智能家居系统。


本项目提供设备控制、传感器数据获取、用户认证、人脸识别日志查询以及系统模式切换等接口。

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

详见 docs/deployment.md EOF

