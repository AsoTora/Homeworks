"""Задача 0
Написать программу, которая предлагает пользователю ввести список чисел, после чего
запрашивает число для которого нужно посчитать сколько раз оно встречается в списке.
"""
num_list = []


def user_input():
    print("type Enter or q to finish yor list")
    while True:
        i = input("Enter your number: ")
        if (i == "") or (i == "q"):
            print("finished")
            print("***" * 5)
            break
        try:
            i = float(i)
        except ValueError:
            print("This isnt a number! Just continue")
            continue
        num_list.append(i)
    return num_list


print("Here is your list:", user_input())


def user_counter():
    n = 0
    c = float(input("Counter is? "))
    for i in num_list:
        if c == i:
            n += 1
    return n


print("We meet counter", user_counter(), "times")


