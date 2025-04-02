size = int(input("Введите размер матрицы: "))
for row in range(1, size + 1):
		for col in range(1, size + 1):
				if row % 2 != 0:
						print(col, end = " ")
				else:
						print(row, end = " ")
		print()