from lab_python_oop.square import Square

class Cube(Square):
    TYPE = 'куб'

    @classmethod
    def type(cls):
        return cls.TYPE

    def __init__(self, side, color):
        self.side = side
        super().__init__(self.side, color)

    def volume(self):
        return self.side ** 3

    def __repr__(self):
        return '{} {} со стороной {} объёмом {}'.format(
            self.color.parametr,
            Cube.type(),
            self.side,
            self.volume()
        )
