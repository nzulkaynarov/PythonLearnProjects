average_salary = 0

for i in range(12):
		salary = int(input('Введите зарплату сотрудника: '))
		average_salary += salary

print('Средняя зарплата за год: ', average_salary / 12)