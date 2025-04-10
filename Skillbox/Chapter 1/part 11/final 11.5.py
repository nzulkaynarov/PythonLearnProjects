earth_volume = 1.08321 * 10 ** 12
random_radius = float(input("Введите радиус случайной планеты: "))
random_volume = (4 / 3) * 3.14 * random_radius ** 3
if earth_volume > random_volume:
		print('Объём планеты Земля больше в', round(earth_volume / random_volume, 3), 'раз') 
else:
		print('Объём планеты Земля меньше в', '(1 /', round(earth_volume / random_volume, 3), ') =' , round(random_volume / earth_volume, 3), 'раз')
