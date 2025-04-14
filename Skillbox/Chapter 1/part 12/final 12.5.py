def rock_paper_scissors():
	print("\nДобро пожаловать в игру 'Камень, ножницы, бумага'!")
	computer_choice = 'камень'
	while True:
		user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ")
		if user_choice == computer_choice:
			print("Ничья!")
		elif (user_choice == 'камень' and computer_choice == 'ножницы') or (user_choice == 'ножницы' and computer_choice == 'бумага') or (user_choice == 'бумага' and computer_choice == 'камень'):
			print("Вы выиграли!")
		else:
			print("Вы проиграли!")
		break

def guess_the_number():
	print("\nДобро пожаловать в игру 'Угадай число'!")
	computer_guess = 89
	while True:
		user_guess = int(input('Введите ваше число: '))
		if user_guess < computer_guess:
			print('Ваше число меньше загаданного.')
		elif user_guess > computer_guess:
			print('Ваше число больше загаданного.')
		else:
			print('Поздравляю! Вы угадали число!')
			break

def main_menu():
	while True:
		print("\nГлавное меню:")
		print("1. Камень, ножницы, бумага")
		print("2. Угадай число")
		print("3. Выход")
		choice = input("Выберите игру (1, 2) или 3 для выхода: ")
		if choice == '1':
			rock_paper_scissors()
		elif choice == '2':
			guess_the_number()
		elif choice == '3':
			print("Спасибо за игру! До свидания!")
			break
		else:
			print("Некорректный выбор. Попробуйте снова.")

main_menu()