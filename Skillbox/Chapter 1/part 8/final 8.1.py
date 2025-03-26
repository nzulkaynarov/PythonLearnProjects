month = 0
print("Информация о запасах гречки:")
for weight in range(96, -1, -4):
    month += 1
    print("Через", month, "месяц:", weight, "кг гречки в запасе")
print("Запасы гречки закончились.")