# Задача 0: Дан список А1..AN. Вывести элементы списка в обратном порядке.


mylist = [1, 2, 3, 4, 5, 6, 7]

# 1 -- самый быстрый
mylist [::-1]
print(list(mylist [::-1]))

#2 -- чуть медленнее
print(list(reversed(mylist)))


# 3 -- удобный
def reversed_string(mylist):
    return mylist[:-1]

reversed_string(mylist)