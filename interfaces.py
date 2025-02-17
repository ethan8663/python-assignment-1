"""
This module stores all the interfaces.
"""
from abc import ABC, abstractmethod

class Updatable(ABC):
    """
    Represents an updatable interface.
    """

    @abstractmethod
    def update(self, amount):
        """
        Methods to be implemented
        :param amount: the amount
        """
        pass

class Notifiable(ABC):
    """
    Represents a notifiable interface.
    """

    @abstractmethod
    def near_notify(self):
        """
        Method to be implemented
        """
        pass

    @abstractmethod
    def exceed_notify(self):
        """
        Method to be implemented
        """
        pass

class Lockable(ABC):
    """
    Represents a lockable interface.
    """
    @abstractmethod
    def lock(self):
        """
        Method to be implemented
        """
        pass

class BudgetLockable(ABC):
    """
    Represents a budget lockable interface.
    """
    @abstractmethod
    def budget_lock(self):
        """
        Method to be implemented
        """
        pass





