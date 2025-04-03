number = int(input('Введите количество чисел: '))
simple_count = 0

for num in range(number):
    simple_num = int(input('Введите число: '))
    is_simple = True
    if simple_num > 1:
        for divisor in range(2, simple_num):
            if simple_num % divisor == 0:
                is_simple = False
                break
        if is_simple:
            simple_count += 1

print('Количество простых чисел в последовательности: ', simple_count)
