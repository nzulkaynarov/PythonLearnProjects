number_of_workers = int(input("Кол-во сотрудников: "))
wages_of_workers = []
for i in range(number_of_workers):
    wage = int(input(f"Зарплата {i + 1} сотрудника: "))
    if wage > 0:
        wages_of_workers.append(wage)

print("Осталось сотрудников:", len(wages_of_workers))
print("Зарплаты:", wages_of_workers)
print("Максимальная зп:", max(wages_of_workers))
print("Минимальная зп:", min(wages_of_workers))