from interfaces import Updatable

class Bank(Updatable):
    def __init__(self, name, number, balance):
        self._name = name
        self._number = number
        self._balance = balance

    def __str__(self):
        return f"Bank name: {self._name}, number: {self._number}, balance: {self._balance}"

    def update(self, amount):
        self._balance -= amount

    def check_balance(self, amount):
        return self._balance >= amount

    @property
    def balance(self):
        return self._balance

