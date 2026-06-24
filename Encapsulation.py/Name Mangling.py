# Python storing private variables
class Student:
    def __init__(self,name):
        self.__name=name
    def show_info(self): #Always print private variable from inside
        print(f" Your name is {self.__name}")
    
s1=Student("Bidhan")
#print(s1.__name) # cannot access this 
s1.show_info()
print(s1._Student__name) #object._class__variable (outside)-- Bad practice