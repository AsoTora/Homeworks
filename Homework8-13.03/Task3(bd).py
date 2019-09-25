"""Задача 3
Реализовать программу с базой учащихся группы (данные хранятся в файле)
Записи по учащемуся: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы.
Результат выводить в удобочитаемом виде с порядковым номером записи.
"""


def filewrite():
    with open('students.txt') as f:
        num_lines = sum(1 for line in f)

    if num_lines < 4:  # добавить немного строк в бд
        with open("students.txt", "a") as f:
            new_marks = ["4 Anton Petuhov m 4", "\n5 Some WomanName f 9"]  # запись
            for i in new_marks:
                f.write(i)


def inp():
    try:
        search = input("search: ").lower().split("&")  # поиск по нескольким параметрам
        search = {k:v for k,v in [i.split(":") for i in search]}  # создание словаря с введенными параметрами
        return search
    except (ValueError, AttributeError) as e:
        print("ERROR:", e)
        return 0


def search_file():
    d = {}
    i = -1
    search = inp()

    with open("students.txt") as file:
        for line in file:
            i += 1
            for pare in line.split():
                key = pare.lower().split(":")[0]
                value = pare.lower().split(":")[1]
                d[key] = value

            if (search!= 0) and (search.items() <= d.items()):  # сравнивает dict'ы ==> сработает даже при повторении параметров
                    return print("Num in base: {}, info: {}".format(i, line))
            d.clear()
        else:
            return print("No such student")


# lastname:Avr&gender:m
# age:18&name:Some
if __name__ == "__main__":
    search_file()





###  Реализация через создание базы со словарем вида base = {0: {"name": "Andrew", "lastname": "Shvedov", }, 1: {}, ...}
###  Подумал, что это при прочтении большего файла, это будет простой перегрузкой памяти
###
#def read():
#     base = {}
#     i = -1
#     d = {}
#
#     with open("students.txt") as file:
#         for line in file:
#             i += 1
#
#             for pare in line.split():
#                 key = pare.lower().split(":")[0]
#                 value = pare.lower().split(":")[1]  # все время получал не те словари или "to many values to unpack"
#                 d[key] = value
#             base[i] = d
#             d = {}  # иначе получаю словарь тольско с последней строкой файла
#         return base  # как можно сделать это лучше?
#
#
# def search():
#     base = read()
#     print("BASE: ", base)
#     search = inp()
#
#     if search != 0:
#         for ind in base:
#             if search.items() <= base[ind].items():  # сравнивает dict'ы ==> сработает даже при повторении параметров
#                 return print("Num in base: {}, info: {}".format(ind, [j for j in base[ind].values()]))
#         else:
#             return print("No such student")
# lastname:Avr&gender:m
# age:18&name:Some
# if __name__ == "__main__":
#     search()






