""" a csv handler """
import csv # NOQA - use for later
from src.abstracts.abs_storage import AbsStorage
# from models.interfaces.event import Event


class CSV(AbsStorage):

    """ CSV handler
    methods:
        save
        read
        update
        delete
    """
    def __init__(self):
        pass

    @classmethod
    def create(cls, event):
        print("create")

    @classmethod
    def read(cls, key, val):
        """ read by
            Attri:
                key, val
                prefix:
                    event_XXX
                    user_username
                    group_name
                example of searching for the event date
                    result = read_by(key='event_date', value='2017-08-08')
        """
        print("read by id")

    @classmethod
    def update(cls, key, value):
        print("update")

    @classmethod
    def delete(cls, key, value):
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
