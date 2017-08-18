""" a csv handler """
import csv # NOQA - use for later
from src.interfaces.storage import Storage
# from models.interfaces.event import Event


class CSV(Storage):

    """ CSV handler
    methods:
        save
        read
        update
        delete
    """
    def __init__(self, event=None):
        self.event = event

    def create(self):
        print("create")

    def read(self, key, val):
        """ read by
            Attri:
                key for searching
                prefix:
                    event_XXX
                    user_username
                    group_name
                example of searching for the event date
                    result = read_by('event_date')
                val:
                    '2017-08-08'
        """
        print("read by id")

    def update(self):
        print("update")

    def delete(self):
        print("delete")

    # TODO
    @classmethod
    def __read_by_event(key, value):
        pass

    # TODO
    @classmethod
    def __read_by_user(key, value):
        pass

    # TODO
    @classmethod
    def __read_by_group(key, value):
        pass
