""" 3адача 1
Определить, является ли введенное слово идентификатором,
т.е. начинается ли оно с английской буквы в любом регистре или знака подчеркивания и не
содержит других символов, кроме букв английского алфавита (в любом регистре),
цифр и знака подчеркивания.
"""
str_allow = "0123456789"
str_Alph = "qwertyuioasdfghjklzxcvbnm_"
str_Alph_U = str_Alph.upper()

user_input = input("Type your world here: ")


def userinput():
    if user_input[0] in str_allow:
        return 0
    for i in user_input:
        if (i in str_allow) or (i in str_Alph) or (i in str_Alph_U):
            continue
        else:
            return 0
    return 1


if userinput() == 1:
    print("Your word", user_input, "is identefecator!")
else:
    print("Your word", user_input, "is not a identefecator!")

