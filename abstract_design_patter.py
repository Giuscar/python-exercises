from abc import ABC, abstractmethod

class AbstractOperation(ABC):
    def __init__(self, valueA, valueB):
        self.valueA = valueA
        self.valueB = valueB
        super().__init__()

    @abstractmethod
    def executeOperation(self):
        print('This is the main class')
        pass

class SumOperation(AbstractOperation):
    def executeOperation(self):
        return self.valueA + self.valueB

class DiffOperation(AbstractOperation):
    def executeOperation(self):
        return self.valueA - self.valueB

class mainClass:
    def do_something(self):
        print('Main class')

class derClass(mainClass):
    def do_something(self):
        print('Derived class')


if __name__ == "__main__":
    sum = SumOperation(1, 2).executeOperation()
    print(sum)
    diff = DiffOperation(3, 4).executeOperation()
    print(diff)

    mainClass = derClass().do_something()

    #List comprehension
    vector1 = [1, 2, 3, 4, 5, 6, 7]
    vector2 = [1, 4, 6]
    res = [item for item in vector1 if item%2 == 0]
    print(res)
