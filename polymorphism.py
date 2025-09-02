# Parent class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Child class: Car
class Car(Vehicle):
    def move(self):
        print("driving on the road.")


# Child class: Plane
class Plane(Vehicle):
    def move(self):
        print("flying in the sky.")


# Child class: Boat
class Boat(Vehicle):
    def move(self):
        print("sailing on the water.")


# Child class: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("pedaling along the path.")


# --- Example Usage ---
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()