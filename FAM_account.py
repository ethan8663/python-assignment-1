"""
This module contains FAM account.
"""

from budget import AllBudgets
from interfaces import Lockable, BudgetLockable
from transaction import TransactionManagerFactory
from user import UserFactory, Angel, Rebel
from bank import Bank

class FAMAccount(Lockable):
    """
    Represents an FAM account
    """

    def __init__(self):
        """
        Constructs an object with creating user, bank, and budgets.
        """
        print("Create FAM account")
        self._user       = self.create_user()
        self._bank       = self.create_bank()
        self._allBudgets = AllBudgets()
        self._is_locked  = False
        self._all_transactions = []

    @staticmethod
    def create_user():
        """
        Creates a user.

        :return: a user
        """

        print("Create user")
        name       = input("Name: ")
        age        = int(input("Age: "))
        type_input = input("Select user type\n1. Angel 2. Troublemaker 3. Rebel:  ")

        match type_input:
            case "1":
                user_type = "angel"
            case "2":
                user_type = "troublemaker"
            case "3":
                user_type = "rebel"
            case _:
                print("Invalid input")
                return

        return UserFactory.get_instance(name, age, user_type)

    @staticmethod
    def create_bank():
        """
        Creates a bank object.
        :return: a bank
        """
        print("Create bank")

        bank_name    = input("Bank name: ")
        bank_number  = int(input("Bank number: "))
        bank_balance = float(input("Bank balance: "))

        return Bank(bank_name, bank_number, bank_balance)

    def __str__(self):
        """
        Represents an object as a string.

        :return: a string
        """
        return self._user.__str__()

    def view_budgets(self):
        """
        Views budgets.
        """
        print(f"{self._user.user_type} {self._user.name}'s balance is ${self._bank.balance}\n")
        self._allBudgets.print_all()

    def record_transaction(self):
        """
        Records transaction.
        """

        manager = TransactionManagerFactory.get_instance(self._user.user_type)(self)

        if manager.check_balance():
            if not manager.check_budget_locked():
                manager.record_transaction()
                manager.check_notify()

        if isinstance(manager, BudgetLockable):
            manager.budget_lock()

        if isinstance(manager, Lockable):
            manager.lock()

    def is_locked(self):
        """
        Checks whether a transaction is locked.
        :return: true or false
        """
        return self._is_locked

    def lock(self):
        """
        Locks the account
        """
        self._is_locked = True

    def check_balance(self, amount):
        """
        Checks balance to see if it can proceed the transaction or not.
        :param amount: the amount
        :return: true or false
        """
        return self._bank.check_balance(amount)

    def get_category(self, category):
        """
        Gets the category.
        :param category: the category.
        :return: the category
        """
        return self._allBudgets.get_category(category)

    def bank_update(self, amount):
        """
        Updates the bank balance.

        :param amount: the amount
        """
        self._bank.update(amount)

    def near_notify(self):
        """
        Notifies user is nearing the limit
        """
        self._user.near_notify()

    def exceed_notify(self):
        """
        Notifies user is exceeding the limit
        """
        self._user.exceed_notify()

    def count_locked(self):
        """
        Counts the number of locked budgets.
        :return: the count
        """
        return self._allBudgets.count_locked()

    def add_transaction(self, transaction):
        """
        Adds a transaction to the account.
        :param transaction: the transaction
        """
        self._all_transactions.append(transaction)

    def get_account_name(self):
        """
        Gets the account name.
        :return: the name
        """
        return self._user.name

    def view_transactions_by_budget(self):
        """
        Views transactions by budget.
        """

        user_input = int(input("1. Game and Entertainment 2. Clothing and Accessories 3. Eating out 4. Miscellaneous"))

        match user_input:
            case 1:
                category = "Game and Entertainment"
            case 2:
                category = "Clothing and Accessories"
            case 3:
                category = "Eating out"
            case 4:
                category = "Miscellaneous"
            case _:
                print("Invalid user type")
                return

        for transaction in self._all_transactions:
            if transaction.category == category:
                print(transaction)

    def view_bank_account_details(self):
        """
        Views bank account details.
        :return: the details
        """
        print(self._bank)

    #testing method
    def test_print(self):
        print(self._user)
        print(self._bank)
        print(self._allBudgets.print_all())

    def generate_test(self):
        self._user = Rebel("ethan", 12, "rebel")
        self._bank = Bank("Bank Name", 12, 1000)
        self._allBudgets = AllBudgets()
