""""
Python has a set of built-in methods and __call__ is one of them. The __call__ method enables Python programmers to
write classes where the instances behave like functions and can be called like a function. When the instance is called
as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).

object() is shorthand for object.__call__()
Example 1:


class Example:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")

# Instance created
e = Example()

# __call__ method will be called
e()
Output :

Instance Created
Instance is called via special method
Example 2:


class Product:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self, a, b):
        print(a * b)

# Instance created
ans = Product()

# __call__ method will be called
ans(10, 20)
Output :

Instance Created
200
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls) \
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)