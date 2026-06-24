class Student:
    def __init__(self,name):
        self.__name= name

    @property
    def name(self):
        return self.__name

s1= Student("Ram")
print(s1.name)

class Bank:
    def __init__(self,balance):
        self.__balance= balance

    @property
    def balance(self):
        return self.__balance

b1= Bank(4500)
print(b1.balance)

# #getter from old method (show)
#     def show_name(self):
#         return self.__name
#     #setter- change
#     def change_name(self,new_name):
#         self.__name = new_name
    
# s1= Student("Ram")
# print(s1.show_name())
# s1.change_name("shyam")
# print(s1.show_name())

#setter

