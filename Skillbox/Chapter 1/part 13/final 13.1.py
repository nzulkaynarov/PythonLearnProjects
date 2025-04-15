def floating_point(number):
	counter = 0
	if number >= 1:
		while number >= 10:
			number /= 10
			counter += 1
	else:
		while number < 1:
			number *= 10
			counter -= 1
	number = round(number, 4)
	message = 'Формат плавающей точки: x = ' + str(number) + ' * 10 ** ' + str(counter)
	return message

float_number = float(input("Введите число: "))
result = floating_point(float_number)
print(result)