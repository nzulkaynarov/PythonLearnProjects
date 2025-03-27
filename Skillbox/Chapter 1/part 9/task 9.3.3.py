text = input('Введите текст: ')
bigt_word = 0
small_word = 0

for word in text:
		if word == 'Ы':
				bigt_word += 1
		elif word == 'ы':
				small_word += 1
print('Больших букв Ы: ', bigt_word)
print('Маленьких букв Ы: ', small_word)