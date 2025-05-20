def caesar_cipher(text, shift):
		char_list = [(rus_alphabet[(rus_alphabet.index(char) + shift) % len(rus_alphabet)]
								if char != ' ' else ' ') for char in text]
		result = ''.join(char_list)
		return result

rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
input_text = input('Введите сообщение: ').lower()
shift_word = int(input('Введите сдвиг: '))

output_text = caesar_cipher(input_text, shift_word)

print('Зашифрованное сообщение:', output_text)