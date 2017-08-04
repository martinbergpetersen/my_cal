""" Calender module
    defines the calendar class"""
from models.abstract.storage import IStorage


class Event(IStorage):
    """  event class
    Prop:
        date
        description
        rating
    """

    def __init__(self, date, description, time):
        self.date = date
        self.description = description
        self.time = time

    def save(self):
        """ save the event
        prop:
            __init__ object, must contain a full event
        """
        pass

    def update(self):
        """ update event
        prop:
            __init__ object, must contain a full event
        """
        pass
