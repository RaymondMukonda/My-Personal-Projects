class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


    def moves(self):
        print("Moving along..")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicle("bmw", "m 340i")

print("")
# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()
print("")

##################################################

your_car = Vehicle("audi", "rs 7")
your_car.get_make_model()
your_car.moves()
print("")

############# inheritence #########################


class Airplane(Vehicle):
    def moves(self):
        print("Flies along..")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along..")

class GolCart(Vehicle):
    pass


cessna = Airplane("Cessna", "Skyline")
mack = Truck("Mack", "Pinnacle")
Golwagon = GolCart("Yamaha", "gc 100")

cessna.get_make_model()
cessna.moves()
print("")
mack.get_make_model()
mack.moves()
print("")
Golwagon.get_make_model()
Golwagon.moves()