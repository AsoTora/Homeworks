"""Задача 2
Дана вещественная матрица А(3,4). Составить программу подсчета количества элементов матрицы,
удовлетворяющих условию р1<=a(i,j)<=p2. Значения р1 и р2 запрашиваются у пользователя.
"""
def matrix_counter(p1=3, p2=4):
	from random import uniform  # возвращает рандомные вещественные числа

	#p1 = float(input("Enter p1: "))
	#p2 = float(input("Enter p2: "))

	n = 3  # количество строк матрицы
	m = 4  # кол-во эл-тов строки матрицы

	matrix = [[round(uniform(0, 10), 3) for i in range(m)] for j in range(n)]  # матрица, округление до 3-го знака
	print(matrix)

	c = 0  # с помощью коунтера посчитать кол-во подходящих эл-тов
	for i in range(n):
		for j in range(m):
			if (matrix[i][j] >= p1) and (matrix[i][j] <= p2):
				c += 1
	return c


# тест
def test_func():
    try:
        print("The number of elements р1<=a<=p2 is:", matrix_counter())
        print("\nThe program works!")
    except ValueError: 
        print("\nAn error occured!")


test_func()

