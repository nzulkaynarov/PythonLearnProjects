import math

def cilinder_square(r, h):
    side = 2 * math.pi * r * h
    full = side + 2 * math.pi * r ** 2
    return side, full

radius_str, height_str = input('Введите радиус и высоту через запятую: ').split(',')
radius = float(radius_str)
height = float(height_str)

side, full = cilinder_square(radius, height)

print('Площадь боковой поверхности: ', round(side, 2))
print('Полная площадь: ', round(full, 2))