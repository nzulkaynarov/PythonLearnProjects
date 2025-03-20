profit = int(input('ваща зп: '))
if profit < 0:
  print('Ошибка: доход не может быть отрицательным')
else:
  if profit < 10000:
    tax = profit * 13 / 100
    print('ваш налог состваляет: ', tax)
  elif profit > 50000:
    tax = profit * 30 / 100
    print('ваш налог состваляет: ', tax)
  else:
    tax = profit * 20 / 100
    print('ваш налог состваляет: ', tax)