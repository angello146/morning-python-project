class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number  # protected attribute
        self.__balance = balance  # private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount should be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Withdrawal amount should be greater than zero and less than or equal to balance.")

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, new_account_number):
        self._account_number = new_account_number


# Usage example
account1 = BankAccount("0798278998", 1000)

# Accessing account number (protected attribute)
print("Account Number:", account1.get_account_number())

# Accessing balance (private attribute) using getter method
print("Initial Balance:", account1.get_balance())

# Depositing and withdrawing money
account1.deposit(500)
account1.withdraw(200)

# Trying to directly access private attributes (name mangling example)
# This would actually not raise an error, but it's discouraged
print("Direct access to balance:", account1._BankAccount__balance)

# Changing account number using setter method (protected attribute)
account1.set_account_number("987654321")
print("New Account Number:", account1.get_account_number())
