# Задача 3. Полученный список из задачи 2 вывести столбиком в отсортированном порядке.


mystr = "Hello!How!Are!you?!"

s = mystr.upper().split("!")
s.remove("")
s.sort(key=None)

for i in s:
	print(i)

