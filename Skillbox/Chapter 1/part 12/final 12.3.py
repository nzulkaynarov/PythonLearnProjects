def menu(choice, item):
	if choice == 1:
		sum_item(item)
	elif choice == 2:
		max_item(item)
	elif choice == 3:
		min_item(item)


def sum_item(item):
	sum = 0
	for number in str(item):
		number = int(number)
		sum += number
	print('Сумма цифр: ', sum)

def max_item(item):
	max = 0
	for number in str(item):
		number = int(number)
		if number > max:
			max = number
	print('Максимальная цифра: ', max)

def min_item(item):
	min = 9
	for number in str(item):
		number = int(number)
		if number < min:
			min = number
	print('Минимальная цифра: ', min)

while True:
	item = int(input('Введите число: '))
	choice = int(input('Введите номер действия: \n1 - сумма цифр \n2 - максимальная цифра \n3 - минимальная цифра: '))
	menu(choice, item)
	print()