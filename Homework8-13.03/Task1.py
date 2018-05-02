"""Задача 1
В текстовом файле посчитать количество строк, а также
для каждой отдельной строки определить количество в ней символов и слов.
"""
# opening
with open("students.txt") as f:  # from Task2
    text = f.read()
    num_lines = sum(1 for line in f)
    print("file input: ", text)


# counter
def counter():
    symb = 0
    words = 0
    for i in x:
        symb += len(i)
        words += len(i.split())  # криво, если будет разделение не только пробелами
    print("The ammount of str is: {}".format(num_lines))
    print("The ammount of words is: {}".format(words))
    print("The ammount of symb is: {}".format(symb))

if __name__ == "__main))":
	counter()


