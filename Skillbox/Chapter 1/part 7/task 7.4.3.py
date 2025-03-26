start_work = int(input("Начало рабочего дня: "))
action_time = 0
count_work = 0

for time in range(start_work, 20):
	sport_time = int(input("Сколько минут вы занимались спортом: "))
	count_work += 1
	action_time += sport_time
	if action_time > 45:
		print("На сегодня спорта хватит")
		break
print("Вы работали", count_work, "ч.", "и занимались спортом", action_time, "минут")
