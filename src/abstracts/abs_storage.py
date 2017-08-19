""" crud metaclass """
from abc import ABCMeta, abstractmethod


class AbsStorage(ABCMeta):
    """
    storage abstract class containing
    create, read, update, delete
    """

    @classmethod
    @abstractmethod
    def create(cls, event):
        """ abstract create
        """
        pass

    @classmethod
    @abstractmethod
    def read(cls, key, val):
        """ abstract read
         class methodself
            prop:
                key
                value
        """
        pass

    @classmethod
    @abstractmethod
    def update(cls, key, val):
        """ abstract update
        class method
        """
        pass

    @classmethod
    @abstractmethod
    def delete(cls, key, val):
        """ abstract delete
        class method
        """
        pass
