# to print the length of the object
class Car:
    def __init__(self,name):
        self.name =name 

    def __len__(self):
        return len(self.name)
c1= Car (" Hyundai ")
print(len(c1))

#2;

class Team:
    def __init__(self, members,leaders, captains):
        self.members= members
        self.leaders= leaders
        self.captains= captains
     
    def __len__(self):
        return len(self.members)
    
t1= Team(["Ram" ,"Shyam", "Krishna", "hari"], ["Ram", "Hari"], ["Krishna", "Vishnnu", "Shyam"])
print(len(t1))