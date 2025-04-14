def count_letters(message, number, word):
	count_numbers = 0
	count_words = 0
	for letter in message:
		if letter == str(number):
			count_numbers += 1
		elif letter == word:
			count_words += 1
	print('Количество цифр', number, ':', count_numbers)
	print('Количество букв', word, ':', count_words)

message = input('Введите текст: ')
number = int(input('Какую цифру ищем? '))
word = input('Какую букву ищем? ')
count_letters(message, number, word)