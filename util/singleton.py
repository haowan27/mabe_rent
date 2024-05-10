class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print(cls)
            print(args)
            print(kwargs)
        return cls._instance

    def __init__(self, *args, **kwargs):
        print(self)
        print(args)
        print(kwargs)
        pass
