ball = 55000
balance = int(input('Сколько баллов у игрока? '))

if balance >= ball:
  balance -= ball
  if balance < 5000:
    balance += 1000
    print('Получен бонус')
  print('Артефакт успешно приобретён!')
else:
  print('Недостаточно баллов для покупки')

print('Остаток баллов: ', balance)
print('Удачной игры!')