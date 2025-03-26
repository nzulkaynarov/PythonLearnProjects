students = int(input('Сколько в классе учеников? '))
a_students = 0
b_students = 0
c_students = 0

for i in range(students):
		student_grade = int(input('Введите оценку ученика: '))
		if student_grade == 5:
				a_students += 1
		elif student_grade == 4:
				b_students += 1
		elif student_grade == 3:
				c_students += 1

if a_students > b_students and a_students > c_students:
		print('Сегодня больше отличников!')
elif b_students > a_students and b_students > c_students:
		print('Сегодня больше хорошистов!')
elif c_students > a_students and c_students > b_students:
		print('Сегодня больше троечников!')
