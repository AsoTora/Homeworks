# Задача 4. Обращение в письмах начинаются с фразы “Dear Mr./Mrs./Miss/Ms. ...“. 
# Необходимо определить и вывести пол человека, которому данное письмо адресовано. 
# Приглашение письма запрашивается у пользователя.

# Mrs/Mr -- male
# Miss/Ms -- female


mystr = input("please, wrote your mail here:", )

if 'Mrs' or 'Mr' in mystr:  ##!! с каких это пор миссис стала мужчиной?)
	print("This mail is for a male")
elif 'Miss' or 'Ms' in mystr:
	print("This mail is for a female")
else:
	print("Unfortunately, I cant say the gender of the adressant")

