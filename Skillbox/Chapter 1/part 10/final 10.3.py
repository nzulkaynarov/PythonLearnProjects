size_width = 20
size_height = 15

for row in range(size_height):
    for col in range(size_width):
        if col == 0 or col == size_width - 1:
            print('|', end=" ")
        elif row == 0 or row == size_height - 1:
            print('-', end=" ")
        else:
            print(' ', end=" ")
    print()