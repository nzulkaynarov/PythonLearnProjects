def summa_n(item):
	items_sum = item * (item + 1) / 2
	print('Сумма чисел от 1 до', item, 'равна', int(items_sum))
	
item = int(input("Введите число: "))
summa_n(item)