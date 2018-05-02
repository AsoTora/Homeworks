"""Задача 4
Реализовать программу, которая выводит содержимое каталога в файловой системе.
Путь к каталогу запрашивается у пользователя.
"""
import os


print("The initial dir:", os.listdir("/home/aso/studystuff/python130218/Homework8-13.03/"))

for files in os.walk("/home/aso/studystuff/python130218/Homework8-13.03/"):
    print("Files: ", files)

inp = str(input("Enter path: "))
print("The user dir:", os.listdir(inp))



