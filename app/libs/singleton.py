from threading import Lock

class Singleton:
  _unique_instance = None
  _lock = Lock()  # クラスロック

  def __new__(cls):
    raise NotImplementedError('Cannot initialize via Constructor')

  @classmethod
  def __internal_new__(cls, **args):
    return super().__new__(cls)

  @classmethod
  def get_instance(cls, **args):
    if not cls._unique_instance:
        with cls._lock:
            if not cls._unique_instance:
                cls._unique_instance = cls.__internal_new__(**args)
    return cls._unique_instance


