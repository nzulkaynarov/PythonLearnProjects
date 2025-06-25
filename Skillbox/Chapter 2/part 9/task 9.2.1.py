import os

your_path = input('Путь: ')
if os.path.isfile(your_path):
    print('Это файл')
    print('Размер файла: ', os.path.getsize(your_path), 'байт')
elif os.path.isdir(your_path):
    print('Это папка')
else:
    print('Указанного пути не существует')
