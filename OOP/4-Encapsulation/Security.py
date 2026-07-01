class Security:
    def __init__ (self,username,password,pin):
        self.__username= username
        self.__password= password
        self.__pin = pin
        print(f" your current data is saved.")
    
    def change_username(self,new_username):
        self.__username = new_username
    def change_password(self,new_password):
        self.__password = new_password
    def change_pin(self,new_pin):
        self.__pin = new_pin
    def show_change(self):
        print(f"The change is Username: {self.__username} ") 
        print(f"Password:{self.__password} ")
        print(f"PIN: {self.__pin}")

change1= Security("adhoc",333,888)    
change1.change_username("root")  
change1.change_password (3334)
change1.change_pin (221)
change1.show_change()

        