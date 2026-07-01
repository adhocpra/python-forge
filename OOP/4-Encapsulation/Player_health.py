class Player:
    def __init__(self,name,health):
        self.__name = name
        self.__health = health
    
    def take_damage(self,damage):
        self.__health -= damage
        if self.__health<damage:
            self.__health=0
    
    def heal(self,heal):
        self.__health += heal
        if self.__health >100:
            self.__health=100
    
    def is_alive(self):
        if self.__health>0:
          return "alive"
        else:
            return "dead"
    
    def show_health(self):
        print(f" {self.__name}, is at {self.__health}")

p1=Player("Avi",20)
p1.take_damage(30)
p1.heal(200)

p1.show_health()
print(p1.is_alive())

