reverse_timer = int(input("Введите время для обратного отсчёта (в секундах): "))
timer_status = False

print("Таймер установлен на", reverse_timer, "секунд.")

for seconds in range(reverse_timer, 0, -1):
		print("Осталось секунд:", seconds)
		status = int(input("Введите 1, если еда готова, или 0, чтобы продолжить: "))
		if status == 1:
			timer_status = True
			print("Ваша еда готова, можете забрать! Таймер был прерван на", seconds, "секундах.")
			break
if not timer_status:
    print("Ваша еда готова. Осторожно, горячо!")