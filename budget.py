"""
This module has all kind of budgets.
"""

from abc import ABC
from interfaces import Updatable, BudgetLockable

class Budget(Updatable, BudgetLockable, ABC):
    """
    Represents a budget.
    """

    def __init__(self, total):
        """
        Constructs an object.
        Sets total and amount left with the given total, amount spent as 0 and is locked false.

        :param total: the total
        """
        self._total        = total
        self._amount_spent = 0
        self._amount_left  = total
        self._is_locked    = False

    def update(self, amount):
        """
        Updates amount spent and amount left.

        :param amount: the amount
        """
        self._amount_spent += amount
        self._amount_left  -= amount

    def budget_lock(self):
        """
        Locks the budget.
        """
        self._is_locked = True

    def is_locked(self):
        """
        Checks if the budget is locked.

        :return: true or false
        """
        return self._is_locked

    @property
    def total(self):
        """
        Returns the total.

        :return: the total
        """
        return self._total

    @property
    def amount_spent(self):
        """
        Returns the amount spent.

        return: the amount spent
        """
        return self._amount_spent


class GameAndEntertainment(Budget):
    """
    Represents a game and entertainment budget.
    """

    def __init__(self, total):
        """
        Constructs an object.
        :param total: the total
        """
        super().__init__(total)

    def __str__(self):
        """
        Returns a string representation of the budget.
        :return: a string
        """
        return f"Game budget: ${self._amount_left}"

    @classmethod
    def get_instance(cls):
        """
        Returns an instance of this class.
        :return: the instance
        """
        print("Initializing game and entertainment")
        total = float(input("Enter the total amount of budget: "))
        return cls(total)

class ClothingAndAccessories(Budget):
    """
    Represents a clothing and accessories budget.
    """

    def __init__(self, total):
        """
        Constructs an object.
        :param total: the total
        """
        super().__init__(total)

    def __str__(self):
        """
        Returns a string representation of the budget.
        :return: a string
        """
        return f"Clothing budget: ${self._amount_left}"

    @classmethod
    def get_instance(cls):
        """
        Returns an instance of this class.
        :return: a instance
        """
        print("Initializing clothing and accessories")
        total = float(input("Enter the total amount of budget: "))
        return cls(total)

class EatingOut(Budget):
    """
    Represents a eating out budget.
    """

    def __init__(self, total):
        """
        Constructs an object.
        :param total: the total
        """
        super().__init__(total)

    def __str__(self):
        """
        Returns a string representation of the budget.
        :return: a string
        """
        return f"Eating budget: ${self._amount_left}"

    @classmethod
    def get_instance(cls):
        """
        Returns an instance of this class.
        :return: an instance
        """
        print("Initializing eating out")
        total = float(input("Enter the total amount of budget: "))
        return cls(total)

class Miscellaneous(Budget):
    """
    Represents a miscellaneous budget.
    """

    def __init__(self, total):
        """
        Constructs an object.
        :param total: the total
        """

        super().__init__(total)

    def __str__(self):
        """
        Returns a string representation of the budget.
        :return: a string
        """
        return f"Misc budget: ${self._amount_left}"

    @classmethod
    def get_instance(cls):
        """
        Returns an instance of this class.
        :return: an instance
        """
        print("Initializing miscellaneous")
        total = float(input("Enter the total amount of budget: "))
        return cls(total)

class AllBudgets:
    """
    Represents all budgets.
    """

    def __init__(self):
        """
        Constructs an object with initializing all the budgets and storing them in the dictionary.
        """

        self._budgets = {}
        self.initialize()

    def initialize(self):
        """
        initializes the budgets.
        """

        game          = GameAndEntertainment.get_instance()
        clothing      = ClothingAndAccessories.get_instance()
        eating        = EatingOut.get_instance()
        miscellaneous = Miscellaneous.get_instance()

        self._budgets["Game and Entertainment"]   = game
        self._budgets["Clothing and Accessories"] = clothing
        self._budgets["Eating out"]               = eating
        self._budgets["Miscellaneous"]            = miscellaneous

    def print_all(self):
        """
        Prints all budgets.
        """

        for budget in self._budgets.values():
            if budget.is_locked():
                print(f"{budget} (locked)")
            else:
                print(budget)

    def count_locked(self):
        """
        Counts the number of locked budgets.
        :return: the count
        """

        count = 0
        for budget in self._budgets.values():
            if budget.is_locked():
                count += 1
        return count

    def get_category(self, category):
        """
        Gets category from the dictionary.

        :param category: the category to search
        :return: the category
        """
        return self._budgets[category]

    def generate_test(self):
        """
        Generates a test budget.
        """
        self._budgets["Game and Entertainment"] = GameAndEntertainment(100)
        self._budgets["Clothing and Accessories"] = ClothingAndAccessories(100)
        self._budgets["Eating out"] = EatingOut(100)
        self._budgets["Miscellaneous"] = Miscellaneous(100)

