from threading import Lock
import sqlalchemy

class Db:
  _unique_instance = None
  _lock = Lock()  # クラスロック

  _engine = None

  def __new__(cls):
    raise NotImplementedError('Cannot initialize via Constructor')

  @classmethod
  def __internal_new__(cls, app):
    url = app.config['SQLALCHEMY_DATABASE_URI']
    cls._engine = sqlalchemy.create_engine(url, echo=True)
    return super().__new__(cls)

  @classmethod
  def get_instance(cls, app):
    if not cls._unique_instance:
        with cls._lock:
            if not cls._unique_instance:
                cls._unique_instance = cls.__internal_new__(app)
    return cls._unique_instance

  def get_connection(cls):
    return cls._engine.connect()
