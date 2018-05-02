"""Задача 0
Написать программу, запрашивающую у пользователя строку с текстом и разделитель.
Необходимо вывести список слов с их длиной в начале слова, например, 5hello.
Для каждой из пользовательских функций написать функцию-тест.
"""

def inp():
	usstr = input("String here: ")
	r = input("Razdel: ")
	usstr = usstr.split(r)
	return usstr


def count(ustr):
	#ustr = inp()
	print(ustr)
	for i in range(len(ustr)):  # берет строку с длиной каждого слова(которые лежат в списке)
		ustr[i] = str(len(ustr[i])) + ustr[i]  # и складывает с самим словом, которое тоже строка
	return ustr


def tests():
	if count(['saddsa', 'dsdsadsa', 'dsadsadsa']) == ['6saddsa', '8dsdsadsa', '9dsadsadsa']:
		print(count(['saddsa', 'dsdsadsa', 'dsadsadsa']))
		print("tests are okay")
	else:
		print("errors")

tests()
