from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
from math import pi

class Circle(Figure):
    TYPE = 'круг'

    @classmethod
    def type(cls):
        return cls.TYPE

    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color()
        self.color.parametr = color

    def square(self):
        return pi*(self.radius ** 2)

    def __repr__(self):
        return '{} {} радиусом {} площадью {}'.format(
            self.color.parametr,
            Circle.type(),
            self.radius,
            self.square()
        )