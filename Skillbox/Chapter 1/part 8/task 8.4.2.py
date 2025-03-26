year = int(input('Введите год (не меньше 1900): ')) 

if year < 1900:
		print('Год должен быть не меньше 1900')
else:
	for number in range(year, 1900-1, -2):
		print(number)