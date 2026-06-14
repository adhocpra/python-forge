class Product:
    def __init__(self,name,price):
        self.name=name
        self.price= price
    
    def __lt__(self,other):
        return s1.price<s2.price

s1= Product("Laptop", 1200)
s2=Product("Mobile",900)
print(s1<s2)