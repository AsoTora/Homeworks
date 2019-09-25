"""Задача 3
Реализовать программу с базой учащихся группы. Записи по учащемуся: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы. Р
езультат выводить в удобочитаемом виде с порядковым номером записи.
"""
# name=jogh&age=12  -- No such student
# name=Andrew&age=18&name=Andrew&a--
# name=Kate&age=33


# Создать базу данных
# потом принять переменную
# потом искать по ней
# для проверки создать переменную с ключами!!!
d0 = {"name": "Andrew", "lastname": "Shvdevod", "gender":"m", "age": "18"}
d1 = {"name": "Kate", "lastname": "Whine", "gender": "f", "age": "20"}
d2 = {"name": "Kate", "lastname": "Urgant", "gender": "m", "age": "33"}
d3 = {"name": "Tan", "lastname": "Maslo", "gender": "f", "age": "15"}
d4 = {"name": "Winston", "lastname": "Shvarz", "gender": "m", "age": "42"}
base = [d0, d1, d2, d3, d4]


def inp():
	try:
		search = input("search: ").split("&")  # поиск по нескольким параметрам
		search = {k:v for k,v in [i.split("=") for i in search]}  # создание словаря с введенными параметрами
		return search
	except ValueError as e:
		print("ERROR:", e)


search = inp()


def check_keys(search):
	for i in search.keys():
		if i in base[0].keys():
			return 1
		else:
			return print("There is no such key \"{}\"".format(i))

def check_values(search,base):
	for i in base:
		if search.items() <= i.items():  # сравнивает dict ==> исключит ошибку, если один из параметров повторится
			return print("Num in base: {}, info: {}".format(base.index(i), [j for j in i.values()]))
	else:
		return print("No such student")


if __name__ == "__main__":
	if check_keys(search) == 1:
			check_values(search,base)

