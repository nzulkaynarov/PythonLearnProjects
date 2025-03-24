ball = int(input('Сколько баллов набрал? '))
medal = int(input('Есть медаль? '))

if ball > 280 and medal == 1:
  print('Поздравляем! Ты поступил!')
else:
  print('К сожалению, ты не прошёл в наш университет.')