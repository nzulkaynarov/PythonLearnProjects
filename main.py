start_sum = int(input("Введите стартовую сумму: "))

while x > 0:
  x = int(input("Сколько выпало на кубике? "))
  if x == 3:
    start_sum = 0
    print("Вы проиграли всё!")
    break
  
    
  print("Выиграли 500 рублей!")
  print("Игра закончена.")
  print("Итого осталось: ", start_sum, " рублей")

if x == 3:
  start_sum = 0
  print("Вы проиграли всё!")
  
  