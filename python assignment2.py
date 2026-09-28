class Bank:

    def login(self):
        username = input("Username: ")
        pin = input("PIN: ")

        if username == "neymar" and pin == "1234":
            print("Login successful")
            return True
        else:
            print("Invalid login")
            return False

    def deposit(self, balance):
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Balance:", balance)
        else:
            print("Enter a valid amount")

        return balance

    def withdraw(self, balance):
        amount = int(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Balance:", balance)
        else:
            print("Invalid amount")

        return balance


bank = Bank()
balance = 5000

if bank.login():

    balance = bank.deposit(balance)

    balance = bank.withdraw(balance)

    print("Final Balance:", balance)
