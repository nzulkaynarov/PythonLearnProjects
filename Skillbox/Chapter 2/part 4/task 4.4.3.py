n = int(input("Введите количество чисел N: "))

numbers = [random.randint(-10, 10) for _ in range(n)]

a = random.randint(0, len(numbers) - 2)
b = random.randint(a + 1, len(numbers) - 1)
# Генерируем числа так, чтобы они не выходили за границу списка
print(numbers, a, b)
numbers = numbers[:a] + numbers[b + 1:]
print(numbers)