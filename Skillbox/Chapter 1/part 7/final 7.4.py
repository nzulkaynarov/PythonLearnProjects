start_segment = int(input('Введите начало отрезка: '))
end_segment = int(input('Введите конец отрезка: '))
summ = 0
count = 0

for i in range(start_segment, end_segment + 1):
	if i % 3 == 0:
		print(i)
		summ += i
		count += 1

print('Среднее арифметическое этих чисел: ', summ/count)