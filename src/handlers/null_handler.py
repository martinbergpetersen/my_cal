from src.abstracts.abs_storage import AbsStorage


class NullHandler(AbsStorage):

    """ Nullhandler
    """
    def __init__(self, storagename):
        self.storagename = storagename
        pass

    def create(self):
        print("Not a valid handler" + self.storagename)

    def read(self):
        print("Not a valid handler" + self.storagename)

    def update(self):
        print("Not a valid handler" + self.storagename)

    def delete(self):
        print("Not a valid handler" + self.storagename)
