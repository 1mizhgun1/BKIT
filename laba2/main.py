from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.cube import Cube
import numpy as np

def main():
    r = Rectangle(23, 23, 'синий')
    c = Circle(23, 'зеленый')
    s = Square(23, 'красный')
    cube = Cube(23, 'жёлтый')
    print(r)
    print(c)
    print(s)
    print(cube)

    a = np.array([[1, 2, 3], [4, 5, 6]], float)
    print(a)

if __name__ == "__main__":
    main()
