educational_grant = int(input("Введите ежемесячную стипендию: "))
expenses = int(input("Введите ежемесячные расходы: "))

total_needed = 0
current_expenses = expenses

for month in range(1, 11):
    if month == 1:
        month_expenses = current_expenses
    else:
        month_expenses = int(current_expenses * 1.03) 
        current_expenses = month_expenses
    
    shortage = month_expenses - educational_grant
    if shortage > 0:
        total_needed += shortage
    
    print(month, "-й месяц: траты ", month_expenses, "рублей, не хватает ", shortage, " рублей.")

print("Сумма денег, которую необходимо получить у родителей: ", total_needed, " рублей.")