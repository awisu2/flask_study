from app.libs.db import Db

def init_app(app):
  @app.route('/')
  def hello_world():
    return "hello"

  @app.route('/create')
  def create():
    try:
      db = Db.get_instance(app)
      connection = db.get_connection()
      print('engine', engine)
      # Create a new record
      sql = """CREATE TABLE `users` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `email` varchar(255) COLLATE utf8_bin NOT NULL,
          `password` varchar(255) COLLATE utf8_bin NOT NULL,
          PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
      AUTO_INCREMENT=1 ;"""
      connection.execute(sql)
    finally:
      connection.close()

    return "create"

  @app.route('/insert')
  def insert():
    try:
      db = Db.get_instance(app)
      connection = db.get_connection(app)
      # Create a new record
      sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
      connection.execute(sql, ('webmaster@python.org', 'very-secret'))
    finally:
      connection.close()

    return "inserted!"

  @app.route('/get')
  def read():
    try:
      db = Db.get_instance(app)
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
