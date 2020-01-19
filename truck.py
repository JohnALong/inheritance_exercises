from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, manufacturer, model):
        self.doors = ""
        self.manufacturer = manufacturer
        self.model = model
        self.wheel_drive = ""
        self.fuel_capacity = 0

    def drive(self):
        print(f"The {self.main_color} {self.manufacturer} {self.model} goes: clop clop clop")
