import sqlalchemy

def get_connection(app):
  url = app.config['SQLALCHEMY_DATABASE_URI']
  engine = sqlalchemy.create_engine(url, echo=True)
  return engine.connect()
