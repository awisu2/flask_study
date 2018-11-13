from flask import Flask
from app.libs import config

app = Flask(__name__)
config.read(app)

def create_app():
  from .main import init_app
  init_app(app)

  return app

