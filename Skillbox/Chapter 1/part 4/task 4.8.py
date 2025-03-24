x = int(input('Первое число '))
b = int(input('Второе число '))
c = int(input('Третье число '))
d = 0

if a > b:
  d = a
else:
  d = b
if d > c:
  print('Максимальное число ', d)
else:
  print('Максимальное число ', c)