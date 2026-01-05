class BankAccount:
    def __init__(self, name="Bill", amount = 1000):
        self.name = name
        self.balance = amount

    def __str__(self):
        s = f"Le solde du compte bancaire de {self.name} est de {self.balance:.2f} euros"
        return s
    
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

# utilisation des classes

account1 = BankAccount("Tim", 800)
account1.deposit(350)
account1.withdraw (200)
print(account1)

account2 = BankAccount()
account2.deposit(25)
print(account2)

# attribut, parameter, 