"""Задача 3
Вводятся строки. Определить самую длинную строку и вывести ее номер на экран.
Если самая длинная строка повторяется несколько раз, то вывести номера всех таких строк.
"""

# Получаем список наших строк
string_list = []
n = 0
while True:
    ourstr = input("Enter your string here. Enter or \"q\" to stop: ")
    if (ourstr == "") or (ourstr == "q"):
        break
    else:
        n += 1
        string_list.append(ourstr)

print("\nYour input is: ", *string_list)

# Нахожу в этом массиве самую длинную строку путем сравнивания всех длин
max_i = string_list[0]
for i in range(n):
    if len(string_list[i]) > len(max_i):
        max_i = string_list[i]

# СПОСОБ ПРОНУМЕРОВАТЬ ЛИСТ И ПОЛУЧИТЬ НОМЕРА СТРОК?
# Пройдем по нашему массиву еще раз, проверяя совпадения для самого большого числа.

for i in range(n):
    if len(max_i) == len(string_list[i]):
        print('The longest str is/are: "', string_list[i], '", index = ', i)

# СРАВНИВАТЬ СТРОКИ СРАЗУ, ИНДЕКС ПО counter
