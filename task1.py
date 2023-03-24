#создать функцию, которая прнимает лист объектов и год, машины которого надо оставить

if __name__ == '__main__':

    def car_year(li, year):

        l = []
        for i in li:
            if i.get_year() == year:
                l.append(i)
        return l


    class Car:

        def __init__(self, stamp, year, color):
            self.__stamp = stamp
            self.__year = year
            self.__color = color

        def set_year(self, year):
            if isinstance(year, str):
                try:
                    year = int(year)
                except Exception:
                    year = 2003

            if 2003 <= year <= 2023:
                self.__year = year

        def get_stamp(self):
            print(self.__stamp)

        def get_year(self):
            return (self.__year)


    YEAR = int(input())
    k = int(input())
    li = []

    for i in range(k):
        car1 = Car(input(), int(input()), input())
        li.append(car1)

    li = car_year(li, YEAR)

    for i in li:
        i.get_stamp()
