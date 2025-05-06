first_line = input("Введите первую строку: ")
second_line = input("Введите вторую строку: ")
count_first = first_line.count("!") + first_line.count("?")
count_second = second_line.count("!") + second_line.count("?")
if count_first > count_second:
    print(first_line + second_line)
elif count_second > count_first:
    print(second_line + first_line)
else:
    print("Ой")