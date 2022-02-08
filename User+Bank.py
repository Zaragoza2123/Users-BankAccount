class BankAccount:
    all_accounts = []
    def __init__(self, int_rate=.01, balance = 0): 
        self.balance = balance
        self.int_rate= int_rate
        if balance > 0:
            self.balance = balance 
        BankAccount.all_accounts.append(self)
    @classmethod
    def all_instantces(cls):
        for account in cls.all_accounts:
            account.display_account_info()
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}, Interste Rate: {self.int_rate}" )
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate) 
        return self

class User:
    def __init__(self , name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount()
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_with_drawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self
    def interest(self):
        self.account.yield_interest()
        return self


user1 = User("John", "johnjohn@gmail.com")
user2 = User("Stitch", "stitch@gmail.com")

user1.make_deposit(100).make_deposit(100).make_deposit(100).make_with_drawal(300).interest().display_user_balance()
user2.make_deposit(1000).make_deposit(1000).make_with_drawal(500).make_with_drawal(500).make_with_drawal(300).make_with_drawal(300).interest().display_user_balance()
print("~~~~~~~~~~~~")
BankAccount.all_instantces()

