class BankAccount():
    def __init__(self,account_balance = 0):
        self.account_balance = account_balance
# acc1 = BankAccount()
# acc2 = BankAccount(200)
# print(acc1.account_balance)
# print(acc2.account_balance)

    def deposit(self,amount):
        self.account_balance += amount

# acc1 = BankAccount(100)
# acc1.deposit(50)
# print(f"Deposited: ${acc1.account_balance}")

    def withdraw(self,amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        else:
            print("Insufficient funds")
            return False

acc1 = BankAccount(100)

print(acc1.withdraw(30))     # should return True
print(acc1.account_balance)  # should now be 70

print(acc1.withdraw(100))    # should return False
print(acc1.account_balance)  # should still be 70
