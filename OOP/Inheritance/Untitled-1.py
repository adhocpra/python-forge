
class Degree:
    def level(self):
        print("You graduated")

class Phd(Degree):
    def graduate(self):
        print("You are a Phd Graduate")
c1=Degree
c1.level()