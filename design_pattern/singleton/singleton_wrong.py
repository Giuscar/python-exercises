""""
Whenever a class is instantiated __new__ and __init__ methods are called. __new__ method will be called when an object
is created and __init__ method will be called to initialize the object. In the base class object, the __new__ method is
defined as a static method which requires to pass a parameter cls. cls represents the class that is needed to be
instantiated, and the compiler automatically provides this parameter at the time of instantiation.
"""
import random


class Database:
    _instance = None

    def __init__(self):
        id = random.randint(1, 101)
        print('Loading a database from file {}'.format(id))

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls) \
                .__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    """"Even if the Database is instanciated once, the initizializer is called everytime you call Database.
        That's the wrong way of dealing with Singletons. 
    """
    print(d1 == d2)