start_work = int(input("Начало рабочего дня: "))
action_time = 0
count_work = 0

for time in range(start_work, 20):
	sport_time = int(input("Сколько минут вы занимались спортом: "))
	if action_time <= 45:
		break
	action_time += sport_time
	count_work += 1
print("Вы работали", count_work, "часа", "и занимались спортом", action_time, "минут")
