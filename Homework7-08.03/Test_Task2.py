"""В матрице поменять местами 2 столбца. Заполняется пользователем. 
После запрос на столбцы, которые нужно поменять местами"""
"""
def matr():
	us_str = int(input("ammount of str: "))
	matrix = []
	for i in range(us_str):
		matrix.append([int(j) for j in input("Numbes here: ").split()])
	print(matrix)
	return matrix

matr()"""

def matr_compr():
	matrix0 = [[int(j) for j in input("Numbers here: ").split()] for i in range(int(input("ammount of str: ")))]
	print("Init matrix is:", matrix0, "\n")
	return matrix0


def change():
	matrix = matr_compr()
	a = int(input("1 st: "))
	b = int(input("2 st: "))
	try:
		matrix[a],matrix[b] = matrix[b],matrix[a]
		print("New matrix is:", matrix)
	except IndexError:
		print("there isnt such st")

change()