class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.04):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance() + 1000:
            if amount <= self.get_balance():
                super().withdraw(amount)
            else:
                print("Overdraft limit exceeded or used.")
                print("This simple account does not track overdraft debt.")
        else:
            print("Withdrawal exceeds the permitted limit.")


account = SavingsAccount("Raman", 5000)

account.deposit(1000)
account.withdraw(500)
account.add_interest()

print("Account holder:", account.name)
print("Final balance:", round(account.get_balance(), 2))

current = CurrentAccount("Student", 2000)
current.withdraw(500)
print("Current account balance:", current.get_balance())