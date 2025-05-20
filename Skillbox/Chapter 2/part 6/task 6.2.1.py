small_storage = {

    'гвозди': 5000,

    'шурупы': 3040,

    'саморезы': 2000

}

big_storage = {

    'доски': 1000,

    'балки': 150,

    'рейки': 600

}

big_storage.update(small_storage)

item_search = input('Поиск товара: ').lower()

quantity = big_storage.get(item_search)

if quantity is not None:
    print(f'Результат поиска "{item_search}". Наличие на складе {quantity} шт.')
else:
    print('Товар не найден')
