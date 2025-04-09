import math

file_size = int(input("Укажите размер файла для скачивания: "))
download_speed = int(input("Какова скорость вашего соединения: "))
time = math.ceil(file_size / download_speed)
download_size = 0

for download_time in range(1, time + 1):
	download_size += download_speed
	download_percent = math.ceil(download_size / file_size * 100)
	if download_percent >= 100:
		download_size = file_size
		download_percent = 100
	print('Прошло', download_time, 'сек. Скачано', download_size, 'из', file_size, 'Мб', '(', download_percent, '%)')