ip_address = "{0}.{1}.{2}.{3}"
count = 0
numbers = []
while count < 4:
    new_number = int(input("Введите число: "))
    if 0 <= new_number <= 255:
        numbers.append(new_number)
        count += 1
    else:
        print('Ошибка ввода!')

print(ip_address.format(*numbers))
# * полезный инструмент, но и без него можно справиться, вручную прописав элементы по индексам
print(ip_address.format(numbers[0], numbers[1], numbers[2], numbers[3]))
