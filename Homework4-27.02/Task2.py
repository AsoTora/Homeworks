""" Задача 2
Наийти и вывести все гласные буквы (без повторений),
которые встречаются в самом коротком слове. Текст запрашивается у пользователя.
 Алфавит использовать любой.

"""
# Получаю данные и преобразую их в массив из отдельных строк
user_text = input("Print your text here: ")
text_list = user_text.replace(",", "").replace(".", "").split(" ")
vovels = "eyuoiaуеыаоэяию"
vovels_U = vovels.upper()

# Нахожу в этом массиве самое короткое слово путем сравнивания всех длин
min_i = text_list[0]
for i in text_list:
    if len(i) <= len(min_i):
        min_i = i
print('The shortest word is: "' + min_i + '"')

# Создаем список глассных
ourvovels = []
for i in min_i:
    if (i in vovels) or (i in vovels_U):
        if i not in ourvovels:
            ourvovels.append(i)
    else:
        continue

# Вывод данных
if not ourvovels:  # проверяет, еввляется ли список пустым, т.е. False
    print('There is no vovels in the shortest word "' + min_i + '"')
else:
    print("The shortest word's \"" + min_i + "\" vovels are: ", ourvovels)
