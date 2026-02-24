import random

class Toyota:
    car_color = 'red'
    car_price = 1000000
    max_speed = 200
    current_speed = 0

car_speed_1 = Toyota()
car_speed_2 = Toyota()
car_speed_3 = Toyota()

car_speed_1.current_speed = random.randint(0, 200)
car_speed_2.current_speed = random.randint(0, 200)
car_speed_3.current_speed = random.randint(0, 200)

print(car_speed_1.current_speed, car_speed_2.current_speed, car_speed_3.current_speed)