""" Дана строка ‘Hello!Anthony!Have!A!Good!Day!’. Создать список, 
состоящий из отдельных слов[‘HELLO’, ‘ANTHONY’, ‘HAVE’, ‘A’, ‘GOOD’, ‘DAY’].
"""

mystr = "Hello!How!Are!you?!"
s = mystr.upper().split("!")
s.remove("")

print(s)

