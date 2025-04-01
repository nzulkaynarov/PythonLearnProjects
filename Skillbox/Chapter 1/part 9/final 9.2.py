row_number = int(input('Введите кол-во рядов: '))
seat_number = int(input('Введите кол-во сидений в ряде: '))
meter_number = int(input('Введите кол-во метров между рядами: '))

print('\nСцена\n')
for rows in range(row_number + 1):
	print('=' * (seat_number + 1), '*' * (meter_number + 1),'=' * (seat_number + 1), end = '\n')