""" Event metaclass """
from abc import ABCMeta, abstractproperty, abstractmethod


class AbsEvent(metaclass=ABCMeta):

    """ Event class
            properties:
                - date
                - title
                - description
                - rating
                - user
                - rating
    """

    @abstractproperty
    def date(self):
        pass

    @abstractproperty
    def title(self):
        pass

    @abstractproperty
    def description(self):
        pass

    @abstractproperty
    def rating(self):
        pass

    @abstractproperty
    def user(self):
        pass

    @abstractproperty
    def group(self):
        pass

    @abstractmethod
    def create(self, storage):
        """ abstract create
        """
        pass

    @classmethod
    @abstractmethod
    def read(cls, key, val, storage):
        """ abstract read
         class method
            prop:
                key
                value
        """
        pass

    @classmethod
    @abstractmethod
    def update(cls, key, val, storage):
        """ abstract update
        class method
        """
        pass

    @classmethod
    @abstractmethod
    def delete(cls, key, val, storage):
        """ abstract delete
        class method
        """
        pass
