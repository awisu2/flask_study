def read(app):
  config = {
    "dev": "app.config.DevelopConfig",
    "local": "app.config.LocalConfig",
    "default": "app.config.DefaultConfig"
  }
  app.config.from_object(config["default"])
  run_mode = "local"
  app.config.from_object(config[run_mode])
