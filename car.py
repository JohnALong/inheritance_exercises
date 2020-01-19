from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, manufacturer, model):
        self.doors = ""
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_type = ""
        self.battery_capacity = 0
        self.fuel_capacity = 0

    def drive(self):
        print(f"The {self.main_color} {self.manufacturer} {self.model} goes: mmmmmmmmmmmm")

    def drive_electric(self):
        print(f"????  Where's the sound when the {self.manufacturer} {self.model} is running on electric????")