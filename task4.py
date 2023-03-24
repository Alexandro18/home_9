# Создать класс треугольник, в который принимаем длинны сторон.
# Записать в поле тип либо прямоугольный... и определить в поле характеристику угла острый/тупой

from math import *

if __name__ == '__main__':

    class Triangle:

        def __init__(self, ab, bc, ca):

            self.ab = ab
            self.bc = bc
            self.ca = ca

        def type_of_triangle(self):

            if self.ab + self.bc <= self.ca or self.ab + self.ca <= self.bc or self.bc + self.ca <= self.ab:
                print('Введенные размеры не могут являться сторонами треугольника')

            elif self.ab ** 2 + self.bc ** 2 == self.ca ** 2 or self.ab ** 2 + self.ca ** 2 == self.bc ** 2 or self.ca ** 2 + self.bc ** 2 == self.ab ** 2:
                print('Прямоугольный')

                if self.ab ** 2 + self.bc ** 2 == self.ca ** 2:
                    a = (asin(self.bc / self.ca))*180/pi
                    b = 90
                    c = (asin(self.ab / self.ca))*180/pi
                    print('Угол A = ', a, ' градусов')
                    print('Угол B = ', b, ' градусов')
                    print('Угол C = ', c, ' градусов')

                elif self.ab ** 2 + self.ca ** 2 == self.bc ** 2:
                    a = 90
                    b = (asin(self.ca / self.bc))*180/pi
                    c = (asin(self.ab / self.bc))*180/pi
                    print('Угол A = ', a, ' градусов')
                    print('Угол B = ', b, ' градусов')
                    print('Угол C = ', c, ' градусов')

                elif self.ca ** 2 + self.bc ** 2 == self.ab ** 2:
                    a = (asin(self.bc / self.ab))*180/pi
                    b = (asin(self.ca / self.ab))*180/pi
                    c = 90
                    print('Угол A = ', a, ' градусов')
                    print('Угол B = ', b, ' градусов')
                    print('Угол C = ', c, ' градусов')

            elif self.ab == self.bc == self.ca:
                print('Равносторонний')
                print('Угол A = 60 градусов')
                print('Угол B = 60 градусов')
                print('Угол C = 60 градусов')

            elif self.ab == self.bc or self.ab == self.ca or self.bc == self.ca:
                print('Равнобедренный')

                if self.ab == self.bc:
                    b = (acos(self.ca / (2*self.ab)))*180/pi
                    a = 180 - 2*b
                    print('Угол A = ', a, ' градусов')
                    print('Угол B = ', b, ' градусов')
                    print('Угол C = ', a, ' градусов')

                elif self.ab == self.ca:
                    a = (acos(self.bc / (2*self.ab)))*180/pi
                    b = 180 - 2 * a
                    print('Угол A = ', a, ' градусов')
                    print('Угол B = ', b, ' градусов')
                    print('Угол C = ', b, ' градусов')

                else:
                    a = (acos(self.ab / (2*self.ca)))*180/pi
                    c = 180 - 2 * a
                    print('Угол A = ', a, ' градусов')
                    print('Угол B = ', a, ' градусов')
                    print('Угол C = ', c, ' градусов')

            else:
                print('Произвольный')
                a = (acos((self.ab ** 2 + self.ca ** 2 - self.bc ** 2) / (2 * self.ab * self.ca)))*180/pi
                b = (acos((self.bc ** 2 + self.ab ** 2 - self.ca ** 2) / (2 * self.ab * self.bc)))*180/pi
                c = (acos((self.bc ** 2 + self.ca ** 2 - self.ab ** 2) / (2 * self.bc * self.ca)))*180/pi
                print('Угол A = ', a, ' градусов')
                print('Угол B = ', b, ' градусов')
                print('Угол C = ', c, ' градусов')

    tr = Triangle(10, 1, 1)
    tr.type_of_triangle()




