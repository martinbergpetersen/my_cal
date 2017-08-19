from abc import ABCMeta, abstractproperty


class AbsUser(metaclass=ABCMeta):
    """ localuser class
            properties:
                - username
                - password
    """
    @abstractproperty
    def username(self):
        pass

    @abstractproperty
    def password(self):
        pass
