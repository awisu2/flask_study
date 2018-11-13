from app.libs import db

def init_app(app):
  @app.route('/')
  def hello_world():
    return "hello"

  @app.route('/create')
  def create():
    try:
      engine = db.get_connection(app)
      # Create a new record
      sql = """CREATE TABLE `users` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `email` varchar(255) COLLATE utf8_bin NOT NULL,
          `password` varchar(255) COLLATE utf8_bin NOT NULL,
          PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
      AUTO_INCREMENT=1 ;"""
      engine.execute(sql)
    finally:
      engine.close()

    return "create"

  @app.route('/insert')
  def insert():
    try:
      engine = db.get_connection(app)
      # Create a new record
      sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
      engine.execute(sql, ('webmaster@python.org', 'very-secret'))
    finally:
      engine.close()

    return "inserted!"

  @app.route('/get')
  def read():
    try:
      engine = db.get_connection(app)
      print('engine', engine)

      # Read a single record
      sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
      rows = engine.execute(sql, ('webmaster@python.org',))
    finally:
      engine.close()

    result = ""
    for v in rows:
      result += str(v)

    return result
