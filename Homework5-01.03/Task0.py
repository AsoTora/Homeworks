"""Задача 0
Дан список А1..AN. Найти элемент, который чаще всего встречается,
вывести его значение и количество повторений.
"""
def count():
# нахожу повтерение каждого эл-та, создавая словарь
	D1 = [1, 2, 3, 0, 1, 2, 3, 1, 2]
	counter = {}
	for i in D1:
	    counter[i] = counter.get(i, 0) + 1
	# если в ключе i словаря counter не будет значения, то оно станет 0 + 1 = 1
	# если будет, то оно станет i + 1
	return counter


# нахожу максимальное число, которое в ключах cреди значений словаря
def max():
	max_value = 0
	counter = count()
	for value in counter.values():
	    if value > max_value:
		max_value = value
	return max_value

# вывод тех значений в словаре, которые максимальны,т.е = max_value
def output():
	our_num = {k: v for k, v in count().items() if v == max()}
	return "Max value is/are {}, numb of repeat is/are {}".format(*(list(our_num.keys()), list(our_num.values())))



# c = {}
# D = [1, 2, 3, 0, 1, 2, 2, 3, 1]
# for i in D:
#     if i in c:
#         c[i] += 1  # для элемента в {с} с ключом i присвоить value += 1
#     else:
#         c[i] = 1
#
#
# def element(x):  # будет использоваться для c.items() => возвращает второй элемент для каждой пары в "с"
#     return x[1]
#
#
# """      max(c.items(), key=element_1)]
#  1) рассматривает(распаковывает) элементы словаря "c".
#  2) среди элементов ищет самый максимальный по ключу element_1
#  3) т.к. element_1 возвращает второе значение
# """
#
# print("Max value is {}, num is {}".format(*max(c.items(), key=element)))
# # * нужна т.к. max будет (1, 3), нужно распокавать их в 1 и 3 для форматирования

####################################################################################
