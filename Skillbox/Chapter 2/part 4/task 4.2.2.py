text = input('Введите строку:')
symbol = input('Введите дополнительный символ:')

double_text = [x * 2 for x in text]
double_text_sym = [x + symbol for x in double_text]

print(double_text)
print(double_text_sym)