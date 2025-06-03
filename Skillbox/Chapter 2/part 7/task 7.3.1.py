your_text = input('Строка: ')
print('Ответ: ', end = '')
for index, value in enumerate(your_text):
    if value == '~':
        print(index, end = ' ')
