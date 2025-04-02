ancient_text = input("Что написано в свитке? ")
reverse_text = ''


for symbol in ancient_text:
    reverse_text = symbol + reverse_text


if ancient_text == reverse_text:
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром!")
    

result = 163 % 100
print(result)