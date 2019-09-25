# 1) Написать программу поиска суммы минимального и максимального
# из трех введенных чисел

"""
# Хорошее решение
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

L = [x, y, z]
lmax = max(L)
lmin = min(L)

print(lmax + lmin)
"""

# Еще более кривое решение
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))


def min(a, b, c):
    if a < b:
        if a < c:
            return (a)
    if b < a:
        if b < c:
            return (b)
    if c < a:
        if c < b:
            return (c)


def max(a, b, c):
    if a > b:
        if a > c:
            return (a)
    if b > a:
        if b > c:
            return (b)
    if c > a:
        if c > b:
            return (c)

print("The sum is:", min(a, b, c) + max(a, b, c))
