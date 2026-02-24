class Toyota:
    car_color = 'red'
    car_price = 1000000
    max_speed = 200
    current_speed = 0

    def info_car(self):
        print(
            'Цвет машины: {}\nТекущая стоимость: {}\nМаксимальная скорость: {}\nТекущая скорость: {}'.format(
                self.car_color, self.car_price, self.max_speed, self.current_speed
            )
        )

    def change_speed(self, new_speed):
        self.current_speed = new_speed

car = Toyota()
car.change_speed(100)
car.info_car()
print(Toyota.current_speed)