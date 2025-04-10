
# 部署说明

## Docker 部署

* 使用 Dockerfile 构建应用镜像。
    
* docker-compose.yml 用于定义多容器应用（例如数据库、Redis 等）。
    
* 建议使用 Jenkins 或 GitLab CI/CD 进行持续集成与自动化部署。
    

## 环境变量配置

* 配置文件位于 `src/config/` 目录，通过环境变量选择加载（开发/生产）。 EOF
    
