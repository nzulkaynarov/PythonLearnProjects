numbers = [3,7,5]
degree = 1
new_number = 0

while True:
 number = int(input('Новое число: '))
 numbers.append(number)
 print('Текущий список чисел:', numbers)
 for i in numbers:
  print(i ** 2, i ** 3, i ** 4)
 print()
