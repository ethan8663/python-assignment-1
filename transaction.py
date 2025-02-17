"""
This module contains transaction and transaction maanger classes.
"""

from abc import ABC, abstractmethod
from datetime import datetime

class Transaction:
    """
    This class represents a transaction.
    """

    def __init__(self, time, amount, category, where):
        """
        Constructs an object.
        :param time:     the time
        :param amount:   the amount
        :param category: the category
        :param where:    the where
        """
        self._time     = time
        self._amount   = amount
        self._category = category
        self._where    = where

    def __str__(self):
        """
        Returns a string representation of the object.
        :return: a string
        """
        return f"{self._time}\n${self._amount} spent at {self._where}({self._category})\n"

    @property
    def amount(self):
        """
        Returns the amount of the transaction.
        :return: the amount
        """
        return self._amount

    @property
    def category(self):
        """
        Returns the category of the transaction.
        :return: the category
        """
        return self._category

    @classmethod
    def create_transaction(cls):
        """
        Creates a new transaction.
        :return: a transaction
        """
        print("Create transaction")
        amount         = float(input("Amount: "))
        category_input = int(
            input("Category:\n 1. Game and Entertainment 2. Clothing and Accessories 3. Eating out 4. Miscellaneous: "))
        where          = input("Where: ")
        current_time   = datetime.now()

        match category_input:
            case 1:
                category = "Game and Entertainment"
            case 2:
                category = "Clothing and Accessories"
            case 3:
                category = "Eating out"
            case 4:
                category = "Miscellaneous"
            case _:
                print("Invalid category")
                return

        return cls(current_time, amount, category, where)

class TransactionManager(ABC):
    """
    This abstract class represents a transaction manager.
    """

    def __init__(self, FAM_account):
        """
        Constructs an object with creating a transaction.
        :param FAM_account: the FAM account
        """

        self._FAM_account = FAM_account
        self._transaction = Transaction.create_transaction()
        self._category    = None

    @abstractmethod
    def check_notify(self):
        """
        Method to be implemented.
        """
        pass

    def check_balance(self):
        """
        Checks the balance whether it have enough funds.
        :return: true or false
        """
        if self._FAM_account.check_balance(self._transaction.amount):
            return True
        else:
            print("Not enough money!")
            return False

    def check_budget_locked(self):
        """
        Checks if the budget is locked.
        :return: true or false
        """
        self._category = self._FAM_account.get_category(self._transaction.category)

        if self._category.is_locked():
            print("This budget category is locked!")
            return True
        else:
            return False

    def record_transaction(self):
        """
        Record the transaction.
        """
        self._category.update(self._transaction.amount)
        self._FAM_account.bank_update(self._transaction.amount)
        self._FAM_account.add_transaction(self._transaction)

class AngelTransactionManager(TransactionManager):
    """
    Represents an Angel transaction manager.
    """

    def __init__(self, FAM_account):
        """
        Constructs an object with creating a transaction.
        :param FAM_account: the FAM account
        """
        super().__init__(FAM_account)

    def check_notify(self):
        """
        Checks if the transaction is notified.
        """
        if self._category.total < self._category.amount_spent:
            self._FAM_account.exceed_notify()
        elif self._category.total * 0.9 < self._category.amount_spent:
            self._FAM_account.near_notify()

class RebelTransactionManager(TransactionManager):
    """
    Represents an Rebel transaction manager.
    """

    def __init__(self, FAM_account):
        """
        Constructs an object with creating a transaction.
        :param FAM_account: the FAM account
        """
        super().__init__(FAM_account)

    def check_notify(self):
        """
        Checks if the transaction is notified.
        """
        if self._category.total < self._category.amount_spent:
            self._FAM_account.exceed_notify()
            self._category.budget_lock()
            print("Budget locked!")

            if self._FAM_account.count_locked() >= 2:
                self._FAM_account.lock()
                print("Account locked!")

        elif self._category.total * 0.5 < self._category.amount_spent:
            self._FAM_account.near_notify()

class TroubleMakerTransactionManager(TransactionManager):
    """
    Represents a Troublemaker transaction manager.
    """

    def __init__(self, FAM_account):
        """
        Constructs an object with creating a transaction.
        :param FAM_account: the FAM account
        """
        super().__init__(FAM_account)

    def check_notify(self):
        """
        Checks if the transaction is notified.
        """
        if self._category.total < self._category.amount_spent:
            self._FAM_account.exceed_notify()

            if self._category.total * 1.2 < self._category.amount_spent:
                self._category.budget_lock()
                print("Budget locked!")

        elif self._category.total * 0.75 < self._category.amount_spent:
            self._FAM_account.near_notify()

class TransactionManagerFactory:
    """
    Factory class for creating transaction managers.
    """
    _registry = {}
    @staticmethod
    def register(name, ref):
        """
        Registers a new transaction manager.
        :param name: the name
        :param ref:  the reference
        """
        TransactionManagerFactory._registry[name] = ref

    @staticmethod
    def get_instance(name):
        """
        Gets an existing transaction manager.
        :param name: the name
        :return:     the corresponding transaction manager
        """
        return TransactionManagerFactory._registry[name]
