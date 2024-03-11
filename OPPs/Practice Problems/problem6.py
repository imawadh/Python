class Account:
    def __init__(self,title = None, balance = 0):
        self.title = title
        self.balance = balance 
        

class SavingAccount(Account):
    def __init__ (self,title, balance, interest=0):
        super().__init__(title,balance)
        self.interest = interest
