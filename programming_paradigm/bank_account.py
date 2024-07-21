class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            print("Insufficient funds.")  # Updated to match the expected output
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

# Example usage (for testing purposes)
if __name__ == "__main__":
    account = BankAccount(100)  # Example starting balance
    account.deposit(50)
    account.withdraw(20)
    account.display_balance()
