#1
from abc import ABC, abstractmethod

class Manager(ABC):
    def critical_data(self):
        print("Acess critical data")
    
    def modify_rules(self):
        print("Can modify company rules")
    
    @abstractmethod
    def security(self):
        pass

class Developer(Manager):
    def security(self):
        print("Developer has secured ")
        
d1=Developer()
d1.critical_data()

class Analyst(Manager):
    def security(self):
        print("Analyst has secured.")
a1=Analyst()
a1.modify_rules()

#2
class WebApp(ABC):
    def show_files(self):
        print("I can show files")
    def show_photos(self):
        print("I can show photos")
    @abstractmethod
    def responsive(self):
        pass
    
class Desktop(WebApp):
    def responsive(self):
        print("fit for desktop.")
class Mobile(WebApp):
    def responsive(self):
        print("fit for mobile")
d1=Desktop()
p1=Mobile()

d1.show_files()
p1.show_photos()
