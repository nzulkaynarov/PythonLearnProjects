# Вводим координаты коня и точки на шахматной доске.
x_horse = float(input('Координата икс коня: '))
y_horse = float(input('Координата игрек коня: '))


x_point = float(input('Координата икс точки: '))
y_point = float(input('Координата игрек точки: '))


# Преобразуем введённые координаты к целому типу после умножения на 10 для точности.
x_horse = int(x_horse * 10)
y_horse = int(y_horse * 10)
x_point = int(x_point * 10)
y_point = int(y_point * 10)


# Вычисляем разницу по координатам, игнорируя направление (получаем положительные значения).
diff_x = abs(x_horse - x_point)
diff_y = abs(y_horse - y_point)


# Проверяем, может ли конь ходить, используя произведение разницы координат. 
# Для допустимого хода одно из значений должно быть 1, а другое — 2, их произведение всегда равно 2.
if diff_x * diff_y == 2:
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь не может ходить в эту точку.')