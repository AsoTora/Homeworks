"""Задача 8
Дан список кортежей grades = [(‘Ann’, 9), (‘John’, 7), (‘Smith’, 5), (‘George’, 6) ].
    Вывести информацию об оценках по возрастанию в виде:
    ‘Hello Ann! Your grade is 9’
"""

grades = [("Ann", 9), ("John", 7), ('Smith', 5), ("George", 6)]
grades = list(grades)


def getKey(item):
    return item[1]


grades.sort(key=getKey)
print(grades)

mystr = "Hello, {}! Your grade is {}!"
print(mystr, )

# for i in grades:
#     for el in i:
#         if type(el) == int:
#
#         if type(el) == str:
#             print(mystr.format(el))
#
#     print(i)
#
# print(type(grades))