from vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, type):
        self.type = type
        self.purpose = ""
        self.fuel_capacity = 0

    def drive(self):
        print(f" The {self.main_color} {self.type} goes: WWWWHHHHOOOOOSSSSSSHHHHHH")

    def turn(self, direction):
        print(f"The {self.main_color} {self.type} banks {direction} and flies on towards morning.")

    def stop(self):
        print(f"Lower the flaps on the {self.main_color} {self.purpose} {self.type} and put the wheels down to land.")