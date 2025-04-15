def numeral_count(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def numeral_check(n):
    max_count = 0
    max_number = 0
    for _ in range(1, n + 1):

        new_value = int(input("Введите число: "))
        if new_value < 0:
            new_value = 0

        cipher_count = numeral_count(new_value)
        if cipher_count > max_count:
            max_count = cipher_count
            max_number = new_value

    return max_number


how_many = int(input("Введите количество чисел: "))
print("Первая задача на обработку: ", numeral_check(how_many))
