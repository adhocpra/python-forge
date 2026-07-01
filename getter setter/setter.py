class Student:
    def __init__(self,name):
        self.__name =name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name= new_name 
    
s1= Student("Ram")
print(s1.name)

s1.name = "Shyam"
print(s1.name)