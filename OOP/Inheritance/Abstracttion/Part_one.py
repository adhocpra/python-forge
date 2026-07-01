#abstraction --
class Phone:
    def call(self):
        self.__connect_network()
        print("Calling....")

    def __connect_network(self):
        print("Connecting network")
p1=Phone()
p1.call()

class Copy:
    def write(self):
        self .__cursive_writing()
        print("Writing...")
    
    def __cursive_writing():
        print("writing in cursive")

w1= Copy()
w1.write()


class Bank:
    def __init__(self,balance):
        self.__balance= balance

    def deposit (self,amount):
        self.__balance += amount
    def withdraw (self,amount):
        self.__balance -= amount
    def show_balance(self):
        print(f"Your balance is {self.__balance}")
b1= Bank(4000)
b1.deposit(1000)
b1.withdraw(2000)
b1.show_balance()