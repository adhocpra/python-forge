class Animal:
    def __init__(self):
      print("I am animal")

c1=Animal() #calls itself after object creation

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("dog created")
d1= Dog()

#with parameters
class CEO():
    def __init__(self,salary,bonus):
        self.__salary= salary
        self.__bonus = bonus
    def hq_info(self):
        print(f"CEO's salary: {self.__salary},bonus: {self.__bonus}")
 
class Manager(CEO) :  
    def __init__(self,salary, bonus,language):
        super().__init__(salary,bonus)
        self.__language= language

    def show_info(self):
        print(f"BM's salary: {self._CEO__salary},bonus: {self._CEO__bonus}, language: {self.__language}")

c1= Manager(12000,200, "java")
c1.show_info()



