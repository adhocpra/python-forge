class student:
    def __init__(self,name,age, location):
        self.name=name
        self.age= age
        self.location= location

    def __repr__(self):
        return f"student ('{self.name}', {self.age},'{self.location}')"

s1= student("smriti",25,"tonkawa")
print(s1)

# is __str__ is also in there it will print str if nothing is done

#2
class Car:
    def __init__(self,name,color, price):
        self.name=name
        self.color=color
        self.price = price
    def __str__(self):
        return "This object is about car"
    # this method is for developer
    def __repr__(self):
        return f" Car( '{self.name}', '{self.color}', {self.price})"


c1= Car("Hyundai", "Grey","8000")
print(c1)
# to print repr we do : or it prints str
print(repr(c1))