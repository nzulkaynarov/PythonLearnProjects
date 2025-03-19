print("Добро пожаловать в игру «Угадай число»!")
print("Настя загадывает число. Дима, не подглядывай!")
nastya_number = int(input("Введите число: "))
dima_number = int(input("Введите число: "))

if nastya_number == dima_number:
    print("Ура! Угадал!")
else:
    print("Нет, это не то, что я загадала.")