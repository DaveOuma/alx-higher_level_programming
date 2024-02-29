class BankAccount:
    """A class representing a bank account."""

    def __init__(self, account_number, balance):
        """
        Initializes a BankAccount object with the given account number and balance.

        Args:
            account_number (str): The account number.
            balance (float): The initial balance of the account.
        """
        self.account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.__balance

    def deposit(self, amount):
        """
        Deposits the given amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        self.__balance += amount

    def withdraw(self, amount):
        """
        Withdraws the given amount from the account, if possible.

        If the withdrawal amount exceeds the balance, prints "Insufficient balance".

        Args:
            amount (float): The amount to withdraw.
        """
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

