input_name = input('Имя: ')
order_number = int(input('Номер заказа: '))
hello_text = 'Здравствуйте, {name}! Ваш номер заказа: {order}. Приятного дня!'


print(hello_text.format(name = input_name, order = order_number))