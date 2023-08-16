from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError()

    @abstractmethod
    def umfang(self):
        raise NotImplementedError()


class Square(Figure):
    def __init__(self, a: float):
        self.__a = a

    def set_a(self, a: float):
        if a <= 0:
            raise ValueError()
        self.__a = a

    def get_a(self) -> float:
        return self.__a

    def area(self) -> float:
        return self.get_a() * self.get_a()

    def umfang(self) -> float:
        return self.get_a() * 4


class Circle(Figure):
    def __init__(self, radius: float):
        self.__radius = radius

    def set_radius(self, radius: float):
        if radius <= 0:
            raise ValueError()
        self.__radius = radius

    def get_radius(self) -> float:
        return self.__radius

    def area(self) -> float:
        return math.pi * self.get_radius() ** 2

    def umfang(self):
        return 2 * self.get_radius() * math.pi


if __name__ == '__main__':
    square1 = Square(5)
    print(square1.area())
    print(square1.umfang())

    circle1 = Circle(5)
    print(circle1.area())
    print(circle1.umfang())
