
a = int(input('первое число: '))
b = int(input('второе число: '))
numbers = [i for i in range(a, b+1) if i % 2 == 0]
print(numbers)