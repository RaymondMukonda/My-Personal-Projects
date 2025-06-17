class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initailAmount, acctName):
        self.balance = initailAmount
        self.name = acctName
        print(f"\nAccount {self.name} has been created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount {self.name} Balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"\n{self.name}'s Deposit completed.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account {self.name} only has a balance of ${self.balance}"
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nwithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interruped: {error}")

    def transfer(self, amount, account):
        try:
            print("\n********************\nBeginning Transfer..")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete.\n\********************")
        except BalanceException as error:
            print(f"Transfer interrupted.{error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initailAmount, acctName):
        super().__init__(initailAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")