# 5) Ввести три числа А,В,С. Удвоить каждое из них, если А>=В>=С, иначе поменять значения А и В.

# Способ с костылями
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a >= b and b >= c:
	a *= 2
	b *= 2
	c *= 2
else:
	a1 = a
	b1 = b
	b = a1
	a = b1
print(a, b, c)
"""
# Топ способ
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a >= b and b >= c:
	mylist = {a, b, c}
	print(mylist * 2)
else:
	mylist = [a, b]
	mylist.reverse()
	print(mylist, c)

"""