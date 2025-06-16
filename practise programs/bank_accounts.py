class BankAccount:
    def __init__(self, initailAmount, acctName):
        self.balance = initailAmount
        self.name = acctName
        print(f"\nAccount {self.name} has been created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount {self.name} has been created.\nBalance = ${self.balance:.2f}")