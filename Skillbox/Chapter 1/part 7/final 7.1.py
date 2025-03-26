passengers_summ = 0

for i in range(10):
    id_person = int(input('Введите номер человека: '))
    if id_person % 2 == 0 and id_person > 0:
        passengers_summ += 1

print('Количество корректных номеров (чётных и положительных): ', passengers_summ)