class Vehicle:
    def __init(self):
        self.main_color = ""
        self.maximum_occupancy = ""
        self.turn = ""

    def drive(self):
        print("Vroooom!")

    def turn(self, direction):
        print(f"To get gas, the {self.main_color} {self.manufacturer} {self.model} turns {direction} and goes two blocks.")

    def stop(self):
        print(f"Hit the brakes if you want the {self.manufacturer} {self.model} to stop.")