# Создать класс круг, принимать в конструктор радиус и на основе него расчитывать
# длинну окружности и площадь круга (делать в конструкторе)

from math import pi
if __name__ == '__main__':

    class Circle:

        def __init__(self, radius):
            self.radius = radius

        def circle_len(self):
            print(2 * pi * self.radius)

        def circle_square(self):
            print(pi * self.radius ** 2)

    c = Circle(5)
    c.circle_len()
    c.circle_square()

