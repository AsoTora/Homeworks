"""Задача 2
В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. 
Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.
"""

# Создание файла + запись в него
with open("students.txt","w") as f:
    data = ["Mark Avr 8", "Andrew Shvedov 2", "Jan Abc 3"]
    f.writelines("\n".join(data))
    print(data, "\n")

with open("students.txt","r") as f:  # Закроет автоматически
    summa = 0
    c = 0  # для количества учащихся. Из условия можно взять и количество строк,
    # но я проверяю каждую строку на наличие оценки
    for i in f.readlines():
        nums = [int(j) for j in i if j.isdigit()]  # list comprehensions, только для чисел
        summa += nums[0]
        c += 1  
        if nums[0] <= 3:  
            print("The bad student is: ", i)

    print("\nCредний балл по классу = {}".format(round(summa/c,2)))
