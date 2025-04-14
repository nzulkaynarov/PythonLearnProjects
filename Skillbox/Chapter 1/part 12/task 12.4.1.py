def calc(a, b,):
	number_sum = 0
	count = 0
	for number in range(a, b+1):
		number_sum += number
		count +=1
	print("Среднее арифметическое:", number_sum / count)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
		a, b = b, a
calc(a, b)
