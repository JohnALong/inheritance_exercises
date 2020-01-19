from vehicle import Vehicle

class Train(Vehicle):
    def __init__(self, style):
        self.style = style
        self.fuel_type = ""
        self.purpose = ""

    def drive(self):
        print(f"The {self.main_color} {self.style} train goes: Chugga Chugga Chugga")

    def turn(self, direction):
        print(f"You're on a freakin' {self.main_color} {self.style} {self.purpose}!  There are no {direction} turns!")

    def stop(self):
        print(f"Pull the cord to stop the {self.main_color} {self.style} {self.purpose}.")