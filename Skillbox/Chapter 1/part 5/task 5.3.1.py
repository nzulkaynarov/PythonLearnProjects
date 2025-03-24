weight_1 = int(input('Введите вес первого груза: '))
weight_2 = int(input('Введите вес второго груза: '))

if weight_1 < weight_2:
  print('Первый груз легче второго.')
elif weight_1 > weight_2:
  print('Второй груз легче первого.')
else:
  print('Оба груза весят одинаково.')