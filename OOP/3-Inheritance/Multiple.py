class Education:
    def info(self):
        print("Education gives knowledge")

class Sports:
    def info_1(self):
        print("Sports give you name")

class Money(Education,Sports): #order matters
    def info_2(self):
        print("Both together and you rich")

c1=Money()
c1.info()
c1.info_1()
c1.info_2()

#Method REsolution Order

class Education:
    def info(self):
        print("Education gives knowledge")

class Sports:
    def info (self):
        print("Sports give you name")

class Money(Education,Sports): #order matters
    def info1 (self):
        print("Both together and you rich")

c1=Money()
c1.info1()
c1.info()


#Method Overriding and Super

class Python:
    def skill(self):
        print(" I code in Python")

class Java(Python):
    def skill(self):
        super().skill()
        print(" I code in Java")
        super().skill()
c1=Java() #This runs
c1.skill()



