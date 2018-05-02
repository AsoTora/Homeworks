"""
Задача 2
Для решений задач занятия №5 вынести общие части в модули. 
Сделать единую точку входа app.py. Необходимо реализовать возможность старта 
выполнения кода одного из заданий сразу после запуска программы, 
а также после его выполнения предоставить возможность выполнить другое задание
без повторного запуска программы.
"""
# sys.argv 
import sys
import importlib  
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , sys.argv[1:])

def hello():
	sys.path.append("/home/aso/studystuff/python130218/Homework5-01.03")  # мой путь
	inp_mod = str(sys.argv[1])

	try:
		importlib.import_module(inp_mod)  	#  __import__(inp)  -- один способ
	except ImportError as e:
		print("There is no such module")
	finally:
		pass #importlib.reload(inp_mod)

def go():
	while 1:
		inp = str(input("Enter next module (q to quit): "))
		if inp != "q":
			try:
				importlib.import_module(inp) 
			except (ImportError, ValueError):
				print("Error:")
			finally:
				pass #importlib.reload(inp)

		else:
			print("Finished")
			break

if __name__ == "__main__":
	hello()
	go()
