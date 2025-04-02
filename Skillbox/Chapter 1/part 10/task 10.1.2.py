number = int(input("Введите число: "))

for row in range(0, number + 1):
		for col in range(0, number + 1):
				print(row + col, end=" ")
		print()