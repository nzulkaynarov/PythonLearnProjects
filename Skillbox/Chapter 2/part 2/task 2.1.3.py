count_workers = int(input('Кол-во сотрудников в офисе: '))
list_workers = []

for _ in range(count_workers):
    id_worker = int(input('ID сотрудника: '))
    list_workers.append(id_worker)

search_id = int(input("Какого сотрудника ищем? "))
search = False
for id in list_workers:
    if id == search_id:
        search = True
if search:
    print("Сотрудник работает!")
else:
    print("Сотрудник не работает!")