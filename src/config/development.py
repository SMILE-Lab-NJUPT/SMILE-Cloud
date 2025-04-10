class DevelopmentConfig: 
    DEBUG = True 
    SECRET_KEY = 'dev-secret-key' 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db' 
    JWT_SECRET_KEY = 'your-jwt-secret' 


# src/config/production.py

