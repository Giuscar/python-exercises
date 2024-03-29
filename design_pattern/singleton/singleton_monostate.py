""""
You keep all the data in a static variable and when you create a new object you just make a copy of the reference.
This is not he best approach.
"""


class CEO:
    __shared_state = {
        'name': 'Steve',
        'age': 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}'


if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)

    """"
    In this case if you change the age of ceo2, you will change it for ceo1 as well
    """
    ceo2 = CEO()
    ceo2.age = 77
    print(ceo2)
    print(ceo1)

    cfo1 = CFO()
    cfo1.name = 'Shery1'
    cfo1.money_managed = 1
    print(cfo1)
    cfo2 = CFO()
    cfo1.name = 'Ruth'
    cfo2.money_managed = 10
    print(cfo1)
    print(cfo2)