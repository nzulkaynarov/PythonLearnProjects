for row in range(6):
	for col in range(11):
		if col % 2 == 0:
			print(row + col, end = "\t")
	print()