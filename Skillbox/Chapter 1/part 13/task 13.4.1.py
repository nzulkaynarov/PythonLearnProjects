import math

def check_exponent_change(tax, new_tax):
    total = tax + new_tax
    degree_e_tax = math.floor(math.log10(tax))
    degree_e_total = math.floor(math.log10(total))
    if degree_e_tax != degree_e_total:
        return True
    else:
        return False
 
country_budget = float(input('Введите бюджет страны: '))
budget_receipts = float(input('Введите новые поступления (налог): '))
is_increase = check_exponent_change(country_budget, budget_receipts)

if is_increase:
    print('Бюджет увеличится')
else:
    print('Бюджет не изменится')

def eqv(a, b, c):
    return abs((a + b) - c) <= 1e-15


first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
third = float(input("Введите третье число: "))
print(eqv(first, second, third))