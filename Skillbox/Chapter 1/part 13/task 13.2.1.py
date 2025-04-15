def sum_n(number):
	sum_numbers = 0
	for numbers in range(1, number + 1):
		sum_numbers += numbers
	
	return sum_numbers

def next_sum(sum_numbers):
	new_sum = 0
	for numbers in range(1, sum_numbers + 1):
		new_sum += numbers
	
	return new_sum

number = int(input('Введите число: '))
sum_numbers = sum_n(number)
new_sum = next_sum(sum_numbers)
print('Сумма от 1 до', number, 'равна', sum_numbers)
print('Сумма от 1 до', sum_numbers, 'равна', new_sum)