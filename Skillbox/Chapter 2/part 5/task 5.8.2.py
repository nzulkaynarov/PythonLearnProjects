def text_coding(text):
    count = 0
    result = ""
    for index, symbol in enumerate(text):
        count += 1
        # Если следующий символ другой или это последний символ
        if index == len(text) - 1 or symbol != text[index + 1]:
            result += f'{symbol}{count}'
            count = 0  # Сброс счетчика для новой группы символов
    return result

user_text = input('Введите строку: ')
print('Закодированная строка:', text_coding(user_text))
