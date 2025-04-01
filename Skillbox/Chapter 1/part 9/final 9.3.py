room_length = 15  
room_width = 20   
robot_x = 8       
robot_y = 10      

while True:
    print('[Программа]: Марсоход находится на позиции', robot_x, ',',robot_y, ',', 'введите команду: ')
    move = input('[Оператор]: ')
    if move == 'D':
        if robot_x < room_length:
            robot_x += 1
    elif move == 'A':
        if robot_x > 1:
            robot_x -= 1
    elif move == 'W':
        if robot_y < room_width:
            robot_y += 1
    elif move == 'S':
        if robot_y > 1:
            robot_y -= 1
    else:
        continue