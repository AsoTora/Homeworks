"""Задача 7
Пользователь вводит строку и символ. В строке найти все
вхождения этого символа и перевести его в верхний регистр,
а также удалить часть строки, начиная с последнего вхождения этого символа и до конца.
"""

user_string = str(input("Enter your string here: "))
symb = input("Symbol: ")

# Переберем всю строку, Заменяя нужный символ на верхний регистр
c = -1
n = 0
user_string_new = ""  # Т.к. строка -- незменяемый объект

for i in user_string:
    c += 1  # Порядковый номер для i
    if i == symb:
        i = i.upper()
        n += 1  # Количество замен
    user_string_new += i
    if n == user_string.count(symb):
        user_string_new = user_string_new[:(c+1)]
        break

print(user_string_new)
