""" Calender module
    defines the calendar class"""
# from models.interfaces.storage import Storage
from src.interfaces.event import Event


class Local(Event):
    """  event class
    uses the Event abstract class
    Prop:
        date
        description
        rating
    Info:
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
    # @Event.date.setter
    # def date(self, val):
    #     self.date = val
    #     return

    # @Event.description.setter
    # def description(self, val):
    #     self.description = val
    #     return

    # @Event.rating.setter
    # def rating(self, val):
    #     self.rating = val
    #     return
