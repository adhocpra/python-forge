#Polymorphism has same method different behavior
#Eg:1
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat Meows")
d1=Dog()
c1=Cat()
d1.sound()
c1.sound()
#this is a repetative task, which can be made easier by using function.
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat Meows")
d1=Dog()
c1=Cat()

def make_sound(animal): #this is the polym. functiom
    animal.sound()
#use different objects in the same function
make_sound(d1)
make_sound(c1)

#Eg:2

class Push_On:
    def start(self):
        print("Vehicle is started using Push Bottom")

class Insert_Key:
    def start(self):
        print("Vehicle is started using Key")

t1=Push_On()
k1=Insert_Key()

def Start_Option(Go):
    Go.start()
Start_Option(t1)
Start_Option(k1)