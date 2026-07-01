class BankAccount:
    def __init__(self, balance):
        self.__balance= balance
    def deposit(self,amount):
        self.__balance +=amount

    def withdraw(self,amount):
        if self.__balance<amount:
            print("Insufficient fund")
        else:
            self.__balance -=amount
    def show_balance(self):
        print(f" Your new balance is {self.__balance}")
acc= BankAccount(1000)
acc.show_balance()

acc.withdraw(10000)
acc.deposit(10000)
acc.show_balance()
acc.deposit(5000)
acc.withdraw(100000)