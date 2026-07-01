#Special method that shows how an object should be displayed when printing
class Car:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        return f" Car name is {self.name }"
    def __str__(self) : # str gives custom info instead of object location 
        return f" Car name is {self.name}"  
c1=Car("Maruti")
print(c1) #printing only object -- using str prints the message 
print(c1.show_info())

#2 
class Student:
    def __init__(self,name, age, location):
        self.name= name
        self.age=age
        self.location=location
    # for the use of user
    def __str__(self):
        return f" Name is {self.name } , age is {self.age} and location is {self.location}"
s1= ("Devindra",25, "tonkawa")
print(s1)

