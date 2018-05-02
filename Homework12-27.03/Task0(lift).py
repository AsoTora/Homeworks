"""
Реализовать класс лифта Elevator. Класс должен обладать методом, lift, отвечающий за вызов лифта. 
При сложении/вычитании экземпляров класса должно возвращаться значение производимой математической операции. 
Если производить вычитание у лифта, который еще не совершал поднятий, должна быть выведена ошибка неправильной операции. Предусмотреть возможность сравнения какой из лифтов совершил большее количество поднятий.
Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
При строчных операциях необходимо вывести детальную информацию по лифту: наименование, количество поднятий и процент от общего количества поднятий всех лифтов. 
"""


class Elevator():
	common_counter = 0  # static value, common for all exemplars

	def __init__(self, name):
		self.counter = 0
		self.name = name

	def lift(self):  # кол-во вызовов лифта. Это НЕ поднятие на этаж, а именно кол-во
		self.counter += 1
		Elevator.common_counter += 1  # change static value

	def __add__(self, other):
		"""Позволяет складывать кол-во операций экземпляров"""

		if isinstance(other, Elevator):
			return "The sum: {}".format(str(self.counter + other.counter)) # У каждого экземпляра в __add__ возвращать lift.counter
		else:
			return "Cant operate with non-class objects"

	def __sub__(self, other): 
		"""Позволяет вычитать кол-во операций экземпляров"""

		if isinstance(other, Elevator):
			if self.counter <= 0:
				return "error, the lift {} wasnt moving".format(str(self.name))
			else:
				return "The sub: " + str(self.counter - other.counter)
		else:
			return "Cant operate with non-class objects"

	def __str__(self):
		try:
			return str(self.name) + ":: " + str(self.counter) + ", " + str(self.counter/Elevator.common_counter*100) + "%"
		except ZeroDivisionError:
			return str(self.name) + ":: " + str(self.counter) + ", " + str(0) + "%"


if __name__ == "__main__":
	lift1 = Elevator("Mogilev")
	lift1.lift()
	lift1.lift()
	lift2 = Elevator("Aaa")
	lift2.lift()
	lift3 = Elevator('Zero')

	if (lift1+lift2 == "The sum: 3") and (lift2-lift1 == "The sub: -1"):
		print("Sum and sub are OK")
	else:
		print('Error')