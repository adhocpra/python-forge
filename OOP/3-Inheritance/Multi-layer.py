
class CEO:
    def info1 (self):
        print("This is CEO")

class Branch_Manager(CEO):
    def info2 (self):
        print("This is BM")

class Desk_staff (Branch_Manager):
    def info3 (self):
        print("I am a staffer")

d1=Desk_staff()
d1.info1()
d1.info2()
d1.info3()