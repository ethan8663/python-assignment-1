from abc import ABC
from interfaces import Updatable, BudgetLockable

class Budget(Updatable, BudgetLockable, ABC):
    def __init__(self, total):
        self._total = total
        self._amount_spent = 0
        self._amount_left = total
        self._is_locked = False

    def update(self, amount):
        self._amount_spent += amount
        self._amount_left -= amount

    def budget_lock(self):
        self._is_locked = True

    def is_locked(self):
        return self._is_locked

    @property
    def total(self):
        return self._total

    @property
    def amount_spent(self):
        return self._amount_spent


class GameAndEntertainment(Budget):
    def __init__(self, total):
        super().__init__(total)

    def __str__(self):
        return f"Game budget: ${self._amount_left}"

    @classmethod
    def get_instance(cls):
        print("Initializing game and entertainment")
        total = float(input("Enter the total amount of budget: "))
        return cls(total)

class ClothingAndAccessories(Budget):
    def __init__(self, total):
        super().__init__(total)

    def __str__(self):
        return f"Clothing budget: ${self._amount_left}"

    @classmethod
    def get_instance(cls):
        print("Initializing clothing and accessories")
        total = float(input("Enter the total amount of budget: "))
        return cls(total)

class EatingOut(Budget):
    def __init__(self, total):
        super().__init__(total)

    def __str__(self):
        return f"Eating budget: ${self._amount_left}"

    @classmethod
    def get_instance(cls):
        print("Initializing eating out")
        total = float(input("Enter the total amount of budget: "))
        return cls(total)

class Miscellaneous(Budget):
    def __init__(self, total):
        super().__init__(total)

    def __str__(self):
        return f"Misc budget: ${self._amount_left}"

    @classmethod
    def get_instance(cls):
        print("Initializing miscellaneous")
        total = float(input("Enter the total amount of budget: "))
        return cls(total)

class AllBudgets:
    def __init__(self):
        self._budgets = {}
        self.initialize()
        # self.generate_test()

    def initialize(self):
        game = GameAndEntertainment.get_instance()
        clothing = ClothingAndAccessories.get_instance()
        eating = EatingOut.get_instance()
        miscellaneous = Miscellaneous.get_instance()

        self._budgets["Game and Entertainment"] = game
        self._budgets["Clothing and Accessories"] = clothing
        self._budgets["Eating out"] = eating
        self._budgets["Miscellaneous"] = miscellaneous

    def print_all(self):
        for budget in self._budgets.values():
            if budget.is_locked():
                print(f"{budget} (locked)")
            else:
                print(budget)

    def count_locked(self):
        count = 0
        for budget in self._budgets.values():
            if budget.is_locked():
                count += 1
        return count

    def get_category(self, category):
        return self._budgets[category]

    def generate_test(self):
        self._budgets["Game and Entertainment"] = GameAndEntertainment(100)
        self._budgets["Clothing and Accessories"] = ClothingAndAccessories(100)
        self._budgets["Eating out"] = EatingOut(100)
        self._budgets["Miscellaneous"] = Miscellaneous(100)

