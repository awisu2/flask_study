from app.libs.singleton import Singleton
import sqlalchemy

class Db(Singleton):
  _engine = None

  @classmethod
  def __internal_new__(cls, **args):
    url = args["app"].config['SQLALCHEMY_DATABASE_URI']
    cls._engine = sqlalchemy.create_engine(url, echo=True)
    return super().__internal_new__(**args)

  def get_connection(cls):
    return cls._engine.connect()
