from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    TYPE = 'квадрат'

    @classmethod
    def type(cls):
        return cls.TYPE

    def __init__(self, side, color):
        self.side = side
        super().__init__(self.side, self.side, color)

    def __repr__(self):
        return '{} {} со стороной {} площадью {}'.format(
            self.color.parametr,
            Square.type(),
            self.side,
            self.square()
        )