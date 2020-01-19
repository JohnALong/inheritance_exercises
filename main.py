from motorcycle import Motorcycle
from plane import Plane
from train import Train
from truck import Truck
from car import Car

#truck
f150 = Truck("Ford", "F-150")
f150.doors = "4 door crew cab"
f150.fuel_capacity = "36 gallons"
f150.wheel_drive = "4"
f150.maximum_occupancy = "5"
f150.main_color = "grey"

#plane
warthog = Plane("jet")
warthog.purpose = "attack"
warthog.fuel_capacity = "1642 gallons"
warthog.maximum_occupancy = "1"
warthog.main_color = "Navy Blue"

#train
pullman = Train("passenger")
pullman.fuel_type = "coal"
pullman.main_color = "Silver"
pullman.purpose = "luxury commercial"
pullman.maximum_occupancy = "890"

#car
fusion = Car("Ford", "Fusion")
fusion.doors = "4"
fusion.fuel_type = "hybrid"
fusion.battery_capacity = "13 kwh"
fusion.fuel_capacity = "12 gallons"
fusion.main_color = "white"
fusion.maximum_occupancy = "5"

#motorcycle
harley = Motorcycle("Harley-Davidson", "Panhead")
harley.maximum_occupancy = "2"
harley.main_color = "black"
harley.fuel_capacity = "7 gallons"

#actions of vehicles
f150.drive()
f150.turn("left")
f150.stop()

fusion.drive()
fusion.turn("right")
fusion.stop()
fusion.drive_electric()

pullman.drive()
pullman.turn("left")
pullman.stop()


harley.drive()
harley.turn("left")
harley.stop()

warthog.drive()
warthog.turn("right")
warthog.stop()



