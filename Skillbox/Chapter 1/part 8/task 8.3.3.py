time_wakeup = int(input('Введите время пробуждения: '))
summ_water = 0
summ_calories = 0

for hour in range(time_wakeup, 23, 3):
	summ_water += 1
	print('Сейчас ', hour, "часов")
	calories = int(input('Введите количество калорий: '))
	summ_calories += calories
print("Выпито воды: ", summ_water, "л")
print("Съедено калорий: ", summ_calories)