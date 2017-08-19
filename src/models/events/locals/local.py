""" Calender module
    defines the calendar class"""
# from models.interfaces.storage import Storage
from src.abstracts.abs_event import AbsEvent


class Local(AbsEvent):
    """  event class
    uses the 'Event' abstract class
    Prop:
        date
        description
        rating
        user
        group
    Methods:
        create
        read
    """

    def __init__(self, date, title,  description,
                 rating, user=None, group=None):

        self._date = date
        self._description = description
        self._rating = rating
        self._title = title
        self._user = user
        self._group = group

    @property
    def date(self):
        return self._date

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def rating(self):
        return self._rating

    @property
    def user(self):
        return self._user

    @property
    def group(self):
        return self._group

    def create(self, storage):
        return 1

    @classmethod
    def read(cls, key, val, storage):
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
        return 1

    @classmethod
    def update(cls, key, val, storage):
        return 1

    @classmethod
    def delete(cls, key, val, storage):
        return 1
