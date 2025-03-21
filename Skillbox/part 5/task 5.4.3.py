temp = int(input("введите температуру "))

if temp < 0 or temp > 100:
  print("Danger!")
else:
  print("Температура в пределах нормы")