number = int(input('Введите количество чисел: '))
max_sum = 0
max_num = 0

for num in range(number):
    current_num = input('Введите число: ')
    current_sum = 0
    for digit in current_num:
        current_sum += int(digit)

    if current_sum > max_sum:
        max_sum = current_sum
        max_num = int(current_num)

print('Число', max_num, 'имеет максимальную сумму цифр:', {max_sum})