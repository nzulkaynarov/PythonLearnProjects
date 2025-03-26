n = int(input("Введите число: "))
summ_number = 0
for number in range(1, n+1, 5):
	print("Номер стула: ", number)
	summ_number += number
print("Сумма: ", summ_number)