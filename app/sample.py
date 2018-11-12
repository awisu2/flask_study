def create_app(app):
  @app.route('/sample')
  def index():
      return "sample!"
