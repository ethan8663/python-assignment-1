from abc import ABC, abstractmethod
from datetime import datetime

class Transaction:
    def __init__(self, time, amount, category, where):
        self._time = time
        self._amount = amount
        self._category = category
        self._where = where

    def __str__(self):
        return f"{self._time}\n${self._amount} spent at {self._where}({self._category})\n"

    @property
    def amount(self):
        return self._amount

    @property
    def category(self):
        return self._category

    @classmethod
    def create_transaction(cls):
        print("Create transaction")
        amount = float(input("Amount: "))
        category_input = int(
            input("Category:\n 1. Game and Entertainment 2. Clothing and Accessories 3. Eating out 4. Miscellaneous: "))
        where = input("Where: ")
        current_time = datetime.now()

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
                print("Invalid category")  # transaction이 none 이 될수도 있음 그래서 밖에서 none 이면(숫자를 잘못입력했으면 진행 안되게 해줘야함 )
                return

        return cls(current_time, amount, category, where)

class TransactionManager(ABC):
    def __init__(self, FAM_account):
        self._FAM_account = FAM_account
        self._transaction = Transaction.create_transaction()
        self._category = None

    @abstractmethod
    def check_notify(self):
        pass

    def check_balance(self):
        if self._FAM_account.check_balance(self._transaction.amount):
            print("enough money")
            return True
        else:
            print("Not enough money!")
            return False

    def check_budget_locked(self):
        self._category = self._FAM_account.get_category(self._transaction.category)

        if self._category.is_locked():
            print("This budget category is locked!")
            return True
        else:
            return False

    def record_transaction(self):
        self._category.update(self._transaction.amount)
        self._FAM_account.bank_update(self._transaction.amount)
        self._FAM_account.add_transaction(self._transaction)

class AngelTransactionManager(TransactionManager):
    def __init__(self, FAM_account):
        super().__init__(FAM_account)

    def check_notify(self):
        if self._category.total < self._category.amount_spent:
            self._FAM_account.exceed_notify()
        elif self._category.total * 0.9 < self._category.amount_spent:
            self._FAM_account.near_notify()

class RebelTransactionManager(TransactionManager):
    def __init__(self, FAM_account):
        super().__init__(FAM_account)

    def check_notify(self):
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
    def __init__(self, FAM_account):
        super().__init__(FAM_account)

    def check_notify(self):
        if self._category.total < self._category.amount_spent:
            self._FAM_account.exceed_notify()

            if self._category.total * 1.2 < self._category.amount_spent:
                self._category.budget_lock()
                print("Budget locked!")

        elif self._category.total * 0.75 < self._category.amount_spent:
            self._FAM_account.near_notify()

class TransactionManagerFactory:
    _registry = {}
    @staticmethod
    def register(name, ref):
        TransactionManagerFactory._registry[name] = ref

    @staticmethod
    def get_instance(name):
        return TransactionManagerFactory._registry[name]
