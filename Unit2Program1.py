class BankAccount:

    # Constructor to initialize account number and balance
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    # Method to check balance
    def check_balance(self):
        print("Current Balance:", self.balance)


# Creating object of class
account1 = BankAccount(12345, 5000)

print("Account Number:", account1.acc_no)

account1.deposit(2000)
account1.withdraw(1500)
account1.check_balance()