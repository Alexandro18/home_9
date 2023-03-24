#Создать текстовый файл, в котором будут хранится данные о людях (1 строка, один объект).
#Нужно из файла сделать эксель таблицу

import pandas

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

    n, l, a = [], [], []

    for i in f:
        s = i.split()
        n.append(s[0])
        l.append(s[1])
        a.append(s[2])

    d = {'name': n,
         'lastname': l,
         'age': a}

    p = pandas.DataFrame(d)
    writter =pandas.ExcelWriter('output.xlsx')
    p.to_excel(writter, 'Люди')
    writter.save()

    f.close()