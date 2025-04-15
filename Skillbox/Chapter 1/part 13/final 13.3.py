def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10  
        reversed_num = reversed_num * 10 + digit
        number = number // 10
    return reversed_num

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("\nПервое число наоборот:", reverse_number(num1), "\nВторое число наоборот:", reverse_number(num2))