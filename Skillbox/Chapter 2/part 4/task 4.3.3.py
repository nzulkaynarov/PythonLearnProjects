import random

first_army = [random.randint(50, 80) for _ in range(10)]
second_army = [random.randint(30, 60) for _ in range(10)]
third_army = ['Погиб' if first_army[i] + second_army[i] >= 100 else 'Выжил' for i in range(10)]
print(first_army)
print(second_army)
print(third_army)