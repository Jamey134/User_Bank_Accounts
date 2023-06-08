class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        return self
        # same as line 9
        # self.balance=self.balance+amount
    def withdraw(self, amount):
        
        if amount < self.balance:
            self.balance-=amount

        else:
            self.balance-=5.00
            print("Insufficient funds: Charging a $5 fee")
        return self
        # same as line 16
        # self.balance=self.balance-amount
    def display_account_info(self):
        print(f'Balance {self.balance}')
    def yield_interest(self):
        interest = self.balance*self.int_rate
        self.balance+=interest
        return self



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self

bank_account=BankAccount(0.01, 100)
bank_account2=BankAccount(0.03, 20)
bank_account3=User('Hancho', 'hanchoiscool@meme.net')

bank_account.deposit(20).deposit(30).deposit(15).withdraw(50).yield_interest().display_account_info()
bank_account2.deposit(5).deposit(34).withdraw(10).withdraw(10).withdraw(15).withdraw(200).yield_interest().display_account_info()
bank_account3.make_deposit(20).make_withdrawl(15).display_user_balance()