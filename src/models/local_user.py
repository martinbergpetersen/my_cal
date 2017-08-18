from src.interfaces.user import User


class LocalUser(User):
    """ local user
        data is from local computer
        param

        Attributes:
                username
                password
        Example:
            user = User('username',  'password')
    """

    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
