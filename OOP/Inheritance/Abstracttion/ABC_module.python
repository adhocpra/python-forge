#Abstract Base Class
from abc import ABC, abstractmethod

class Animal(ABC):# class has to be child of ABC class 
    @abstractmethod #decorator
    def sound(self): #incomplete-- this is abstract method
        pass
    @abstractmethod
    def info(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
    def info(self):
        print("This is a dog")
d1=Dog()
d1.sound()
d1.info()
