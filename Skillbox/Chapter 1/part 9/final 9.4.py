word_length = 0  
current_word = 0  

text = input('Введите текст: ')

for word in text:
    if word != ' ':
        current_word += 1
    else:
        if current_word > word_length:
            word_length = current_word
        current_word = 0

if current_word > word_length:
    word_length = current_word

print('Самое длинное слово', word_length, 'букв')