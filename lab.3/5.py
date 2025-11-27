class BankAccount:

account=Bankaccount("John Doe",1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)

print(f"Current balance:{account.get_balance()}")