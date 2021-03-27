""""
ISP: the idea is that I don't want to stick too many methods into one interface only.
"""
from abc import abstractmethod

"""Implementing a class containing multiple method is not a good idea, because you are forcing the user making use 
of all the methods contained in the main class."""
class Machine:

    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


""""
With a multifunction printer no problem in using the Machine root class, because it will implement all the methods.
"""
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


""""
What if we have an old printer supporting print functionality only? In this case we may use the same approach for the 
MultiFunctionPrinter, but this will be problematic, because you need to maintain all the methods. You can add comments
by saying the methods are not supported, but there could be a better approach.
"""
class OdlFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        pass #noop

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    def __init__(self, scanner, printer):
        self.scanner = scanner
        self.printer = printer

    @abstractmethod
    def print(self, document):
        self.printer.print(document)

    @abstractmethod
    def scan(self, document):
        self.scanner.scan(document)