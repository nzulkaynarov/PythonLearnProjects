def fluctuations(start, stop):
	count = 0
	while start > stop:
		start = start * 0.916
		count += 1
	return count

def main():
	start_amplitude = float(input("Введите начальную амплитуду: "))
	stop_amplitude = float(input("Введите амплитуду остановки: "))
	if start_amplitude <= 0 or stop_amplitude <= 0:
		print("Амплитуды должны быть положительными числами.")
	elif stop_amplitude >= start_amplitude:
		print("Амплитуда остановки должна быть меньше начальной.")
	else:
		print("Маятник считается остановившимся через", fluctuations(start_amplitude, stop_amplitude), "колебаний.")

main()