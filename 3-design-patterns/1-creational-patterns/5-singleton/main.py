


class SingletonMeta(type):
    _instances : dict[type["SingletonMeta"], object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, name : str) -> None:
        self.name = name


# Exemple d'utilisation du singleton
singleton1 = Singleton("Instance 1")
singleton2 = Singleton("Instance 2")

print(singleton1.name)  # Output: Instance 1
print(singleton2.name)  # Output: Instance 1 (même instance que singleton1)
print(id(singleton1) == id(singleton2), id(singleton1), id(singleton2))