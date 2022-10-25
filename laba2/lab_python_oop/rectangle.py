from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    TYPE = 'прямоугольник'

    @classmethod
    def type(cls):
        return cls.TYPE

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color()
        self.color.parametr = color

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} шириной {} высотой {} площадью {}'.format(
            self.color.parametr,
            Rectangle.type(),
            self.width,
            self.height,
            self.square()
        )
