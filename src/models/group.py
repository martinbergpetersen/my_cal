class Group():
    """ Group class to attach a event to a group
    """
    def __init__(self, name):
        self._name = name
        pass

    @property
    def name(self):
        return self._name
