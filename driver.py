from FAM_account import FAMAccount
from user import UserFactory, Angel, TroubleMaker, Rebel
from transaction import TransactionManagerFactory, AngelTransactionManager, RebelTransactionManager, \
    TroubleMakerTransactionManager


class Menu:
    def __init__(self):
        self._FAM_account_list = []
        self._selected_account = None

    def check_account_locked(self):
        return self._selected_account.is_locked()


    def start(self):
        print("Welcome to the FAM! Select from the options below")
        while True:
            print("1. Register new user")
            print("2. Login existing user")
            print("3. Exit program")

            user_input = int(input())
            if user_input == 1:
                self.create_account()
            elif user_input == 2:
                self.show_fam_account_list()
            elif user_input == 3:
                print("Thank you for using FAM")
                break
            else:
                print("wrong input")

            while self._selected_account is not None:
                print("1. View Budgets")
                print("2. Record a Transaction")
                print("3. View Transactions by Budget ")
                print("4. View Bank Account Details")
                print("5. Logout")

                user_input = int(input())
                if user_input == 1:
                    self._selected_account.view_budgets()
                elif user_input == 2:
                    self._selected_account.record_transaction()
                    if self.check_account_locked():
                        self._selected_account = None
                elif user_input == 3:
                    self._selected_account.view_transactions_by_budget()
                elif user_input == 4:
                    self._selected_account.view_bank_account_details()
                elif user_input == 5:
                    self._selected_account = None
                else:
                    print("wrong input")




    def create_account(self):
        print("Registering a new user")
        f_account = FAMAccount()
        self._FAM_account_list.append(f_account)
        self._selected_account = f_account
        print(f"Logged in as {self._selected_account}")

    def show_fam_account_list(self):
        if not self._FAM_account_list:
            print("There is no account")
            return

        print("Select users to log in as")

        while True:
            for i in range(len(self._FAM_account_list)):
                if self._FAM_account_list[i].is_locked():
                    print(f"{i + 1}. {self._FAM_account_list[i]}- LOCKED")
                else:
                    print(f"{i + 1}. {self._FAM_account_list[i]}")

            index = int(input())
            if self._FAM_account_list[index - 1].is_locked():
                print(f"{self._FAM_account_list[index - 1].get_account_name()}'s account is LOCKED, they can not log in")
            else:
                self._selected_account = self._FAM_account_list[index - 1]
                print(f"Logged in as {self._selected_account}")
                break



def main():
    UserFactory.register("angel", Angel)
    UserFactory.register("troublemaker", TroubleMaker)
    UserFactory.register("rebel", Rebel)

    TransactionManagerFactory.register("angel", AngelTransactionManager)
    TransactionManagerFactory.register("troublemaker", TroubleMakerTransactionManager)
    TransactionManagerFactory.register("rebel", RebelTransactionManager)

    menu  = Menu()
    menu.start()


if __name__ == "__main__":
    main()