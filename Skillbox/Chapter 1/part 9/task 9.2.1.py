total_students = int(input('Введите кол-во учащихся: '))
answer = 'Пушкин'
bad_answer = 0

for student in range (total_students):
	student_answer = input('Введите ответ: ')
	if student_answer != answer:
		print('Ответ неверный')
		bad_answer += 1
	else:
		print('Ответ верный')
		break
print('Количество неверных ответов: ', bad_answer, 'из', total_students)
		
	

