class Car:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return self.model


class Truck(Car):

    def __init__(self, trunk_fullness=0, model="грузовой автомобиль"):
        super().__init__(model)
        self.trunk_fullness = trunk_fullness

    def loading(self):
        self.trunk_fullness = 100
        print(f"{self} загружен")

    def unloading(self):
        self.trunk_fullness = 0
        print(f"{self} разгружен")


class PassengerCar(Car):

    def __init__(self, gps_system, model="легковой автомобиль"):
        super().__init__(model)
        self.gps_system = gps_system

    def gps_enable(self):
        print(f"{self}, включена навигация {self.gps_system}")


truck = Truck()
truck.loading()
truck.unloading()

passenger_car = PassengerCar("ГЛОНАСС")
passenger_car.gps_enable()