class Toyota:
    def __init__(self, color='red', price=1e6, max_speed=200, current_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def check_info(self):
        print(self.color, self.price, self.max_speed, self.current_speed)

    def change_speed(self, new_speed):
        self.current_speed = new_speed


car = Toyota()
car.check_info()
car.change_speed(100)
car.check_info()
car_2 = Toyota('green', 500000, 150)
car_2.change_speed(50)
car_2.check_info()