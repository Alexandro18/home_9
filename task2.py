#Создать текстовый файл, в котором будут хранится данные о людях (1 строка, один объект).
#Нужно из файла сделать лист объкетов

if __name__ == '__main__':

    class Person:

        def __init__(self, name, lastname, age):
            self.name = name
            self.lastname = lastname
            self.age = age

        def info(self):
            print(f'name = {self.name}, lastname = {self.lastname}, age = {self.age}')

    k = int(input())
    f = open('data.txt', 'r+')

    for i in range(k):
        f.write(input() + '\n')

    f.seek(0)
    li = []

    for i in f:
        l = i.split()
        li.append(Person(l[0], l[1], l[2]))

    for i in li:
        i.info()
    f.close()




