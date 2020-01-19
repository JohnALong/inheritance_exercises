from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_capacity = 0

    def drive(self):
        print(f"The {self.main_color} {self.manufacturer} {self.model} goes: Rumble Rumble Rumble")

    def turn(self, direction):
        print(f"To get gas, the {self.main_color} {self.manufacturer} turns {direction} and then {direction} again.")

    def stop(self):
        print(f"Pull the lever on the right handlebar of the  {self.manufacturer} to stop.")