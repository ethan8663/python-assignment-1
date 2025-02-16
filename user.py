from abc import ABC
from interfaces import Notifiable, Lockable

class User(Notifiable, ABC):
    def __init__(self, name, age, user_type):
        self._name = name
        self._age = age
        self._user_type = user_type

    def __str__(self):
        pass

    @property
    def user_type(self):
        return self._user_type

    @property
    def name(self):
        return self._name

class Angel(User):
    def __init__(self, name, age, user_type):
        super().__init__(name, age, user_type)

    def __str__(self):
        return f"{self._name}(Angel)"

    def near_notify(self):
        print(f"{self.name} is nearing the budget limit")

    def exceed_notify(self):
        print(f"{self.name} exceeded the budget limit")

class Rebel(User, Lockable):
    def __init__(self, name, age, user_type):
        super().__init__(name, age, user_type)

    def __str__(self):
        return f"{self._name}(Rebel)"

    def near_notify(self):
        print(f"{self.name} is nearing the budget limit")

    def exceed_notify(self):
        print(f"{self.name} exceeded the budget limit")

    def lock(self):
        print(f"{self.name} account is locked")

class TroubleMaker(User):
    def __init__(self, name, age, user_type):
        super().__init__(name, age, user_type)

    def __str__(self):
        return f"{self._name}(Troublemaker)"

    def near_notify(self):
        print(f"{self.name} is nearing the budget limit")

    def exceed_notify(self):
        print(f"{self.name} exceeded the budget limit")

class UserFactory:
    _registry = {}

    @staticmethod
    def register(name, ref):
        UserFactory._registry[name] = ref

    @staticmethod
    def get_instance(name, age, user_type):
        return UserFactory._registry[user_type](name, age, user_type)

