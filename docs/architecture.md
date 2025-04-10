


# 系统架构设计文档

## 模块划分

* **Controller 层:** 处理请求，调用对应的服务。
    
* **Service 层:** 实现业务逻辑，独立于控制器。
    
* **Model 层:** 数据库模型定义，采用 ORM 技术管理数据持久化。
    
* **Middleware:** 实现认证、权限校验与全局错误处理。
    
* **Utils:** 公共工具，如数据库连接、日志处理、JWT 校验等。
    

## 数据流

1. 客户端调用 RESTful API 请求。
    
2. 路由映射至对应 Controller。
    
3. Controller 调用 Service 层处理业务逻辑。
    
4. Service 层与 Model 交互操作数据库（或调用其它服务）。
    
5. 响应经过 Middleware 处理后返回客户端。 

