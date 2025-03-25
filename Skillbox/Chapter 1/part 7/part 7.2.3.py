winners = 0

for ticket in 345, 19, 87, 1020, 421:
	if ticket // 100 > 0 and ticket % 5 == 0:
		print(ticket, "- выигрышный билет")
		winners += 1
print("Число победителей: ",  winners)