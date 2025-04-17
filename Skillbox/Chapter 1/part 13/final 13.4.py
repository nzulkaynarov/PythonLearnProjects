def count_numbers(number):
	num_count = 0
	temp = number
	while temp > 0:
		num_count += 1
		temp = temp // 10
	return num_count

def change_number(number):
    digits_count = count_numbers(number)
    last_digit = number % 10
    first_digit = number // 10 ** (digits_count - 1)
    between_digits = number % 10 ** (digits_count - 1) // 10
    new_number = last_digit * 10 ** (digits_count - 1) + between_digits * 10 + first_digit
    return new_number

def main():
	first_n = int(input("Введите первое число: "))
	if count_numbers(first_n) < 3:
		print("В первом числе меньше трёх цифр.")
	else:
		print('Изменённое первое число:', change_number(first_n))
	second_n = int(input("\nВведите второе число: "))
	if count_numbers(second_n) < 4:
		print("Во втором числе меньше четырёх цифр.")
	else:
		print('Изменённое второе число:', change_number(second_n))
		print('\nСумма чисел:', first_n + second_n)

main()