class Vehicle:
    def start(self):
        print("Vehicle start")


class Car(Vehicle):
    def start(self):
        super().start()
        print("Car start")


class ElectricCar(Vehicle):
    def start(self):
        super().start()
