""" crud metaclass """
from abc import ABCMeta, abstractmethod


class Storage(ABCMeta):
    """
    storage abstract class containing
    create, read, update, delete
    """

    @abstractmethod
    def create(self):
        """ abstract create
        """
        pass

    @abstractmethod
    def read(self, key, val):
        """ abstract read
         class method
            prop:
                key
                value
        """
        pass

    @abstractmethod
    def update(self):
        """ abstract update
        class method
        """
        pass

    @abstractmethod
    def delete(self):
        """ abstract delete
        class method
        """
        pass
