temp = int(input("сколько температура? "))
dist = 0
while temp > 15:
  dist += 20
  temp -= 2
  if temp <= 15:
    break
  dist += 10
print("дистанция: ", dist)