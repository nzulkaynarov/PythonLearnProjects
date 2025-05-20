friend_name = input('Введите имя: ')
credit_value = int(input('Введите долг: '))

print('{name}!, {name}, привет! Как дела, {name}? Где мои {cash} рублей? {name}!'.format(name = friend_name, cash = credit_value))