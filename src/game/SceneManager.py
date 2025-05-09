class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SceneManager(metaclass=Singleton):
    def __init__(self, scene):
        self._scene = scene

    def get_scene(self):
        return self._scene

    def set_scene(self, scene):
        self._scene = scene
