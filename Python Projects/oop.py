from bank_accounts import *

Rammy = BankAccount(1000, "Rammy")
sara = BankAccount(2000, "sara")

Rammy.getBalance()
sara.getBalance()

sara.deposit(500)
Rammy.withdraw(3000)


Rammy.transfer(10000,sara)
print("")
Rammy.transfer(300,sara)



jim = InterestRewardsAcct(1000, "jim")
jim.getBalance()
jim.deposit(100)
jim.transfer(100, Rammy)



blaze = SavingsAcct(1000, "blaze")
blaze.getBalance()
blaze.deposit(200)
blaze.transfer(200, Rammy)