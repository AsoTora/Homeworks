""" Вводится строка. Найти самое длинное слово в ней и вывести его на экран. 
Если оно потворяется несколько раз, то вывести предыдушее самое длинное слово"""

get_str = input('Input a string: ')
list_split = get_str.split(' ')

num = list(map(lambda x: len(x), list_split))
no_repeat = list(filter(lambda ind: num.count(ind) < 2, num))  # возвращает список, в которых count всех номеров <2, т.е отфильтрует повторящиееся числа

our_max = list_split[num.index(max(no_repeat))] # 

print(our_max)


