""" Event metaclass """
from abc import ABCMeta, abstractproperty


class Event(metaclass=ABCMeta):

    """ Event class
            properties:
                - date
                - title
                - description
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

    def group(self):
        pass
