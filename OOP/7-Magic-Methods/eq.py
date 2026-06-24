class Student:
    def __init__(self,name):
        self.name=name

    def __eq__(self, value):
        return self.name == value.name
s1= Student("Ram")
s2=Student("Ram")

print(s1)
print(s1)
print(s1==s2)

class Student:
    def __init__(self,name):
        self.name=name

    def __eq__(self, value):
        return self.name == value.name
s1= Student("Ram")
s2=Student("Ram")

print(s1)
print(s1)
print(s1==s2)

