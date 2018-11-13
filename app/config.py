import os

class DefaultConfig:
  SECRET_KEY = 'secret key!?'

  # default env and auto reload
  ENV = 'development'
  DEBUG = True

class LocalConfig:
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@127.0.0.1/mydb?charset=utf8mb4'

class DevelopConfig:
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@db/mydb?charset=utf8mb4'

class ProductionConfig:
  ENV = 'production'
  DEBUG = False
  SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')

