class BankAccount:
    def __init__(self,balance = 0,int_rate = 0.01):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        current_balance = self.balance
        new_balance= current_balance + amount
        self.balance = new_balance
    def withdraw(self, amount2):
        current_balance2 = self.balance
        new_balance2 = current_balance2 - amount2
        self.balance = new_balance2
    def display_account_info(self):
        print("your balance is", self.balance)
        print("your interest rate is",self.int_rate)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate 



class User:
    def __init__(self,name,last_name,age,):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.savings = BankAccount(balance=0,int_rate=0.02)
    def user_info(self):
        print("name",self.name)
        print("last name",self.last_name)
        print("age",self.age)
        self.savings.display_account_info()
    def user_deposit(self,amount):
        self.savings.deposit(amount)
    def user_withdraw(self,amount):
        self.savings.withdraw(amount)
    def user_yield_interest(self,):
        self.savings.yield_interest()



user = User("Lenddy","Morales",18)
user.user_info()
user.user_deposit(10.0)
user.user_info()
user.user_withdraw(1.00)
user.user_info()
user.user_yield_interest()
user.user_info()

