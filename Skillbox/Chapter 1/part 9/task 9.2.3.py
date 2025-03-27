user_name = input('Как тебя зовут? ')
print(user_name,', купи слона! ')
user_answer = 0
while user_answer != 'Слон':
	user_answer = input()
	print('Все говорят, ', user_answer, ', а ты купи слона!')
