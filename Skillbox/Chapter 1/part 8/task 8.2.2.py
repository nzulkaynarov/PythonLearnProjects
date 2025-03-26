total_hours = int(input("Количество часов: "))
cell_count = 1
for hour in range(1, total_hours // 3 + 1):
    cell_count *= 2
    print("Прошло часов:", hour * 3)
    print("Количество клеток:", cell_count)
    print("Осталось часов:", total_hours - hour * 3)
print("Наблюдение завершено!")