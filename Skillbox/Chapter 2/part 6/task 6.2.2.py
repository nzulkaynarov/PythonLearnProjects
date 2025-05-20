incomes = {

    'apple': 5600.20,

    'orange': 3500.45,

    'banana': 5000.00,

    'bergamot': 3700.56,

    'durian': 5987.23,

    'grapefruit': 300.40,

    'peach': 10000.50,

    'pear': 1020.00,

    'persimmon': 310.00,

}

total_income = 0

for price in incomes.values():
    total_income += price

min_price = min(incomes.values())
min_key = min(incomes, key = incomes.get)

incomes.pop(min_key)

print(f'Общий доход за год составил {total_income} рублей')
print(f'Самый маленький доход у {min_key}. Он составляет {min_price} рублей')
print('Итоговый словарь:', incomes)
