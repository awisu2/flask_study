import os

configs = {
  "default": "app.config.DefaultConfig",
  "dev": "app.config.DevelopConfig",
  "local": "app.config.LocalConfig",
  "prod": "app.config.ProductionConfig"
}

def read(app):
  app.config.from_object(configs["default"])

  config_name = os.getenv('RUNMODE', 'dev')
  app.config.from_object(configs[config_name])
