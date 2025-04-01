true_answer = 0

for answer in range(10):
	key_word = input('Введите ключевое слово: ')
	if key_word == 'Карамба' or key_word == 'карамба':
		true_answer += 1
print('На борт попадут:', true_answer, 'человек')