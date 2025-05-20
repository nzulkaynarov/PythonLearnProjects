number_int = int(input('Введите целое число: '))
number_dict = {}


for number in range(1, number_int + 1):
    number_dict[number] = number ** 2

print(number_dict)