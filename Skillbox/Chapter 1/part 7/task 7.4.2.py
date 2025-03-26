first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
summ_numbers = 0


for number in range(first_number, second_number + 1):
		summ_numbers += number

print("Сумма чисел от", first_number, "до", second_number, "равна"
"", summ_numbers)