def print_all_info(surname, name, country, city, street, house, flat):
	print("Фамилия:", surname)
	print("Имя:", name)
	print("Страна проживания:", country)
	print("Город:", city)
	print("Улица:", street)
	print("Номер дома:", house)
	print("Номер квартиры:", flat)

user_surname = input("Введите фамилию: ")
user_name = input("Введите имя: ")
user_street = input("Введите улицу: ")
user_house = input("Введите номер дома: ")

for _ in range(3):
    user_surname = input("Введите фамилию: ")
    user_name = input("Введите имя: ")
    user_country = input("Введите страну проживания: ")
    user_city = input("Введите город: ")
    user_street = input("Введите улицу: ")
    user_house = input("Введите номер дома: ")
    user_flat = input("Введите номер квартиры: ")

    print_all_info(user_surname, user_name, user_country, user_city, user_street, user_house, user_flat)

