import math
number_count = int(input("Введите кол-во чисел: "))

for count in range(number_count):
    number = float(input("Введите число: "))
    if number > 0:
        rounded_number = math.ceil(number)
        print("x =", rounded_number, "log(x) = ", math.log(rounded_number))
    else:
        rounded_number = math.floor(number)  # Округляем вниз
        print(f"x = ", rounded_number, "exp(x) =", math.exp(rounded_number))