def gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    gcd_find = 1
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            gcd_find = i

    return gcd_find


first_number = int(input("Первое число: "))
second_number = int(input("Второе число: "))
print("НОД=", gcd(first_number, second_number))