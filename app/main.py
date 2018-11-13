from app.libs.db import Db

def init_app(app):
  @app.route('/')
  def hello_world():
    return "hello"

  @app.route('/insert')
  def insert():
    try:
      db = Db.get_instance(app=app)
      connection = db.get_connection()
      # Create a new record
      sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
      connection.execute(sql, ('webmaster@python.org', 'very-secret'))
    finally:
      connection.close()

    return "inserted!"

  @app.route('/get')
  def read():
    try:
      db = Db.get_instance(app=app)
      connection = db.get_connection()

      # Read a single record
      sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
      rows = connection.execute(sql, ('webmaster@python.org',))
    finally:
      connection.close()

    result = ""
    for v in rows:
      result += str(v)

    return result
