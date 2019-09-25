""" Задача 6
Преобразовать массив так, чтобы сначала шли все отрицательные элементы,
а потом положительные(0 считать положительным). Порядок следования должен быть сохранен.
"""
# input: 1 4 3 2 0 0 5 4 -1 -2 -3 4 5
# output: -1 -2 -3 4 5 1 2 3 4 0 0 5 4

# 1. Получение массива
list1 = input("Input here: ").split()

# 2. Итерация по нему. Вынос всех положительных элементов в конец pop()
d = 0
for i in range(len(list1)):
    el_num = i - d
    if int(list1[el_num]) >= 0:
        list1.append(list1.pop(el_num))
        d += 1  # т.к. вылетел один элемент, надо учесть изменение нумерации
print(*list1)


#### СДЕЛАТЬ ЭТО СДВИГОМ
"""
# 1. Получение массива
list1 = input("Input here: ").split()

for i in range(len(list1)-1):
	if int(list1[i]) > 0:
		list1[i],list1[i+1] = list1[i+1],list1[i]
	else:
		continue
print(list1)
"""
