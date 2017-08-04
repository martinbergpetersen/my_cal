""" a csv handler """

from models.abstract.storage import IStorage
import csv


class CSV(IStorage):

    """ CSV handler
    methods:
        save
        read
        update
        delete
    """
