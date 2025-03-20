cent_1 = int(input('введите вес первой монетки '))
cent_2 = int(input('введите вес второй монетки '))
cent_3 = int(input('введите вес третьей монетки '))

if cent_1 == cent_2:
  print('Третья легче')
elif cent_1 == cent_3:
  print('Вторая легче')
else:
  print('Первая легче')