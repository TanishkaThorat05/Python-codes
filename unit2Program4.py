# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")


# Subclass Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road")


# Subclass Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# Create objects
c = Car()
b = Bicycle()

# Demonstrate polymorphism
c.move()
b.move()