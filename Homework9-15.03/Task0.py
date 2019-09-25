"""Сума цифр числа N без использования всего кроме рекурсии"""


def summa(N):
	if not N:
		return 0
	else:			
		return (N%10) + summa(N//10)
		
if __name__ == "__main__":
	if (summa(123) == 6) and (summa(666) == 18) and (summa(346) == 13):
		print("Tests passed")
