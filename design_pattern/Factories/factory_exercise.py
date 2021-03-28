""""
You are given a class called Person. The person has two attributes: id and name. Please implement a PersonFactory that
has a non-static create_person() method that takes a person's name and return a person initialized with this name and
an id. The id of the person should be set as a 0-based index of the object created. So, the first person the factory
makes should have Id=0, second Id=1 and so on.
"""


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    max_id = 0

    def create_person(self, name):
        if name:
            p = Person(self.max_id, name)
            self.max_id += 1
            return p

pf = PersonFactory()
print(pf.create_person("giuseppe"))
print(pf.create_person("carlo"))
print(pf.create_person("pino"))
