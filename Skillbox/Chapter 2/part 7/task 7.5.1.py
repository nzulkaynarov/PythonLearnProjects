data = {

    (5000, 123456): ('Иванов', 'Василий'),

    (6000, 111111): ('Иванов', 'Петр'),

    (7000, 222222): ('Медведев', 'Алексей'),

    (8000, 333333): ('Алексеев', 'Георгий'),

    (9000, 444444): ('Георгиева', 'Мария')

}

number = int(input("Введите номер паспорта: "))
series = int(input("Введите серию паспорта: "))

number_and_series = (number, series)

if number_and_series in data:
    for index, person_name in enumerate(data[number_and_series]):
        print(person_name, end=' ')
else:
    print("Такого человека нет")
