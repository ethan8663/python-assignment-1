"""
This module describes bank
"""

from interfaces import Updatable

class Bank(Updatable):
    """
    Represent a bank.
    """

    def __init__(self, name, number, balance):
        """
        Constructs an object.
        :param name:    the name
        :param number:  the number
        :param balance: the balance
        """
        self._name    = name
        self._number  = number
        self._balance = balance

    def __str__(self):
        """
        Returns a string representation of the object.
        :return: a string
        """
        return f"Bank name: {self._name}, number: {self._number}, balance: {self._balance}"

    def update(self, amount):
        """
        Updates the balance.

        :param amount: the amount
        """
        self._balance -= amount

    def check_balance(self, amount):
        """
        Checks the balance if the balance is bigger than the amount.
        :param amount: the amount
        :return: true or false
        """
        return self._balance >= amount

    @property
    def balance(self):
        """
        Returns the balance.

        :return: the balance
        """
        return self._balance

