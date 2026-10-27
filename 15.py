from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __add__(self, other):
        if isinstance(other, Circle):
            return self.area() + other.area()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.area() < other.area()
        return NotImplemented

    def __str__(self):
        return f"Circle(radius={self.radius})"


c1 = Circle(5)
c2 = Circle(3)

print(c1)
print("Area of circle 1:", round(c1.area(), 2))
print("Area of circle 2:", round(c2.area(), 2))
print("Combined areas:", round(c1 + c2, 2))
print("Are circles equal?", c1 == c2)
print("Is circle 1 smaller than circle 2?", c1 < c2)