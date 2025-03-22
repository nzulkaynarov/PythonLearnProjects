print("Программа для отслеживания температуры")
err_count = 0
stop_check = False
temp_sensor = -10

while not stop_check:
    temp = int(input("Какая температура на датчике? "))
    
    if temp == temp_sensor:
        print("Внимание: дублирующее значение температуры", temp, "обнаружено!")
        err_count += 1 
        print("Зафиксировано сбоев датчика: ", err_count)
        next_step = int(input("Хотите продолжить сбор данных? 1 — да, 0 — нет: "))
        if next_step == 0:
            print("Сбор данных остановлен!")
            stop_check = True
    else:
        temp_sensor = temp
 

