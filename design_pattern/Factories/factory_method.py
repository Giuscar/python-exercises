from cmath import cos, sin
from enum import Enum


class CoordinatesSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x} y: {self.y}'

    # def __init__(self, a, b, system=CoordinatesSystem.CARTESIAN):
    #     if system == CoordinatesSystem.CARTESIAN:
    #         self.x = a
    #         self.x = b
    #     elif system == CoordinatesSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    """We can add these methods into an inner Factory class"""
    # @staticmethod
    # def new_cartesian_point(x, y):
    #     return Point(x, y)
    #
    # @staticmethod
    # def new_polar_point(rho, theta):
    #     return Point(rho * cos(theta), rho * sin(theta))

    class PointFactory:
        def new_cartesian_point(self, x, y):
            p = Point()
            p.x = x
            p.y = y
            return p

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()


if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p, p2)