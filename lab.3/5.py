class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  
        self.balance = balance  
    
    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
       
        if amount > self.balance:
            print("Insufficient funds! Cannot withdraw more than available balance.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")
        else:
            print("Withdrawal amount must be positive.")
    
    def get_balance(self):
       
        return self.balance


account = BankAccount("John Doe", 1000)


account.deposit(500)  
account.withdraw(200)  
account.withdraw(1500)  


print(f"Current balance: {account.get_balance()}")
