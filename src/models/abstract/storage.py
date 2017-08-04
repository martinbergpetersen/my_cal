""" crud metaclass """

from abc import ABCMeta, abstractmethod


class IStorage(ABCMeta):
    """
    storage abstract class containing
    create, read, update, delete
    """

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
