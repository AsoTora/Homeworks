"""cоздать файл и записать в него данные пользователя"""

def writer(autoimp):
	with open("ourfile.txt", "w") as f:
		while 0:  # поменял с True для тестов
			us_inp = str(input("Press q to stop. Write here: "))
			if (us_inp == "q"):
				break
			f.write(us_inp + "\n")
		else:
			f.write(autoimp)

def reader():
	with open("ourfile.txt") as f:
		# print()
		output = f.read()
		return output  # для теста. Иначе поставил бы print(f.read())
	
if __name__ == "__main__":
	writer("aaa")
	if reader() == "aaa":
		print("Test passed")




