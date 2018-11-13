class DefaultConfig:
  SECRET_KEY = 'secret key!?'

class LocalConfig:
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@127.0.0.1/mydb?charset=utf8mb4'

class DevelopConfig:
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@db/mydb?charset=utf8mb4'

