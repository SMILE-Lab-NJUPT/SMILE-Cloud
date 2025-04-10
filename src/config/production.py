
class ProductionConfig: 
    DEBUG = False 
    SECRET_KEY = 'prod-secret-key' 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@db:3306/prod_db' 
    JWT_SECRET_KEY = 'your-jwt-production-secret'

