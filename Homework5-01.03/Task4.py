"""Задача 4*
Дана квадратная матрица А(N,N). Составить программу подсчета количества отрицательных элементов,
расположенных выше главной диагонали.
"""
def make_matrix(n=3):
	from random import randrange
	# n = int(input("Enter n: "))
	matrix = [[randrange(-100, 100) for i in range(n)] for j in range(n)]
		
	d = []  # Главная диагональ -- проведена из левого верхнего,т.e 1 эл-ту 1-го столбца к
	for i in range(len(matrix)):  # правому нижнему, т.e последнему эл-ту последнего стольца
		d.append(matrix[i][i])
	print("Matrix is:", matrix)
	print("Diagonal is:", d)
	return matrix


# Для 0-й строки проверяю каждый эл-т от [0+1] до [len()]
# Для 1-й эл-ты [1+1] до [len()]
# Для n-ной эл-ты [n+1] до [len()]
def elements():
	c = 0
	i_num = 0  # т.к. диагональ не считается. Если бы считалась, то начал бы с -1
	matrix = make_matrix()
	for i in range(len(matrix)):
		i_num += 1
		for j in range(i_num, len(matrix[i])):  # для каждой итерации j будет начинаться на 1 правее
			if matrix[i][j] < 0:
				c += 1
	return c


def test_fuct():
	try:
		print("\nThe ammount of negative elements above the diagonal is/are:", elements())
		print("\nTests are okay")
	except ValueError as err:
		print(err)
		print("\nAn error occured!")


test_fuct()
