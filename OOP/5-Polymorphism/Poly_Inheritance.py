class Vehicle:
    def info(self):
        print("I do transportation")
    
class Car(Vehicle):
    def info(self):
        print("I transport people")

class Truck(Vehicle):
    def info(self):
        print("I transport goods")
#objects
v1=Vehicle()
c1=Car()
t1=Truck()

# #without poly method
# v1.info()
# c1.info()
# t1.info()

def show_info(object):
    object.info()

show_info(v1)
show_info(c1)
show_info(t1)

print ()

print ()
#2.
#short-cut with list and loop
class Vehicle:
    def info(self):
        print("I do transportation")
    
class Car(Vehicle):
    def info(self):
        print("I transport people")

class Truck(Vehicle):
    def info(self):
        print("I transport goods")
#objects
vehicles= [Vehicle(),Car(), Truck()]

def show_info(object):
    object.info()

# show_info(vehicles[0])
# show_info(vehicles[1])
# show_info(vehicles[2])

for Vehicle in vehicles:
    show_info(Vehicle)