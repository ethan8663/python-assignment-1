"""
This module contains user classes.
"""

from abc import ABC
from interfaces import Notifiable, Lockable

class User(Notifiable, ABC):
    """
    This abstract class represent a user.
    """

    def __init__(self, name, age, user_type):
        """
        Constructs an object.
        :param name:      the name
        :param age:       the age
        :param user_type: the user type
        """
        self._name      = name
        self._age       = age
        self._user_type = user_type

    def __str__(self):
        """
        Methods to be implemented.
        """
        pass

    @property
    def user_type(self):
        """
        Returns the user type.
        :return: the user type
        """
        return self._user_type

    @property
    def name(self):
        """
        Returns the name of the user.
        :return: the name
        """
        return self._name

class Angel(User):
    """
    Represents an angel user
    """

    def __init__(self, name, age, user_type):
        """
        Constructs an object.
        :param name:      the name
        :param age:       the age
        :param user_type: the user type
        """
        super().__init__(name, age, user_type)

    def __str__(self):
        """
        Returns a string representation of the user.
        :return: a string
        """
        return f"{self._name}(Angel)"

    def near_notify(self):
        """
        Informs the user is nearing the limit
        """
        print(f"{self.name} is nearing the budget limit")

    def exceed_notify(self):
        """
        Informs the user is exceeding the limit
        """
        print(f"{self.name} exceeded the budget limit")

class Rebel(User, Lockable):
    """
    Represents an rebel user
    """
    def __init__(self, name, age, user_type):
        """
        Constructs an object.
        :param name:      the name
        :param age:       the age
        :param user_type: the user type
        """
        super().__init__(name, age, user_type)

    def __str__(self):
        """
        Returns a string representation of the user.
        :return: a string
        """
        return f"{self._name}(Rebel)"

    def near_notify(self):
        """
        Informs the user is nearing the limit
        """
        print(f"{self.name} is nearing the budget limit")

    def exceed_notify(self):
        """
        Informs the user is exceeding the limit
        """
        print(f"{self.name} exceeded the budget limit")

    def lock(self):
        """
        Informs the user is locked
        """
        print(f"{self.name} account is locked")

class TroubleMaker(User):
    """
    Represents a troublemaker user.
    """
    def __init__(self, name, age, user_type):
        """
        Constructs an object.
        :param name:      the name
        :param age:       the age
        :param user_type: the user type
        """
        super().__init__(name, age, user_type)

    def __str__(self):
        """
        Returns a string representation of the user.
        :return: a string
        """
        return f"{self._name}(Troublemaker)"

    def near_notify(self):
        """
        Informs the user is nearing the limit
        """
        print(f"{self.name} is nearing the budget limit")

    def exceed_notify(self):
        """
        Informs the user is exceeding the limit
        """
        print(f"{self.name} exceeded the budget limit")

class UserFactory:
    """
    Factory class to create users
    """
    _registry = {}

    @staticmethod
    def register(name, ref):
        """
        Registers a new user type
        :param name: the name
        :param ref:  the reference
        """
        UserFactory._registry[name] = ref

    @staticmethod
    def get_instance(name, age, user_type):
        """
        Gets an instance of user type
        :param name:      the name
        :param age:       the age
        :param user_type: the user type
        :return:          an instance
        """
        return UserFactory._registry[user_type](name, age, user_type)

