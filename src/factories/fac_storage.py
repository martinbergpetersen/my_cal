""" A storage factory
"""
from inspect import getmembers, isclass, isabstract
import src.handlers as handlers


class StorageFactory(object):
    """ a storage factory

    """
    handlers = {}

    def __init__(self):
        self.load_storage()

    def load_storage(self):
        classes = getmembers(handlers,
                             lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, handlers.AbsStorage):
                self.handlers.update([[name, _type]])

    def create_instance(self, storagename):
        if storagename in self.handlers:
            return self.handlers[storagename]()
        else:
            return handlers.NullHandler(storagename)
