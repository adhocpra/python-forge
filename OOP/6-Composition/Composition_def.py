#Definition-- Building a class using other class
# 'Has' relationship 

class Engine:
    def start(self):
        print("Engine started")
    
class Car:
    def __init__(self):
       self.engine= Engine() #object created
    
    def start(self):
        self.engine.start()
        print("car is running")
    
c1=Car()
c1.start()

