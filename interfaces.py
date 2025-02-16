from abc import ABC, abstractmethod

class Updatable(ABC):
    @abstractmethod
    def update(self, amount):
        pass

class Notifiable(ABC):
    @abstractmethod
    def near_notify(self):
        pass
    @abstractmethod
    def exceed_notify(self):
        pass

class Lockable(ABC):
    @abstractmethod
    def lock(self):
        pass

class BudgetLockable(ABC):
    @abstractmethod
    def budget_lock(self):
        pass





