class Bank:
    def __init__(self,name,number):
        self.__name=name ### Private anf Protected Variables 
        self.__number=number

    #def show_info(self):
        print(f" {self.__name},{self.__number}")

b1=Bank("Saving",00)
b1.__name="Current"
#b1.show_info()

# #Bad practices 

print(b1.__name) 
# print(b1._number)