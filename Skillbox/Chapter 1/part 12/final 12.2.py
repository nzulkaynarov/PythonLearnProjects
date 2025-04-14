def test(number):
	if number > 0:
		positive()
	elif number < 0:
		negative()
	else:
		print('Ноль')
		
def positive():
			print('Положительное ')

def negative():
			print('Отрицательное ')

number = int(input('Введите число: '))
test(number)
