from budget import AllBudgets
from interfaces import Lockable, BudgetLockable
from transaction import TransactionManagerFactory
from user import UserFactory, Angel, Rebel
from bank import Bank

class FAMAccount(Lockable):
    def __init__(self):
        print("Create FAM account")
        self._user = self.create_user()
        self._bank = self.create_bank()
        self._allBudgets = AllBudgets()
        self._is_locked = False
        self._all_transactions = []

    @staticmethod
    def create_user():
        print("Create user")
        name = input("Name: ")
        age = int(input("Age: "))
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
        print("Create bank")
        bank_name = input("Bank name: ")
        bank_number = int(input("Bank number: "))
        bank_balance = float(input("Bank balance: "))
        return Bank(bank_name, bank_number, bank_balance)

    def __str__(self):
        return self._user.__str__()

    def view_budgets(self):
        print(f"{self._user.user_type} {self._user.name}'s balance is ${self._bank.balance}\n")
        self._allBudgets.print_all()

    def record_transaction(self):
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
        return self._is_locked

    def lock(self):
        self._is_locked = True

    def check_balance(self, amount):
        return self._bank.check_balance(amount)

    def get_category(self, category):
        return self._allBudgets.get_category(category)

    def bank_update(self, amount):
        return self._bank.update(amount)

    def near_notify(self):
        self._user.near_notify()

    def exceed_notify(self):
        self._user.exceed_notify()

    def count_locked(self):
        return self._allBudgets.count_locked()

    def add_transaction(self, transaction):
        self._all_transactions.append(transaction)

    def get_account_name(self):
        return self._user.name

    def view_transactions_by_budget(self):
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
