phone_book = {}

while True:
    first_name = input('Введите имя: ')
    second_name = input('Введите фамилию: ')
    person_key = first_name, second_name
    if person_key not in phone_book:
        phone_book[person_key] = int(input('Введите номер телефона: '))
    else:
        print('Контакт {name} уже имеется в контактах'.format(name=person_key))
    print(phone_book)