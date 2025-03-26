debtors = int(input("Введите количество должников: "))
debtors_summ = 0
for client in range(0, debtors, 5):
		print("Должник с номером ", client)
		client_summ = int(input("Сколько должны? "))
		debtors_summ += client_summ
print()
print("Общая сумма долга: ", debtors_summ)