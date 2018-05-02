"""Задача 1
Дана целая матрица А(N,N). Составить программу подсчета среднего арифметического значения элементов матрицы.
"""
# input: [1, 2, 3], [1, 4, 5], [3, 8, 0]
# output: ((1+2+3)/3 + (1+4+5)/3 + (3+8+0)/3)3
def make_matrix():
	from random import randrange

	# Задаем матрицу через генератор
	n = int(input("Enter n: "))  # количество строк матрицы
	m = int(input("Enter m: "))  # кол-во эл-тов строки матрицы
	matrix = [[randrange(0, 10) for i in range(m)] for j in range(n)]
	return matrix


def n_mid():
    x = 0
    matrix = make_matrix()
    for i in matrix:
        x += sum(i)/len(i)  # считаю среднее арифметическое для каждой строки, сразу добавляя в общую сумму
    return x/len(matrix)


def test_func():
    try:
        print(n_mid())
        print("Tests are okay")
    except ValueError:
        print("An error occured")


test_func()






