"""Задача 5
Сжать список, удалив из него все 0 и заполнить освободившиеся справа
элементы значениями -1.
"""
### 1 ###
# Получение массива
user_input = input("Enter here: ").split()

d = 0
for i in range(len(user_input)):
    el_num = i - d
    if user_input[el_num] == '0':
        user_input.append(user_input.pop(el_num))  # Каждый раз будет добавлять "0" в конец списка
        d += 1  # т.к. вылетел один элемент, надо учесть изменение нумерации
print(*b)


### 2 ###
user_input = []
while 1:
    user_input.append(input("Enter number here: "))
    if "" in user_input:
        user_input.remove("")
        break

# Получение нового списка без нулей и количество нулей в веденном списке
null = 0
new_spisok = []
for i in user_input:
    if i != "0":
        new_spisok.append(i)
    else:
        null += 1

# Итерация для добавления в новый список такого же кол-ва -1
for i in range(null):
    new_spisok.append("-1")

print(new_spisok)


### 3 ###

spisok = input("Enter numbers with space: ")
spisok = spisok.split()
null = spisok.count('0')

new_spisok = " ".join([i for i in spisok if i != "0"] + ["-1"]*null)
print(new_spisok)

