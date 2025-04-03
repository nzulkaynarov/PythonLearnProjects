highest = int(input('Введите высоту пирамиды: '))

for row in range(1, highest + 1):
    print('\' * (highest - row), end='')
    print('#' * (2 * row - 1))